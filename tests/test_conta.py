from models.cliente import Cliente
from models.conta import Conta

def test_deposito():
    cliente = Cliente("Maria", "111")
    conta = Conta(1, cliente)
    assert conta.depositar(100) is True
    assert conta.saldo == 100

def test_saque_sem_saldo():
    cliente = Cliente("Ana", "222")
    conta = Conta(2, cliente)
    assert conta.sacar(50) == "Saldo insuficiente."
    assert conta.saldo == 0