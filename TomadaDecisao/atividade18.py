data = input('digite uma data :')
dia = data[:2]
mes = data[3] + data[4]
ano = data[6] + data[7] + data[8] + data[9]
d = ['0', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18',
     '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
m = ['01', '02', '03', '04', '05', '06', '08', '09', '10', '11', '12']
a = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def validar_dia():
    if dia in d:
        print('dia:', dia, ' validado')
    else:
        print(' dia não valido')


def validar_mes():
    if mes in m:
        print('mes:', mes, ' valido')
    else:
        print('mes não valido')


def validar_ano():
    if ano != '0000':
        print('ano:', ano, ' valido')
    else:
        print("ano invalido")


if dia not in d or mes not in m:
    print('verifique as informações e digite a data com o formato correto')
elif data[2] == "/" and data[5] == '/':
    validar_dia()
    validar_mes()
    validar_ano()
    print('a data digitada foi :', data)