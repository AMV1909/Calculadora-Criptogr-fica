import random
from modules import mod_exp, is_prime, text_to_binary, binary_to_text, max_common_divisor, inverse_multiplicative

def _11():
    print("1.1 Calcular el módulo de dos números a mod n = b")


def _12():
    print("1.2 Calcular inverso aditivo")


def _13():
    print("1.3 Calcular inverso de XOR")


def _14():
    print("1.4 Calcular máximo común divisor (MCD) e indicar si existe el inverso multiplicativo")


def _15():
    print("1.5 Calcular inverso multiplicativo por método tradicional visto en clase")


def _16():
    print("1.6 Calcular el  inverso multiplicativo aplicando el Algoritmo Extendido de Euclides AEE, indicando cuantas rondas, y mostrar tabla*")


def _21():
    print("2.1 cifrado Módulo 27")


def _22():
    print("2.2 cifrado cesar")


def _23():
    print("2.3 cifrado vernam")


def _24():
    print("2.4 cifrado ATBASH")


def _25():
    print("2.5 Cifrador transposición columnar simple")


def _26():
    print("2.6 cifrado afin")


def _27():
    print("2.7 Cifra de Sustitución Simple")


def _31():
    print("3.1 Calcular Diffie Hellman")

    while (True):
        # Número primo p
        p = int(input("\nIngrese un número primo p: "))

        # Verificar si es primo
        if (is_prime(p)):
            break
        else:
            print(p, "no es un número primo")

    while (True):
        # Generador α del primo p
        alpha = int(
            input("\nIngrese un α (generador del primo p) menor que p: "))

        if (alpha < p):
            break
        else:
            print("α debe ser menor que p")

    # Claves privadas aleatorias a y b
    a = int(input("\nIngrese un valor para la clave privada a: "))
    b = int(input("Ingrese un valor para la clave privada b: "))

    # Cáculos de claves públicas
    A = mod_exp(alpha, a, p)
    B = mod_exp(alpha, b, p)

    # Calculo de claves compartidas
    s_A = mod_exp(B, a, p)
    s_B = mod_exp(A, b, p)

    # Verificación de claves compartidas
    if (s_A != s_B):
        print("Error en el cálculo de las claves compartidas")
        exit()

    # Imprimir todos los valores
    print("\nNúmero primo p: ", p)
    print("Generador α: ", alpha)
    print("Clave privada a: ", a)
    print("Clave privada b: ", b)
    print("Clave pública A: ", A)
    print("Clave pública B: ", B)
    print("Clave compartida: ", s_A)

    print("\nIngrese cualquier tecla para continuar...")
    input()

def _32():
    print("3.2 Calcular RSA")

    while(True):
        # Número primo p
        p = int(input("\nIngrese un número primo p: "))

        # Verificar si es primo
        if (is_prime(p)):
            break
        else:
            print(p, "no es un número primo")

    while(True):
        # Número primo q
        q = int(input("\nIngrese un número primo q: "))

        # Verificar si es primo
        if (is_prime(q)):
            break
        else:
            print(q, "no es un número primo")

    # Valor público n
    n = p * q

    # Calcular indicador de Euler
    phi = (p - 1) * (q - 1)

    # Generar e
    while(True):
        e = random.randint(1, phi - 1)

        # Verificar que e y phi sean coprimos
        if (max_common_divisor(e, phi) == 1):
            break
    
    # Calcular d
    d = inverse_multiplicative(e, phi)

    # Mensaje a cifrar
    m = input("\nIngrese el mensaje a cifrar: ")
    print("Mensaje a cifrar: ", m)

    # Convertir mensaje a binario
    m_binary = text_to_binary(m)

    # Convertir binario a entero
    m_int = int(m_binary, 2)

    # Cifrar mensaje
    c = mod_exp(m_int, e, n)

    # Descifrar mensaje
    m_int = mod_exp(c, d, n)

    # Convertir entero a binario
    m_binary = bin(m_int)[2:]

    # Convertir binario a texto
    m_text = binary_to_text(m_binary)

    # Verificar que el mensaje descifrado sea igual al original
    if (m != m_text):
        print("Error en el descifrado")
        exit()

    # Imprimir todos los valores
    print("\nNúmero primo p: ", p)
    print("Número primo q: ", q)
    print("Valor público n: ", n)
    print("Indicador de Euler: ", phi)
    print("Valor público e: ", e)
    print("Valor privado d: ", d)
    print("Mensaje a cifrar: ", m)
    print("Mensaje cifrado: ", c)
    print("Mensaje descifrado: ", m_text)

    print("\nIngrese cualquier tecla para continuar...")
    input()

def _33():
    print("3.3 Calcular Algoritmo de exponenciación rápida")

    # Base
    b = int(input("\nIngrese la base: "))

    # Exponente
    e = int(input("Ingrese el exponente: "))

    # Módulo
    m = int(input("Ingrese el módulo: "))

    # Calcular resultado
    r = mod_exp(b, e, m)

    # Imprimir resultado
    print("\nResultado: ", r)

    print("\nIngrese cualquier tecla para continuar...")
    input()