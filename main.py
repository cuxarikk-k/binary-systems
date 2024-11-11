def decimal_to_binary():
  decimal = int(input("Enter a decimal number: "))
  binary = ""
  if decimal == 0:
    return "0"
  while decimal > 0:
    binary = str(decimal % 2) + binary
    decimal = decimal // 2
  return binary

def binary_to_decimal():
  while True:
    binary = input("Enter a binary number: ")
    decimal = 0
    if binary.startswith("0b"):
      binary = binary[2:]
    else:
      print("Please enter a hexadecimal number with the prefix 0b.")
      return None
    for i in range(len(binary)):
      decimal += int(binary[i]) * (2 ** (len(binary) - i - 1))
    return decimal

def decimal_to_hexadecimal():
  decimal = int(input("Enter a decimal number: "))
  letters = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
  hexadecimal = ""
  if decimal == 0:
    return "0"
  while decimal > 0:
    x = decimal % 16
    if x > 9:
      hexadecimal = letters[x] + hexadecimal
    else:
      hexadecimal = str(decimal % 16) + hexadecimal
    decimal = decimal // 16
  return hexadecimal

def hexadecimal_to_decimal():
  while True:
    hexadecimal = input("Enter a hexadecimal number: ")
    letters = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    decimal = 0
    if hexadecimal.startswith("0x"):
      hexadecimal = hexadecimal[2:].upper()
    else:
      print("Please enter a hexadecimal number with the prefix 0x.")
      return None
    for i in range(len(hexadecimal)):
      if hexadecimal[i] in letters:
        decimal += letters[hexadecimal[i]] * (16 ** (len(hexadecimal) - i - 1))
        return decimal
      elif '0' <= hexadecimal[i] <= '9':
        decimal += int(hexadecimal[i]) * (16 ** (len(hexadecimal) - i - 1))
        return decimal
      else:
        print("Please, enter valid hexadecimal number.")
        return None

def decimal_to_base():
  while True:
    users_input = input("Enter a number with its base (e. g., 3123x4): ")
    if "x" not in users_input:
      print("Please, enter a valid number with its base.")
      continue
    decimal_to_base, base = users_input.split("x")
    base = int(base)
    decimal = int(decimal_to_base)
    based_number = ''
    symbols = '0123456789ABCDEF'
    if base < 2 or base > 16:
      print("Please, enter a base between 2 and 16.")
      continue
    if decimal == 0:
      return "0"
    while decimal > 0:
      based_number = symbols[decimal % base] + based_number
      decimal = decimal // base
    return based_number

def base_to_decimal():
  while True:
    users_input = input("Enter a number with its base (e. g., 3123x4) to convert to decimal: ")
    if "x" not in users_input:
      print("Please, enter a valid number with its base.")
      return None
    base_to_decimal, base = users_input.split("x")
    letters = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    base = int(base)
    decimal = 0
    if base < 2 or base > 16:
      print("Please, enter a base between 2 and 16.")
      continue
    for i in range(len(base_to_decimal)):
      if base_to_decimal[i] in letters:
        decimal += letters[base_to_decimal[i]] * (base ** (len(base_to_decimal) - i - 1))
      elif '0' <= base_to_decimal[i] <= '9':
        decimal += int(base_to_decimal[i]) * (base ** (len(base_to_decimal) - i - 1))
      else:
        print("Please, enter a valid number with its base.")
    else:
      return decimal

def conversation():
  while True:
    choice = int(input("Press: \n1.decimal to binary \n2.binary to decimal \n3.decimal to hexadecimal \n4.hexadecimal to decimal \n5.decimal to base \n6.base to decimal"))
    if choice == 1:
      print(decimal_to_binary())
    elif choice == 2:
      print(binary_to_decimal())
    elif choice == 3:
      print(decimal_to_hexadecimal())
    elif choice == 4:
      print(hexadecimal_to_decimal())
    elif choice == 5:
      print(decimal_to_base())
    elif choice == 6:
      print(base_to_decimal())
    else:
      print("Please, enter a valid number.")
      return None
    to_continue = input("Do you want to continue?").lower()
    if to_continue == "yes":
      continue
    elif to_continue == "no":
      break

print(conversation())