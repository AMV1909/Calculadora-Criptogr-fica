# Verifica si un número es primo o no
def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
        else:
            return True
    else:
        return False

# Calcula el algoritmo de exponenciación rápida
def mod_exp(base, exp, modulus):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exp = exp // 2
    return result

# Convertir texto a binario en ASCII
def text_to_binary(text):
    return ''.join(format(ord(i), '08b') for i in text)

# Convertir binario a texto en ASCII
def binary_to_text(binary):
    return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))

# Calcula el máximo común divisor
def max_common_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Calcula el inverso multiplicativo
def inverse_multiplicative(a, b):
    for i in range(1, b):
        if (a * i) % b == 1:
            return i
        
    return -1