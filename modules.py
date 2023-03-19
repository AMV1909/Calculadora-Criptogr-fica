# Verificar si un número es primo o no
def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
        else:
            return True
    else:
        return False


def mcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b//a, b % a
        m, n = x-u*q, y-v*q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


def inv(a, m):
    gcd, x, y = mcd(a, m)
    print(gcd, x, y)
    if gcd != 1:
        return None  # No existe el inverso multiplicativo
    else:
        return x % m
