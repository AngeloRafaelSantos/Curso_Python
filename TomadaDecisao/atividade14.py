a = int(input("Insira o primeiro número: "))
b = int(input("Insira o segundo número: "))
c = int(input("Insira o terceiro número:"))

if (a < b and a < c):  # testa se 'a' para verificar se é o menor dentre os números.

    if (b < c):  # Se 'a for o menor, então testa-se 'b' para verficar se é o menor.
        print(a, b, c)
    else:  # Se o teste de 'b' falhar, então 'c' e menor que 'b'.
        print(a, c, b)

elif (b < a and b < c):  # Se falhar o teste 'a', então testa-se 'b' para verificar se é o menor.

    if (a < c):  # Se 'b' for o menor, então testa-se 'a' para verificar se é o menor.
        print(b, a, c)
    else:  # Se o teste de 'a' falhar, então 'c' é menor que 'a'
        print(b, c, a)

else:  # Se todos os testes falharem quer dizer que c é o menor.
    if (a < b):  # Sendo 'c' o menor, testa-se 'a' para verificar se é menor que 'b'.
        print(c, a, b)
    else:  # Se o teste de 'a' falhar, então 'b' é menor que 'a
        print(c, b, a)