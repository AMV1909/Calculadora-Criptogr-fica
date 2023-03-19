import random
import string
from math import gcd, ceil
from modules import is_prime, inv


def _11():
    print("1.1 alcular Módulo De Dos Números a mod n = b")

    a = int(input("\nIngrese un valor para a: "))
    n = int(input("Ingrese un valor para n: "))

    b = a % n

    print("\nEl resultado de", a, "mod", n, "es", b)

    print("\nIngrese cualquier tecla para continuar...")
    input()


def _12():
    print("1.2 Calcular Inverso Aditivo")

    a = int(input("\nIngrese un valor para a: "))
    b = int(input("Ingrese un valor para b: "))

    # Calcular inverso aditivo
    c = -a % b

    print("\nEl inverso aditivo de", a, "mod", b, "es", c)

    print("\nIngrese cualquier tecla para continuar...")
    input()


def _13():
    print("1.3 Calcular Inverso De XOR")

    a = int(input("\nIngrese un valor para a: "))
    b = int(input("Ingrese un valor para b: "))

    # Calcular inverso de XOR
    a_binary = bin(a)[2:]
    b_binary = bin(b)[2:]

    # Verificar que los números tengan la misma cantidad de bits
    if (len(a_binary) > len(b_binary)):
        b_binary = b_binary.zfill(len(a_binary))
    elif (len(a_binary) < len(b_binary)):
        a_binary = a_binary.zfill(len(b_binary))

    # Calcular inverso de XOR
    c_binary = ""

    for i in range(len(a_binary)):
        if (a_binary[i] == b_binary[i]):
            c_binary += "0"
        else:
            c_binary += "1"

    print("\n" + a_binary)
    print(b_binary)
    print("-" * len(a_binary))
    print(c_binary)

    c = int(c_binary, 2)

    print("\nEl inverso de XOR de", a, "y", b, "es", c)

    print("\nIngrese cualquier tecla para continuar...")
    input()


def _14():
    print("1.4 Calcular Máximo Común Divisor (MCD) e Indicar Si Existe Inverso Multiplicativo")

    a = int(input("\nIngrese un valor para a: "))
    b = int(input("Ingrese un valor para b: "))

    # Calcular MCD
    mcd = gcd(a, b)

    # Verificar si existe inverso multiplicativo
    if (mcd == 1):
        print("\nExiste inverso multiplicativo")
    else:
        print("\nNo existe inverso multiplicativo")

    print("El MCD de", a, "y", b, "es", mcd)

    print("\nIngrese cualquier tecla para continuar...")
    input()


def _15():
    print("1.5 Calcular Inverso Multiplicativo Por Método Tradicional")

    a = int(input("\nIngrese un valor para a: "))
    b = int(input("Ingrese un valor para b: "))

    # Calcular inverso multiplicativo
    c = 0

    for i in range(1, b):
        if ((a * i) % b == 1):
            c = i
            break

    # Verificar si existe inverso multiplicativo
    if (c == 0):
        print("\nNo existe inverso multiplicativo")
    else:
        print("\nEl inverso multiplicativo de", a, "mod", b, "es", c)

    print("\nIngrese cualquier tecla para continuar...")
    input()


