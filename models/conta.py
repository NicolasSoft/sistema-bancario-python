class Conta:
    LIMITE_SAQUE = 500
    LIMITE_DIARIO = 3

    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0
        self.extrato = []
        self.numero_saques = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            return True
        return False

    def sacar(self, valor):
        if self.numero_saques >= self.LIMITE_DIARIO:
            return "Limite diário de saques excedido."

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
class Conta:
    LIMITE_SAQUE = 500
    LIMITE_DIARIO = 3

    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0
        self.extrato = []
        self.numero_saques = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            return True
        return False

    def sacar(self, valor):
        if self.numero_saques >= self.LIMITE_DIARIO:
            return "Limite diário de saques excedido."

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
