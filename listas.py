from os import system
system('cls')

nombres=[]
apellidos=[]

apellidos.append('soto')
apellidos.append('perez')
apellidos.append(input('ingrese apellido: '))

nombres.append('jose')
nombres.append('mario')
nombres.append('luis')

print(nombres)
print(apellidos)

for i in range(len(nombres)):
    n=i+1
    print(f'persona {n}: {nombres}{apellidos[i]}')