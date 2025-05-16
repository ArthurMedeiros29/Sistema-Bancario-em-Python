print("""
[D] Depositar
[S] Sacar
[E] Extrato
[F] Finalizar Operacao
""")

saldo = 0
limite = 500
numero_saques = 0
limite_saques = 3
total_depositado = 0
total_sacado = 0

while True:
    opcao = input("\nEscolha uma das opcoes acima: ").upper()

    if opcao == "D":
        deposito = float(input("Informe o valor que deseja depositar: "))

        if deposito > 0:
            saldo += deposito
            total_depositado += deposito
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == 'S':
        sacar = float(input("Informe o valor que deseja sacar: "))

        if sacar > saldo:
            print("Operacao falhou! Você nao tem saldo suficiente.")
        elif sacar > limite:
            print("Operacao falhou! O valor do saque excede o limite.")
        elif numero_saques >= limite_saques:
            print("Operacao falhou! Numero maximo de saques excedido.")
        elif sacar > 0:
            saldo -= sacar
            total_sacado += sacar
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == "E":
        print("\n=============== EXTRATO ===============")
        print(f"Total depositado: R${total_depositado:.2f}")
        print(f"Total sacado:     R${total_sacado:.2f}")
        print(f"Saldo atual:      R${saldo:.2f}")
        print("=======================================")

    elif opcao == "F":
        print("\nOperacao finalizada. Obrigado pela preferencia!")
        break

    else:
        print("\nOpcao inválida. Por favor selecione corretamente uma das opcoes acima.")