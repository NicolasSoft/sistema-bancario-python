import json
from models.cliente import Cliente
from models.conta import Conta

class Banco:
    def __init__(self, arquivo="data/banco.json"):
        self.arquivo = arquivo
        self.clientes = {}
        self.contas = {}
        self.carregar_dados()

    def criar_cliente(self, nome, cpf):
        if cpf not in self.clientes:
            self.clientes[cpf] = Cliente(nome, cpf)
            self.salvar_dados()

    def criar_conta(self, cpf):
        numero = len(self.contas) + 1
        conta = Conta(numero, self.clientes[cpf])
        self.contas[numero] = conta
        self.salvar_dados()
        return conta

    def salvar_dados(self):
        with open(self.arquivo, "w") as f:
            json.dump(self.serializar(), f, indent=4)

    def carregar_dados(self):
        try:
            with open(self.arquivo, "r") as f:
                dados = json.load(f)
        except FileNotFoundError:
            return

        for cpf, cliente in dados["clientes"].items():
            self.clientes[cpf] = Cliente(cliente["nome"], cpf)

        for numero, conta in dados["contas"].items():
            c = Conta(int(numero), self.clientes[conta["cpf"]])
            c.saldo = conta["saldo"]
            c.extrato = conta["extrato"]
            c.numero_saques = conta["numero_saques"]
            self.contas[int(numero)] = c

    def serializar(self):
        return {
            "clientes": {
                cpf: {"nome": c.nome} for cpf, c in self.clientes.items()
            },
            "contas": {
                numero: {
                    "cpf": conta.cliente.cpf,
                    "saldo": conta.saldo,
                    "extrato": conta.extrato,
                    "numero_saques": conta.numero_saques
                } for numero, conta in self.contas.items()
            }
        }
        if valor > self.LIMITE_SAQUE:
            return "Valor excede o limite por saque."
        if valor > self.saldo:
            return "Saldo insuficiente."
        if valor > 0:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            self.numero_saques += 1
            return True
        return "Valor inválido."
    def gerar_extrato(self):
        return self.extrato, self.saldo
    