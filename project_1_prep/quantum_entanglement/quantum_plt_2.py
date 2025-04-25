import math

from sympy import mod_inverse

N = 55  # modulus
e = 11  # public exponent
C = 4  # Example ciphertext


def factorize(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i, n // i

    return None, None


p, q = factorize(N)

if p and q:
    print(f"Factors found: p = {p}, q = {q}")
    phi = (p - 1) * (q - 1)
    print(f"Phi: {phi}")
    d = mod_inverse(e, phi)
    print(f"Private key is: {d}")
else:
    print("Factors not found")

"""
Output:

Factors found: p = 5, q = 11
Phi: 40
Private key is: 11
"""