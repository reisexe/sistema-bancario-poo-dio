# 🏦 Sistema Bancário em POO com Python

Projeto desenvolvido como desafio da trilha **Luizalabs Back-end com Python** na plataforma [DIO](https://www.dio.me/), com o objetivo de evoluir um sistema bancário procedural para uma arquitetura orientada a objetos.

---

## 📌 Sobre o Projeto

O sistema simula operações bancárias básicas como depósito, saque e extrato, modelado seguindo um diagrama UML com classes, herança, encapsulamento e interfaces abstratas.

---

## 🧱 Arquitetura — Diagrama de Classes

    Transacao (ABC)
    ├── Deposito
    └── Saque

    Cliente
    └── PessoaFisica

    Conta
    └── ContaCorrente

    Historico

---

## 🚀 Funcionalidades

- ✅ Cadastro de usuários (Pessoa Física)
- ✅ Criação de contas correntes
- ✅ Depósito
- ✅ Saque com validação de limite por operação e limite de saques diários
- ✅ Extrato com histórico de transações
- ✅ Listagem de contas

---

## 🧠 Conceitos de POO Aplicados

| Conceito | Onde foi aplicado |
|---|---|
| Classes e __init__ | Todas as classes do sistema |
| Herança | PessoaFisica → Cliente, ContaCorrente → Conta, Deposito/Saque → Transacao |
| super() | PessoaFisica e ContaCorrente aproveitam o __init__ da classe mãe |
| Classe Abstrata (ABC) | Transacao define interface obrigatória para Deposito e Saque |
| @abstractmethod | Método registrar() obrigatório em todas as transações |
| Encapsulamento | _saldo e _numero_saques protegidos na classe Conta |
| @classmethod | Conta.nova_conta() como factory method |
| Composição | Conta possui um objeto Historico |
| Polimorfismo | realizar_transacao() funciona com qualquer tipo de Transacao |

---

## 🗂️ Estrutura das Classes

**Historico** — Armazena todas as transações realizadas em uma conta.

**Transacao (ABC)** — Interface abstrata que obriga Deposito e Saque a implementarem o método registrar(conta).

**Deposito e Saque** — Implementam Transacao. Cada uma sabe como se registrar em uma conta.

**Cliente** — Classe base com endereço e lista de contas. Métodos: realizar_transacao() e adicionar_conta().

**PessoaFisica** — Herda de Cliente. Adiciona cpf, nome e data_nascimento.

**Conta** — Coração do sistema. Gerencia saldo, histórico e operações. Possui @classmethod nova_conta() como factory.

**ContaCorrente** — Herda de Conta. Adiciona limite (R$ 500,00) e limite_saques (3 por dia).

---

## 🖥️ Como Executar

Clone o repositório e execute:

    git clone https://github.com/reisexe/sistema-bancario-poo-dio.git
    cd sistema-bancario-poo-dio
    python "Sistema Bancário em POO com Python (01LRS).py"

**Fluxo recomendado:**

1. [nu] → Criar usuário
2. [nc] → Criar conta
3. [d] → Depositar
4. [s] → Sacar
5. [e] → Ver extrato

---

## 🛠️ Tecnologias

- Python 3.x
- Módulo abc (Abstract Base Classes)
- Módulo textwrap

---

## 👨‍💻 Autor

Feito por **Leonardo Reis** • [GitHub](https://github.com/reisexe)

Desafio proposto pela [DIO](https://www.dio.me/) — Trilha Luizalabs Back-end com Python.
