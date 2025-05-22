from datetime import datetime

saldo = 0
limite = 500
numero_saques = 0
limite_saques = 3
limite_transacoes = 10

total_depositado = 0
total_sacado = 0
transacoes = []

while True:
    if len(transacoes) >= limite_transacoes:
        print("Limite de 10 transacoes diarias atingido. AS operacoes estao bloqueadas")
        break

    print("""
    [D] Depositar
    [S] Sacar
    [E] Extrato
    [F] Finalizar Operacao
    """)
    opcao = input("Escolha uma das opcoes acima: ").upper()

    if opcao == "D":
        deposito = float(input("Informe o valor que deseja depositar: "))

        if deposito > 0:
            saldo += deposito
            total_depositado += deposito
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            transacoes.append(("Deposito", deposito, data_hora))
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
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            transacoes.append(("Saque", sacar, data_hora))
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == "E":
        print("\n=============== EXTRATO ===============")
        if transacoes:
            for tipo, valor, data_hora in transacoes:
                print(f"{data_hora} - {tipo}: R${valor:.2f}")
        else:
            print("Não foram realizadas movimentacoes")
        print(f"Total depositado: R${total_depositado:.2f}")
        print(f"Total sacado:     R${total_sacado:.2f}")
        print(f"Saldo atual:      R${saldo:.2f}")
        print("=======================================")

    elif opcao == "F":
        print("\nOperacao finalizada. Obrigado pela preferencia!")
        break

    else:
        print("\nOpcao inválida. Por favor selecione corretamente uma das opcoes acima.")