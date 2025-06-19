menu = """
    [d] depositar
    [s] sacar
    [e] extrato
    [q] sair
    Digite a opção desejada: """

saldo = 0
extrato = ""
limite = 500
numero_saques = 0

LIMITE_SAQUES = 3


def depositar_valor(valor):
    global saldo, extrato
    if valor > 0:
        if valor > limite:
            print(
                f"Operação falhou! O valor máximo para depósito diario é R$ {limite:.2f}.")
            return
        if saldo + valor > limite:
            print(
                f"Operação falhou! O saldo máximo permitido é para sua conta e R$ {limite:.2f}.")
            return
        # Verifica se o valor é positivo
        if valor <= 0:
            print(
                "Operação falhou! O valor informado é inválido. Verique e tente novamente.")
            return
        # Realiza o depósito
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

        print("Depósito realizado com sucesso !")
    else:
        print("Operação falhou! O valor informado é inválido. Verifique e tente novamente.")


def sacar_dinheiro(valor):
    global saldo, extrato, numero_saques
    if valor > 0:
        if valor > limite:
            print(
                f"Operação falhou! O valor máximo para saque é R$ {limite:.2f}.")
            return
        if saldo < valor:
            print("Operação falhou! Saldo insuficiente.")
            return
        if numero_saques >= LIMITE_SAQUES:
            print(
                f"Operação falhou! Número máximo de saques diários é {LIMITE_SAQUES}.")
            return
        # Realizar o saque
        saldo -= valor
        # armazena a operacao no extrato
        extrato += f"Saque: R$ {valor:.2f}\n"
        # Incrementa o número de saques
        numero_saques += 1
        print("saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")


def exibir_extrato():
    global extrato, saldo
    if extrato == "":
        print("Conta sem movimentacoes!")
    else:
        print(extrato)
    print(f"Saldo: R$ {saldo:.2f}\n")


while True:
    opcao = input(menu.upper()).upper()

    if opcao == "D":
        valor_deposito = float(input("Informe o valor do depósito: R$ "))
        depositar_valor(valor_deposito)
    elif opcao == "S":
        valor_saque = float(input("Informe o valor do saque: R$ "))
        sacar_dinheiro(valor_saque)
    elif opcao == "E":
        exibir_extrato()
    elif opcao == "Q":
        print("Saindo...")
        break