def _16():
    print("1.6 Calcular Inverso Multiplicativo Aplicando Algoritmo Extendido de Euclides AEE, Indicando Rondas y Mostrar Tabla")

    a = int(input("\nIngrese un valor para a: "))
    b = int(input("Ingrese un valor para b: "))

    # Verificar si existe inverso multiplicativo
    if (gcd(a, b) != 1):
        print("\nNo existe inverso multiplicativo")
        print("\nIngrese cualquier tecla para continuar...")
        input()
        return

    # Definir variables
    count = 0
    i = []
    yi = []
    gi = []
    ui = []
    vi = []

    # Concatenar valores iniciales a las listas
    i.append(0)
    i.append(1)

    gi.append(b)
    gi.append(a)

    ui.append(1)
    ui.append(0)

    vi.append(0)
    vi.append(1)

    # Imprimir encabezado de la tabla
    print("i     yi     gi     ui     vi")
    print(str(i[-2]) + "     -     " + str(gi[-2]) +
          "     " + str(ui[-2]) + "     " + str(vi[-2]))
    print(str(i[-1]) + "     -     " + str(gi[-1]) +
          "     " + str(ui[-1]) + "     " + str(vi[-1]))

    # Calcular inverso multiplicativo
    while (gi[-1] != 0):
        count = count + 1
        i.append(len(i))

        yi.append(gi[-2] // gi[-1])
        gi.append(gi[-2] % gi[-1])

        ui.append(ui[-2] - yi[-1] * ui[-1])
        vi.append(vi[-2] - yi[-1] * vi[-1])

        print(str(i[-1]) + "     " + str(yi[-1]) + "     " +
              str(gi[-1]) + "     " + str(ui[-1]) + "     " + str(vi[-1]))

    print("Cantidad de rondas: " + str(count))
    print("El inverso es " + str(vi[-2] + vi[-1]))

    print("\nIngrese cualquier tecla para continuar...")
    input()


def _21():
    print("2.1 Cifrado Módulo 27")

    message = input("\nIngrese el mensaje a cifrar: ")
    displacement = int(input("Ingrese el desplazamiento: "))

    # Definir alfabeto 27 más espacio
    ALPHABET = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ "
    alphabet = "abcdefghijklmnñopqrstuvwxyz "

    cipher = ""

    # Cifrar mensaje
    for letter in message:
        if (letter in ALPHABET):
            cipher += ALPHABET[(ALPHABET.index(letter) +
                                displacement) % len(ALPHABET)]
        elif (letter in alphabet):
            cipher += alphabet[(alphabet.index(letter) +
                                displacement) % len(alphabet)]
        else:
            cipher += letter

    # Descifrar mensaje
    decipher = ""

    for letter in cipher:
        if (letter in ALPHABET):
            decipher += ALPHABET[(ALPHABET.index(letter) -
                                  displacement) % len(ALPHABET)]
        elif (letter in alphabet):
            decipher += alphabet[(alphabet.index(letter) -
                                  displacement) % len(alphabet)]
        else:
            decipher += letter

    # Imprimir valores
    print("\nMensaje a cifrar:", message)
    print("Mensaje cifrado:", cipher)
    print("Mensaje descifrado:", decipher)

    print("\nIngrese cualquier tecla para continuar...")
    input()


def _22():
    print("2.2 Cifrado César")

    message = input("\nIngrese el mensaje a cifrar: ")
    displacement = int(input("Ingrese el desplazamiento: "))

    # Definir alfabeto 26 más espacio
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    alphabet = "abcdefghijklmnopqrstuvwxyz "

    cipher = ""

    # Cifrar mensaje
    for letter in message:
        if (letter in ALPHABET):
            cipher += ALPHABET[(ALPHABET.index(letter) +
                                displacement) % len(ALPHABET)]
        elif (letter in alphabet):
            cipher += alphabet[(alphabet.index(letter) +
                                displacement) % len(alphabet)]
        else:
            cipher += letter

    # Descifrar mensaje
    decipher = ""

    for letter in cipher:
        if (letter in ALPHABET):
            decipher += ALPHABET[(ALPHABET.index(letter) -
                                  displacement) % len(ALPHABET)]
        elif (letter in alphabet):
            decipher += alphabet[(alphabet.index(letter) -
                                  displacement) % len(alphabet)]
        else:
            decipher += letter

    # Imprimir valores
    print("\nMensaje a cifrar:", message)
    print("Mensaje cifrado:", cipher)
    print("Mensaje descifrado:", decipher)

    print("\nIngrese cualquier tecla para continuar...")
    input()


def _23():
    print("2.3 Cifrado Vernam")

    message = input("\nIngrese el mensaje a cifrar: ")

    # Mensaje en bytes
    message_bytes = message.encode("utf-8")

    # Generar llave aleatoria de tamaño del mensaje
    key_bytes = bytes([random.randint(0, 255)
                      for _ in range(len(message_bytes))])
    key_text = str(key_bytes)[2:-1]

    # Cifrar mensaje
    cipher_bytes = bytes([message_bytes[i] ^ key_bytes[i]
                         for i in range(len(message_bytes))])
    cipher_text = str(cipher_bytes)[2:-1]

    # Descifrar mensaje
    decipher_bytes = bytes([cipher_bytes[i] ^ key_bytes[i]
                           for i in range(len(cipher_bytes))])
    decipher_text = str(decipher_bytes)[2:-1]

    # Imprimir mensaje cifrado y llave
    print("\nMensaje a cifrar:", message)
    print("Mensaje cifrado:", cipher_text)
    print("Llave:", key_text)
    print("Mensaje descifrado:", decipher_text)

    print("\nIngrese cualquier tecla para continuar...")
    input()


def _24():
    print("2.4 Cifrado ATBASH")

    message = input("\nIngrese el mensaje a cifrar: ")

    # Definir alfabeto 26 más espacio
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    cipher = ""

    # Cifrar mensaje
    for letter in message:
        if (letter in ALPHABET):
            cipher += ALPHABET[len(ALPHABET) - 1 - ALPHABET.index(letter)]
        elif (letter in alphabet):
            cipher += alphabet[len(alphabet) - 1 - alphabet.index(letter)]
        else:
            cipher += letter

    # Descifrar mensaje
    decipher = ""

    for letter in cipher:
        if (letter in ALPHABET):
            decipher += ALPHABET[len(ALPHABET) - 1 - ALPHABET.index(letter)]
        elif (letter in alphabet):
            decipher += alphabet[len(alphabet) - 1 - alphabet.index(letter)]
        else:
            decipher += letter

    # Imprimir valores
    print("\nMensaje a cifrar:", message)
    print("Mensaje cifrado:", cipher)
    print("Mensaje descifrado:", decipher)

    print("\nIngrese cualquier tecla para continuar...")
    input()


def _25():
    print("2.5 Cifrado De Transposición Columnar Simple")

    message = input("Ingrese el mensaje a cifrar: ")
    key = int(input("Ingrese la llave (0 < key < len(message)): "))

    # Filas de la matriz
    rows = ceil(len(message) / key)

    # Matriz que contendrá el mensaje
    matrix = [[" " for _ in range(key)] for _ in range(rows)]

    # Índice del mensaje
    k = 0

    # Llenar matriz
    for i in range(rows):
        for j in range(key):
            if (k < len(message)):
                matrix[i][j] = message[k]
                k += 1
            
    # Imprimir mensaje
    print("\nMensaje:")
    for i in range(rows):
        row_matrix = "["
        for j in range(key):
            row_matrix += "\'" + matrix[i][j] + "\'"
            if (j < key - 1):
                row_matrix += ", "
        print(row_matrix + "]")

    # Cifrar mensaje
    cipher = ""

    for i in range(key):
        for j in range(rows):
            cipher += matrix[j][i]

    # Imprimir mensaje cifrado
    print("\nMensaje cifrado:")
    for i in range(key):
        row_matrix = "["
        for j in range(rows):
            row_matrix += "\'" + matrix[j][i] + "\'"
            if (j < rows - 1):
                row_matrix += ", "
        print(row_matrix + "]")

    # Descifrar mensaje
    decipher = ""

    for i in range(rows):
        for j in range(key):
            decipher += matrix[i][j]

    # Imprimir mensaje descifrado
    print("\nMensaje descifrado:")
    for i in range(rows):
        row_matrix = "["
        for j in range(key):
            row_matrix += "\'" + matrix[i][j] + "\'"
            if (j < key - 1):
                row_matrix += ", "
        print(row_matrix + "]")

    # Imprimir valores
    print("\nMensaje a cifrar:", message)
    print("Mensaje cifrado:", cipher)
    print("Mensaje descifrado:", decipher)

    print("\nIngrese cualquier tecla para continuar...")
    input()


def _26():
    print("2.6 Cifrado Afín")

    message = input("\nIngrese el mensaje a cifrar: ")

    # Verificar que a y b sean primos entre sí y que estén en el rango [0, 26]
    while (True):
        while (True):
            a = int(input("Ingrese el valor de a para la llave (Debe ser primo con 26): "))
            if (a < 0 or a > 26):
                print("Valor de a fuera de rango")
            else:
                break
        
        while (True):
            b = int(input("Ingrese el valor de b para la llave: "))
            if (b < 0 or b > 26):
                print("Valor de b fuera de rango")
            else:
                break

        if (gcd(a, b) != 1):
            print("a y b no son primos entre sí")
        else:
            break

    # Llave
    key = (a, b)

    # Cifrar mensaje
    cipher = ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26) + ord('A')) for t in message.upper().replace(' ', '') ])

    # Descifrar mensaje
    decipher = ''.join([ chr((( inv(key[0], 26)*(ord(c) - ord('A') - key[1])) % 26) + ord('A')) for c in cipher ])

    # Imprimir valores
    print("\nMensaje a cifrar:", message)
    print("Mensaje cifrado:", cipher)
    print("Llave:", key)
    print("Mensaje descifrado:", decipher)

    print("\nIngrese cualquier tecla para continuar...")
    input()


