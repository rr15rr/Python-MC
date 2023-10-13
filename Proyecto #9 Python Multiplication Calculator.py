print('Elige tu propio camino')
inicio = input("Escribe empezar para iniciar el programa: ")
while (inicio == 'empezar'):
    print(""" Que camino quieres elegir? 
    escribe la opcion con numero
    1 - Quiero que me saludes
    2 - Quiero usar la calculadora de multiplicacion
    3 - Quiero salir del programa """)
    opcion = input()
    if opcion == "1":
        print("Te saludo :)")
    elif opcion == "2":
        numero1 = float(input("Introduce el valor a multiplicar primero: "))
        numero2 = float(input("Introduce el valor a multiplicar segundo: "))
        print("El resultado es ", numero1*numero2)
    elif opcion == '3':
            print("Goodbye")
            break 
    else: 
            print("Elige una opcion permitida")