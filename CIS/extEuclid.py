
import math
from tabulate import tabulate

# A function for computing x and y such that gcd(a,b) = (x*a) + (y*b),
# using the Extended Euclid's algorithm.
# Parameters:
#   a, b - integers
def ext_euclid(a, b):
  if b == 0:
    print(a, b, "-", a, 1, 0)
    return (a, 1, 0)
  else:
    (d1, x1, y1) = ext_euclid(b, a % b)
    q = math.floor(a / b)
    print(d1, x1, y1)
    (d, x, y) = (d1, y1, x1 - q * y1)
    print(a, b, q, d, x, y)
    return (d, x, y)

# ext_euclid(99, 78)

# A function for computing x and y such that gcd(a,b) = (x*a) + (y*b),
# using the Extended Euclid's algorithm, but with passed in list to store data.
# Helper function for ext_euclid_table.
# Parameters:
#   a, b - integers
#   data - list of integers
def ext_euclid_data(a, b, data):
  if b == 0:
    row = [a, b, "-", a, 1, 0]
    data.append(row)
    return (a, 1, 0)
  else:
    (d1, x1, y1) = ext_euclid_data(b, a % b, data)
    q = math.floor(a / b)
    (d, x, y) = (d1, y1, x1 - q * y1)
    row = [a, b, q, d, x, y]
    data.append(row)
    return (d, x, y)

# A function for computing x and y such that gcd(a,b) = (x*a) + (y*b),
# using the Extended Euclid's algorithm.
# Prints out a formatted table.
# Parameters:
#   a, b - integers
def ext_euclid_table(a, b):
  data = [] 
  headers = ["a", "b", "[a/b]", "d", "x", "y"]

  ext_euclid_data(a,b, data)
  data.reverse()

  print()
  print(tabulate(data, headers))
  print()

  print("For RSA")
  y = data[0][5]
  totient = a
  if y < 0:
    print(f"d = y mod a = {y % totient}")
  else:
    print(f"d = y = {y}")

ext_euclid_table(72,23)