def _27():
    print("2.7 Cifrado De Sustitución Simple")

    message = input("\nIngrese el mensaje a cifrar: ")

    # Alfabeto original
    ALPHABET = string.ascii_uppercase
    alphabet = string.ascii_lowercase

    # Generar clave aleatoria
    substitution = list(alphabet)
    random.shuffle(substitution)
    substitution = ''.join(substitution)

    # Cifrar mensaje
    cipher = ""

    for letter in message:
        if (letter in ALPHABET):
            index = ALPHABET.index(letter)
            cipher += ALPHABET[index]
        elif (letter in alphabet):
            index = alphabet.index(letter)
            cipher += substitution[index]
        else:
            cipher += letter

    # Descifrar mensaje
    decipher = ""

    for letter in cipher:
        if (letter in ALPHABET):
            index = ALPHABET.index(letter)
            decipher += ALPHABET[index]
        elif (letter in alphabet):
            index = substitution.index(letter)
            decipher += alphabet[index]
        else:
            decipher += letter

    # Imprimir valores
    print("\nMensaje a cifrar:", message)
    print("Mensaje cifrado:", cipher)
    print("Llave:", substitution)
    print("Mensaje descifrado:", decipher)

    print("\nIngrese cualquier tecla para continuar...")
    input()


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
    A = (alpha ** a) % p
    B = (alpha ** b) % p

    # Calculo de claves compartidas
    s_A = (B ** a) % p
    s_B = (A ** b) % p

    # Verificación de claves compartidas
    if (s_A != s_B):
        print("Error en el cálculo de las claves compartidas")
        exit()

    # Imprimir todos los valores
    print("\nNúmero primo p:", p)
    print("Generador α:", alpha)
    print("Clave privada a:", a)
    print("Clave privada b:", b)
    print("Clave pública A:", A)
    print("Clave pública B:", B)
    print("Clave compartida:", s_A)

    print("\nIngrese cualquier tecla para continuar...")
    input()


