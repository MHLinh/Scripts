import math

# A function for computing x and y such that gcd(a,b) = (x*a) + (y*b),
# using the Extended Euclid's algorithm.
# Parameters:
#   a, b - integers
def extEuclid(a, b):
  if b == 0:
    return (a, 1, 0)
  else:
    (d1, x1, y1) = extEuclid(b, a % b)
    q = math.floor(a / b)
    (d, x, y) = (d1, y1, x1 - q * y1)
    return (d, x, y)

# A function to encrypt a message.
# Parameters:
#   e - recipient public key first part
#   n - recipient public key second part (product of 2 large primes p and q)
#   M - message
def encrypt(e, n, M):
  return (M**e) % n

# A function to decrypt a cipher text.
# Parameters:
#   d - recipient private key first part
#   n - recipient private key second part (product of 2 large primes p and q)
#   C - cipher text
def decrypt(d, n, C):
  return (C**d) % n

# A function to compute all necessary components for RSA 
# and encryption of message knowing e.
# Parameters:
#   p, q - prime numbers
#   e - public key first part
#   M - message
def rsa_e(p, q, e, M):
  n = p * q
  phi_n = (p-1)*(q-1)

  d = extEuclid(phi_n, e)[2] % phi_n
  C = encrypt(e, n, M)
  print()
  print(f"n = {n}")
  print(f"phi_n = {phi_n}")
  print(f"e = {e}")
  print(f"d = {d}")
  print(f"C = {C}")

# A function to compute all necessary components for RSA 
# and encryption of message knowing d.
# Parameters:
#   p, q - prime numbers
#   d - private key first part
#   M - message
def rsa_d(p, q, d, M):
  n = p * q
  phi_n = (p-1)*(q-1)

  e = extEuclid(phi_n, d)[2] % phi_n
  C = encrypt(e, n, M)
  print()
  print(f"n = {n}")
  print(f"phi_n = {phi_n}")
  print(f"e = {e}")
  print(f"d = {d}")
  print(f"C = {C}")

rsa_e(17, 31, 7, 2)

rsa_e(7, 13, 23, 51)