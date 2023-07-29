print("----------------------------------")

print("SISTEMA BANCÁRIO DO BANCO DO WESLLY")

print("----------------------------------")

print("Seja bem-vindo ao nosso sistema")

saldo = int(3000)

extrato = ["operações realizadas:"]

opção = int(input("para iniciar sua operação, digite 1: "))

while opção == 1:

    print("para prosseguir, escolha sua operação:")

    print("s - saque")
    print("d - depósito")
    print("e - extrato")

    operação = input("operação: ")

    if operação == "s":
        valor_saldo = int(input("Digite o valor do saque: "))

        if valor_saldo <= saldo:
            saldo = saldo - valor_saldo
            saldo_novo_saque = str(saldo)+"-"
            extrato.append(saldo_novo_saque)
            

            print("seu novo saldo é "+ str(saldo))

            opção = int(input("Deseja realizar nova operação? 1 - sim, 2 - não: "))

    if operação == "d":
        valor_deposito = int(input("Digite o valor do depósito: "))
        saldo = saldo + valor_deposito
        saldo_novo_deposito = str(saldo)+"+"
        extrato.append(saldo_novo_deposito)


        print("seu novo saldo é "+ str(saldo))

        opção = int(input("Deseja realizar nova operação? 1 - sim, 2 - não: "))


    if operação == "e":
        print(extrato)

        opção = int(input("Deseja realizar nova operação? 1 - sim, 2 - não: "))

        

        


        
        

        

        
    



