i=0
x=0
y=0
for i in range(0, 100, 1):
    if(i%2==1):
        continue
    print(i)
    x = i+i
    y +=1
print("a soma dos pares encontrados na lista é de", x)
print("existe no total de %i numeros pares na lista"%y)