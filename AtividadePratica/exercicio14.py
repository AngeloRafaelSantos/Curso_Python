compra = float(input("insira o valor da compra: "))
desconto = compra*10/100
total = compra-desconto
print("o valor na compra é de %2.f com "%compra + '10% de desconto' + "o valor total é de %2.f" %total)