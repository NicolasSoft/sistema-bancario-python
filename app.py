from services.banco import Banco

banco = Banco()

while True:
    print("""
    [1] Criar cliente
    [2] Criar conta
    [3] Depositar
    [4] Sacar
    [5] Extrato
    [0] Sair
    """)

    opcao = input("=> ")

    if opcao == "1":
        nome = input("Nome: ")
        cpf = input("CPF: ")
        banco.criar_cliente(nome, cpf)

    elif opcao == "2":
        cpf = input("CPF do cliente: ")
        conta = banco.criar_conta(cpf)
        print(f"Conta criada: {conta.numero}")

    elif opcao == "3":
        numero = int(input("Número da conta: "))
        valor = float(input("Valor: "))
        banco.contas[numero].depositar(valor)
        banco.salvar_dados()

    elif opcao == "4":
        numero = int(input("Número da conta: "))
        valor = float(input("Valor: "))
        print(banco.contas[numero].sacar(valor))
        banco.salvar_dados()

    elif opcao == "5":
        numero = int(input("Número da conta: "))
        extrato, saldo = banco.contas[numero].gerar_extrato()
        print("\n".join(extrato))
        print(f"Saldo: R$ {saldo:.2f}")

    elif opcao == "0":
        break
