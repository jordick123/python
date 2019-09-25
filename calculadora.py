'''una calculadora para
aprender python'''

from os import system



def sumar(num1,num2):
    print('la suma es',str(num1+num2))

def restar(x,y):
    resta=x-y
    print(f'la resta es {resta}')

def dividir(a,b):
    pass

def multiplicar(a,b):
    pass

def pausa():
    print('presione tecla para continuar')
    input()
    system('cls')

def menu():
    print('''1. sumar
2. restar
3. multiplicar
4. dividir
9. salir''')

system('cls')
while True:
    num1=float(input('ingrese numero 1: '))
    num2=float(input('ingrese numero 2: '))
    menu()
    op=int(input('Ingrese nùmero: '))
    if op==1:
        sumar(num1,num2)
    elif op==2:
        restar(num1,num2)
    elif op==3:
        multiplicar(num1,num2)
    elif op==4:
        dividir(num1,num2)
    elif op==9:
        print('fin del programa')
        pausa()
        break
    else:
        print('opción no válida')
    pausa()