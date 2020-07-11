a = input("Digite o tipo de carne, F para filé, A para alcatra e P para picanha!\n")
b = float(input("Digite a quantidade de carne desejada:" ))
c = input("Deseja realizar a compra no cartão de cédito? Se sim, digite S, se não digite N")

if a == 'F' or a == 'f':
    if b > 5:
        valorTotal_Carne = b*5.80 
        if c == 'S' or c == 's':
            valorTotal_Carne = b*5.80 
            valorfinal = (valorTotal_Carne*5)/100
            VALOR = valorTotal_Carne - valorfinal
            print(valorfinal)
            print(VALOR)
        else:
            print(valorTotal_Carne)
    else:
        valorTotal_Carne = b*4.90 
        if c == 'S' or c == 's':
            valorTotal_Carne = b*4.90 
            valorfinal = (valorTotal_Carne*5)/100
            VALOR = valorTotal_Carne - valorfinal
            print(valorfinal)
            print(VALOR)
        else:
            print(valorTotal_Carne)
elif a == 'A' or a == 'a':
    if b > 5:
        valorTotal_Carne = b*6.80
        if c == 'S' or c == 's':
            valorTotal_Carne = b*6.80
            valorfinal = (valorTotal_Carne*5)/100
            VALOR = valorTotal_Carne - valorfinal
            print(valorfinal)
            print(VALOR)
        else:
            print(valorTotal_Carne)
    else:
        valorTotal_Carne = b*5.90
        if c == 'S' or c == 's':
            valorTotal_Carne = b*5.90
            valorfinal = (valorTotal_Carne*5)/100
            VALOR = valorTotal_Carne - valorfinal
            print(valorfinal)
            print(VALOR)
        else:
            print(valorTotal_Carne)
elif a == 'P' or a == 'p':
    if b > 5:
        valorTotal_Carne =  b*7.80
        if c == 'S' or c == 's':
            valorTotal_Carne = b*7.80
            valorfinal = (valorTotal_Carne*5)/100
            VALOR = valorTotal_Carne - valorfinal
            print(valorfinal)
            print(VALOR)
        else:
            print(valorTotal_Carne)
    else:
        valorTotal_Carne: b*6.90
        if c == 'S' or c == 's':
            valorTotal_Carne = b*6.90
            valorfinal = (valorTotal_Carne*5)/100
            VALOR = valorTotal_Carne - valorfinal
            print(valorfinal)
            print(VALOR)
        else:
            print(valorTotal_Carne)


            
