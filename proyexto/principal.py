"""
Farmacia
"""
import numeros


def datos():
    """

    :return:
    """
    nombre = input("Escriba su nombre: ")
    cedula = input("Escriba su cedula: ")
    return nombre, cedula


nombre, cedula = datos()

NOMBREFARMACIA = "Buena Vista"


def saludo():
    """

    :return:
    """
    print(f"Hola bienvenido sr: {nombre} cc: {cedula} a la Farmacia {NOMBREFARMACIA}")
    print("""
    ----Menu----
    turnos
    [1]-Perfume
    [2]-Farmacia
    [3]-cosmetica
    [4]-Salir
    """)


def menu():
    """

    :return:
    """
    inicio = False
    while not inicio:
        saludo()
        try:
            numero = int(input("Qué área quieres: "))
            if 1 <= numero <= 4:
                if numero == 1:
                    print(f"Tu turno para la perfumes  es : {next(numeros.turnoPerfumes)}")
                    interinio = False
                    while not interinio:
                        confirmar = input("Quieres sacar otro turno para perfumes\n[SI]\n[NO]: ").upper()
                        if confirmar == "SI":
                            print(f"Tu turno para la perfumes  es : {next(numeros.turnoPerfumes)}")
                        elif confirmar == "NO":
                            interinio = True
                        else:
                            print("----ERROR: Debes ingresar SI o NO-----")
                elif numero == 2:
                    print(f"Tu turno para la perfumes  es : {next(numeros.turnofarmacia)}")
                    interinio = False
                    while not interinio:
                        confirmar = input("Quieres sacar otro turno para Farmacia\n[SI]\n[NO]: ").upper()
                        if confirmar == "SI":
                            print(f"Tu turno para la Farmacia  es : {next(numeros.turnofarmacia)}")
                        elif confirmar == "NO":
                            interinio = True
                        else:
                            print("----ERROR: Debes ingresar SI o NO-----")
                elif numero == 3:
                    print(f"Tu turno para la perfumes  es : {next(numeros.turnocosmeticos)}")
                    interinio = False
                    while not interinio:
                        confirmar = input("Quieres sacar otro turno para Cosmetios\n[SI]\n[NO]: ").upper()
                        if confirmar == "SI":
                            print(f"Tu turno para la Farmacia  es : {next(numeros.turnocosmeticos)}")
                        elif confirmar == "NO":
                            interinio = True
                        else:
                            print("----ERROR: Debes ingresar SI o NO-----")
                elif numero == 4:
                    inicio = True




            else:
                print("""--------------ERROR: Debes ingresar un numero del 1 al 4-----------------------
            """)
        except ValueError:
            print("""--------------ERROR: Debes ingresar un numero del 1 al 4-----------------------
            """)


menu()
