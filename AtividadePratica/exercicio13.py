dias = int(input("insira o numero de dias: "))
horas = int(input("insira o numero de horas: "))
minutos = int(input("insira o numero de minutos: "))
segundos = int(input("insira o numero de segundos: "))
conversao = (dias*86400)+(horas*3600)+(minutos*60)+segundos

print("a conversão de %i dias %i horas %i minutos e %i segundos é igual a %i segundos" %(dias, horas, minutos, segundos, conversao))