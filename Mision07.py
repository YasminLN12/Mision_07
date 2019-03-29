#Autor: Yasmín Landaverde Nava
#Descripción:


def probarDivisiones():
    dividendo = int(input("Teclea el dividendo: "))
    divisor = int(input("Teclea el divisor: "))
    cociente = 0
    divisorO = divisor
    residuo=dividendo
    if divisor <= dividendo:
        while divisor <= dividendo:
            cociente += 1
            divisor = divisor + divisorO
            residuo = dividendo - (divisor-divisorO)
    print(dividendo, "/", divisorO, "=", cociente,", sobra", residuo)

def crearLista():
        print("Teclea una serie de números para encontrar el mayor.")
        num = int(input("Teclea un numero[teclea -1 para salir]: "))
        mayor = 0
        if num != -1:
            while num != -1:
                if num > mayor:
                    mayor = num
                num = int(input("Teclea un numero[teclea -1 para salir]: "))
            print("El número mayor es:", mayor)
        else:
            print("No hay valor mayor")


def main():
    print("""Misión 07.Ciclos while
Autor: Yasmín Landaverde Nava
Matrícula: A01745725

Elige una opción a ejecutar
1. Calcular divisiones
2. Encontrar el mayor
3. Salir""")

    opcion = int(input("Elige tu opción: "))
    while opcion != 3:
        if opcion == 1:
            probarDivisiones()

            print("""Misión 07.Ciclos while
Autor: Yasmín Landaverde Nava
Matrícula: A01745725

Elige una opción a ejecutar
1. Calcular divisiones.
2. Encontrar el mayor
3. Salir""")
            opcion = int(input("¿Qué desea hacer?: "))

        elif opcion == 2:
            crearLista()
            print("""Misión 07.Ciclos while
Autor: Yasmín Landaverde Nava
Matrícula: A01745725

Elige una opción a ejecutar
1. Calcular divisiones.
2. Encontrar el mayor
3. Salir""" '\n')
            opcion = int(input("¿Qué desea hacer?: "))

    print("RRegresa pronto")


main()