class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
    def __repr__(self):
        return f"Cliente(nome={self.nome}, cpf={self.cpf})"
    