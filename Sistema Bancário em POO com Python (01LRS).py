import textwrap
from abc import ABC, abstractmethod


class Historico():
    def __init__(self):
        self.transacoes = []
    
    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao) 

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.depositar(self)

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.sacar(self)

class Cliente():
    def __init__(self, endereco):
        self.endereco = endereco 
        self.contas = []

    def realizar_transacao(self, conta, transacao): 
        transacao.registrar(conta)
        

    def adicionar_conta(self, conta):
        self.contas.append(conta)
        

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome 
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta():
    def __init__(self, numero, agencia, cliente):
        self._saldo = 0 
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico() 
        self._numero_saques = 0 

    def saldo(self):
        return self._saldo

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, '0001', cliente)
    
    def sacar(self, transacao):
        valor = transacao.valor
        excedeu_saldo = valor > self._saldo
        excedeu_limite = valor > self.limite
        excedeu_saques = self._numero_saques >= self.limite_saques

        if excedeu_saldo: 
            print ('O valor é maior do que o saldo disponível!')
            return False

        elif excedeu_limite: 
            print ('O valor do saque é maior que o limite por operação... Tente novamente')
            return False

        elif excedeu_saques: 
            print ('Seu número de saques já realiados atingiu o máximo permitido. Tente novamente amanhã!')
            return False

        else: 
            self._saldo -= valor 
            self._numero_saques += 1
            self.historico.adicionar_transacao(transacao)
            print ('\n=== Saque Realizado com Sucesso! ===')
            return True
        
    def depositar(self,transacao):
        valor = transacao.valor
        if valor > 0:
            self._saldo += valor 
            self.historico.adicionar_transacao(transacao)
            print ('\n=== Seu depósito foi realizado com sucesso! ===')
            return True 

        else:
            print ('\n @@@ Operação Falhou! O valor informado é inválido para esta operação! @@@')
            return False 


class ContaCorrente(Conta):
    def __init__(self, numero, agencia, cliente, limite=500, limite_saques=3):
        super().__init__(numero, agencia, cliente)
        self.limite = float(limite)
        self.limite_saques = int(limite_saques)

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def exibir_extrato(conta):
    print("\n================ EXTRATO ================")
    if not conta.historico.transacoes:
        print("Não foram realizadas movimentações.")
    else:
        for transacao in conta.historico.transacoes:
            print(f"{transacao.__class__.__name__}:\tR$ {transacao.valor:.2f}")
    print(f"\nSaldo:\t\tR$ {conta.saldo():.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuario = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    usuarios.append(usuario)

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario.cpf == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        conta = ContaCorrente.nova_conta(cliente=usuario, numero=numero_conta)
        usuario.adicionar_conta(conta)
        print("\n=== Conta criada com sucesso! ===")
        return conta

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta.agencia}
            C/C:\t\t{conta.numero}
            Titular:\t{conta.cliente.nome}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
    
def main():

    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            transacao = Deposito(valor)
            conta = contas[0]
            cliente = conta.cliente
            cliente.realizar_transacao(conta,transacao)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            transacao = Saque(valor)
            conta = contas[0]
            cliente = conta.cliente
            cliente.realizar_transacao(conta,transacao)

        elif opcao == "e":
            conta = contas[0]
            exibir_extrato(conta)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()