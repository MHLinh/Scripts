# A function to compute the Diffie-Hellman key exchange.
# Parameters:
#   a - shared integer
#   q - shared prime number
#   x_a - randomly generated number by party A
#   x_b - randomly generated number by party B
def diffie(a, q, x_a, x_b):
  y_a = (a**x_a) % q
  y_b = (a**x_b) % q

  # generated key, should be the same for both parties
  k_a = (y_b**x_a) % q
  k_b = (y_a**x_b) % q

  print()
  print("Diffie")
  print(f"YA = {y_a}, KA = {k_a}")
  print(f"YB = {y_b}, KB = {k_b}")

# A function to compute the Diffie-Hellman key exchange with man-in-the-middle attack.
# Parameters:
#   a - shared integer
#   q - shared prime number
#   x_a - randomly generated number by party A
#   x_b - randomly generated number by party B
#   x_c - randomly henerated number by party C (attacker)
def middle(a, q, x_a, x_b, x_c):
  y_a = (a**x_a) % q
  y_b = (a**x_b) % q
  y_c = (a**x_c) % q

  k_ac = (y_c**x_a) % q # key generated between A and C
  k_bc = (y_c**x_b) % q # key generated between B and C

  print()
  print("Middle")
  print(f"YA = {y_a}, KAC = {k_ac}")
  print(f"YB = {y_b}, KBC = {k_bc}")
  print(f"YC = {y_c},  KAC = {k_ac}, KBC = {k_bc}")

diffie(2, 11, 4, 3)

middle(2, 11, 4, 3, 9)