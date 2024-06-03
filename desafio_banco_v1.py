menu = """
[d] Deposito
[s] Saque
[e] Estrato
[q] Sair

=>"""
saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True: #Loop infinito até que se digite 'q' para sair(Break)
    opcao = input(menu)
    if opcao =='d':
        print("Depósito")
        valor = float(input("Informe o valor de DEPÓSITO:"))
        if valor > 0:
            saldo += valor
            extrato = f'Deposito: R$ {valor:.2f}\n'
            # print(extrato)
        else:
            print("Valor inválido.")
    elif opcao =='s':
        print("Saque!")
        valor = float(input("Informe o valor de SAQUE:"))
        excedeu_saldo = valor > saldo
        #print(excedeu_limite)
        excedeu_limite = valor > limite
        excedeu_saques = numero_saque >= LIMITE_SAQUE
        #checar se excedeu algo(saldo, limite ou limite diário)
        if excedeu_saldo:
            print("Saldo insuficiente!")
        elif excedeu_limite:
            print("Limite insuficiente!")
        elif excedeu_saques:
            print("Limite de saque diário atingido!")
        elif valor > 0:
            saldo -=valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1
        else:
            print("Valor informado incorreto.")
        
    elif opcao == 'e':
        print("Extrato")
        print("\n=-=-=-=-=- EXTRADO -=-=-=-=-=")
        print("Sem movimentação." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    elif opcao =='q':
        print("Sair")
        break
    else:
        print("Opção Inválida, tente novamete.")
