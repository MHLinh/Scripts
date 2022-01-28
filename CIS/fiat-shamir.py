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

# A function for computing response to challenge
def response(r, s, c, n):
  return (r * s**c) % n

# Helper functions to check identity
def check_a(y, n):
  return y**2 % n

def check_b(x, v, c, n):
  return (x * v**c) % n

# A function computing all components during a Fiat-Shamir identification protocol.
# Parameters:
#   p, q - prime numbers
#   s - secret
#   r - chosen commitment
def fiat_shamir(p, q, s, r):
  n = p*q
  v = (s**2) % n # known to verifier
  x = (r**2) % n # witness

  # verifier's challenge 0
  y_0 = response(r, s, 0, n)
  check_0a = check_a(y_0, n)
  check_0b = check_b(x, v, 0, n)

  # verifier's challenge 1
  y_1 = response(r, s, 1, n)
  check_1a = check_a(y_1, n)
  check_1b = check_b(x, v, 1, n)

  print()
  print("Fiat-shamir")
  print(f"n = {n}")
  print(f"v = {v}")
  print(f"r = {r}")
  print(f"x = {x}")
  print(f"y_0 = {y_0}, check_0a = {check_0a}, check_0b = {check_0b}")
  print(f"y_1 = {y_1}, check_1a = {check_1a}, check_1b = {check_1b}")

# A function computing all components during a cheating Fiat-Shamir identification protocol.
# Parameters:
#   v - known number (s^2 mod n, s only known to authorised party)
#   r - chosen commitment
#   n - computed product of prime numbers
def cheat(v, r, n):
  x_0 = (r**2) % n
  y_0 = r % n
  check_0a = check_a(y_0, n)
  check_0b = check_b(x_0, v, 0, n)

  v_inverse = extEuclid(n, v)[2]
  x_1= (r**2 * v_inverse) % n
  y_1 = r % n
  check_1a = check_a(y_1, n)
  check_1b = check_b(x_1, v, 1, n)

  print()
  print("Cheat")
  print(f"n = {n}")
  print(f"v = {v}")
  print(f"x_0 = {x_0}")
  print(f"y_0 = {y_0}, check_0a = {check_0a}, check_0b = {check_0b}")
  print(f"x_1 = {x_1}")
  print(f"y_1 = {y_1}, check_1a = {check_1a}, check_1b = {check_1b}")

# fiat_shamir(p, q, s, r)
fiat_shamir(3, 7, 5, 11)

cheat(4, 14, 21)