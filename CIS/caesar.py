letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# A function trying out all caesar keys for decryption of cipher text.
def caesar(cypher_text):
  for i in range(26):
    decryption = ""
    for letter in cypher_text:
      decryption = decryption + letters[(letters.index(letter) + i) % 26] 
    print(i, decryption)

caesar("EVIRE")
