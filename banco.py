# forma de adicionar strings em mais de uma linha
menu = """ 
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
=> """

saldo = 0
limite = 500
extrato = ""   #esse valor e uma string
numero_saques = 0
LIMITE_SAQUES = 3 #Essa e uma constante o valor nao ira ser alterado

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor #A cada interação adicione uma soma do saldo com o valor
            extrato += f"Depósito: R$ {valor:.2f}\n" # Concatena (unir) uma nova string a variavel extrato
        
        else:
            print("A operação falhou! \n O valor informado é inválido.")
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if valor > 0:
            if numero_saques >= LIMITE_SAQUES:
                print("Você excedeu o limite de saques, tente mais tarde.")
            elif valor > saldo:
                print("Saldo insuficiente para realizar o saque.")
            else:
                saldo -= valor #A cada interação adicione uma subtração do saldo com o valor
                extrato += f"Saque: R$ {valor:.2f}\n" # Concatena (unir) uma nova string a variavel extrato
                numero_saques += 1 # Adiciona uma interaçao a cada saque
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("A operação falhou! \n O valor informado é inválido.")

    elif opcao == "e":
        print("\n========= Extrato =========")
        print("Não foram realizadas movimentações." if not extrato else extrato) # IF ternario, eliminando a estrutura IF
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==============================")

    # Opção de sair    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")