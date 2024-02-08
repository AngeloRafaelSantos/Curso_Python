num = int(input("digite o numero a qual deseja iniciar o intervalo: "))
num2 = int(input("digite o numero a qual deseja finalizar o intervalo: "))
num3 = int(input("digite o primeiro numero a qual deseja ignorar: " ))
num4 = int(input("digite o segundo numero a qual deseja ignorar: " ))
num5 = int(input("digite o terceiro numero a qual deseja ignorar: " ))
for i in range(num, num2, 1):
    if(i==num3):
        continue
    if (i == num4):
        continue
    elif (i == num5):
        continue
    print(i)