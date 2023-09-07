import os

menu = """\n
================ MENU ================
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == 'd':
        os.system('cls')
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            os.system('cls')
            print('Operação falhou! O valor informado é inválido.')
    elif opcao == "s":
        os.system('cls')
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            os.system('cls')
            print('Operação falhou! Você não tem saldo sufuciente.')
        elif excedeu_limite:
            os.system('cls')
            print('Operação falhou! O valor do saque excede o limite.')
        elif excedeu_saques:
            os.system('cls')
            print('Operação falhou! Número máximo de saques excedido.')
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
        else:
            os.system('cls')
            print('Operação falhou! Valor informado é inválido.')
    elif opcao == 'e':
        os.system('cls')
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================\n")
    elif opcao == 'q':
        os.system('cls')
        print('Saindo do porgrama...')
        break
    else:
        os.system('cls')
        print("Operação inválida, por favor selecione novamente a operação desejada.")