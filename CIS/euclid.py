# A function for computing the greatest common divisor
# using Euclid's algorithm.
# Parameters:
#   a, b - integers
def euclid(a, b):
  print(f"euclid({a}, {b})")
  if b == 0:
    print(f"Reulst is {a}")
    return a
  else:
    print(f"gcd({b}, {a} mod {b})")
    print(f"gcd({b}, {a % b})")
    return euclid(b, a % b)

euclid(30, 21)