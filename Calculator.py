from os import system
from Functions import _11, _12, _13, _14, _15, _16, _21, _22, _23, _24, _25, _26, _27, _31, _32, _33

while (True):
    system("cls")

    print("***********MENU*****************\n"
          + "*********************************\n"
          + "1. Operaciones Matemáticas Modulares\n"
          + "2. Criptografía Clásica\n"
          + "3. Criptografía Moderna\n"
          + "4. Salir\n"
          + "*********************************")

    option = int(input())
    system("cls")

    if option == 1:
        while (True):
            system("cls")

            print("+++++++++++++++SUBMENU MATEMATICA MODULAR +++++++++++++++++++\n"
                  + "1.1 Calcular Módulo De Dos Números a mod n = b\n"
                  + "1.2 Calcular Inverso Aditivo\n"
                  + "1.3 Calcular Inverso De XOR\n"
                  + "1.4 Calcular Máximo Común Divisor (MCD) e Indicar Si Existe Inverso Multiplicativo\n"
                  + "1.5 Calcular Inverso Multiplicativo Por Método Tradicional\n"
                  + "1.6 Calcular Inverso Multiplicativo Aplicando Algoritmo Extendido de Euclides AEE, Indicando Rondas y Mostrar Tabla\n"
                  + "1.7 Atrás\n"
                  + "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

            option = int(input())
            system("cls")

            if option == 1:
                _11()

            elif option == 2:
                _12()

            elif option == 3:
                _13()

            elif option == 4:
                _14()

            elif option == 5:
                _15()

            elif option == 6:
                _16()

            elif option == 7:
                break

            else:
                print("Opción inválida\n"
                      + "Presione cualquier tecla para continuar")

                input()

    elif option == 2:
        while (True):
            system("cls")

            print("+++++++++++++CRIPTOGRAFIA CLASICA ++++++++++++++++++\n"
                  + "++++++++++++++++++++++++++++++++++++++++++++++++++\n"
                  + "2.1 Cifrado Módulo 27\n"
                  + "2.2 Cifrado César\n"
                  + "2.3 Cifrado Vernam\n"
                  + "2.4 Cifrado ATBASH\n"
                  + "2.5 Cifrado De Transposición Columnar Simple\n"
                  + "2.6 Cifrado Afín\n"
                  + "2.7 Cifrado De Sustitución Simple\n"
                  + "2.8 Atrás\n"
                  + "++++++++++++++++++++++++++++++++++++++++++++++++++++")

            option = int(input())
            system("cls")

            if option == 1:
                _21()

            elif option == 2:
                _22()

            elif option == 3:
                _23()

            elif option == 4:
                _24()

            elif option == 5:
                _25()

            elif option == 6:
                _26()

            elif option == 7:
                _27()

            elif option == 8:
                break

            else:
                print("Opción inválida\n"
                      + "Presione cualquier tecla para continuar")

                input()

    elif option == 3:
        while (True):
            system("cls")

            print("+++++++++++++CRIPTOGRAFIA MODERNA++++++++++++++++++\n"
                  + "++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
                  + "3.1 Calcular Diffie Hellman\n"
                  + "3.2 Calcular RSA\n"
                  + "3.3 Calcular Algoritmo De Exponenciación Rápida\n"
                  + "3.4 Atrás\n"
                  + "++++++++++++++++++++++++++++++++++++++++++++++++++++")

            option = int(input())
            system("cls")

            if option == 1:
                _31()

            elif option == 2:
                _32()

            elif option == 3:
                _33()

            elif option == 4:
                break

            else:
                print("Opción inválida\n"
                      + "Presione cualquier tecla para continuar")

                input()

    elif option == 4:
        break

    else:
        print("Opción inválida\n"
              + "Presione cualquier tecla para continuar")

        input()