def _32():
    print("3.2 Calcular RSA")

    while (True):
        # Número primo p
        p = int(input("\nIngrese un número primo p: "))

        # Verificar si es primo
        if (is_prime(p)):
            break
        else:
            print(p, "no es un número primo")

    while (True):
        # Número primo q
        q = int(input("\nIngrese un número primo q: "))

        # Verificar q > p
        if (q > p):
            # Verificar si es primo
            if (is_prime(q)):
                break
            else:
                print(q, "no es un número primo")
        else:
            print("q debe ser mayor que p")

    # Valor público n
    n = p * q

    # Calcular indicador de Euler
    phi = (p - 1) * (q - 1)

    # Generar e
    while (True):
        e = random.randint(1, phi)

        # Verificar que e sea coprimo con phi
        if gcd(e, phi) == 1:
            break

    # Calcular d
    d = pow(e, -1, phi)

    # Mensaje a cifrar int de 64 bits
    m = input("\nIngrese el mensaje a cifrar: ")

    if (m.isdigit()):
        m = int(m)

        # Cifrar mensaje
        c = pow(m, e, n)

        # Descifrar mensaje
        m2 = pow(c, d, n)
    else:
        # Cifrar mensaje
        c = [pow(ord(char), e, n) for char in m]

        # Descifrar mensaje
        m2 = ''.join([chr(pow(char, d, n)) for char in c])

    # Verificar que el mensaje descifrado sea igual al original
    if (m != m2):
        print("Error en el descifrado")
        print("Escoja unos valores más alejados para p y q")
        exit()

    else:
        # Imprimir todos los valores
        print("\nNúmero primo p: ", p)
        print("Número primo q: ", q)
        print("Valor público n: ", n)
        print("Indicador de Euler: ", phi)
        print("Valor público e: ", e)
        print("Valor privado d: ", d)
        print("Mensaje a cifrar: ", m)
        print("Mensaje cifrado: ", c)
        print("Mensaje descifrado: ", m2)

    print("\nIngrese cualquier tecla para continuar...")
    input()


def _33():
    print("3.3 Calcular Algoritmo De Exponenciación Rápida")

    # Base
    b = int(input("\nIngrese la base: "))

    # Exponente
    e = int(input("Ingrese el exponente: "))

    # Módulo
    m = int(input("Ingrese el módulo: "))

    # Convertir exponente a binario
    e = bin(e)[2:]

    # Valores para mostrar en pantalla
    x = 1
    x_aux = 1
    i = 0
    c = len(e) - 1

    print("")

    while i < len(e):
        if e[i] == '1':
            x = ((x ** 2) * b) % m
            print("b" + str(c) + " = " + e[i] + " -> x = " + str(
                x_aux) + "² * " + str(b) + " mod " + str(m) + " = " + str(x))
            x_aux = x
        else:
            x = (x ** 2) % m
            print("b" + str(c) + " = " + e[i] + " -> x = " +
                  str(x_aux) + "² mod " + str(m) + " = " + str(x))
            x_aux = x
        i += 1
        c -= 1

    # Imprimir resultado
    print("\nResultado:", x)

    print("\nIngrese cualquier tecla para continuar...")
    input()
