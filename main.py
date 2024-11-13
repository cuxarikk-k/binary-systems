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
      print("Please enter a binary number with the prefix 0b.")
      break
    for i in range(len(binary)):
      if binary[i] not in ["0", "1"]:
        print("Please enter a binary number with only 0s and 1s.")
        break
      else:
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
      continue
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

def base_to_base():
  while True:
    users_input = input("Enter a number with its base (e. g., 3123x4) to convert to another base: ")
    another_base = input("Enter the base to convert to (e.g., x16): ")
    if ("x" not in users_input) or ("x" not in another_base):
      print("Please, enter a valid number with its base.")
      continue
      
    base_to_base, base = users_input.split("x")
    base = int(base)
    another_base = int(another_base[1:])
    base_to_base = base_to_base.upper()
    letters = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    symbols = '0123456789ABCDEF'
    decimal = 0
    based_number = ''
    
    for i in base_to_base:
      if i in letters and letters[i] >= base:
        print("Please, enter a valid number with this base.")
        continue
      elif "0" <= i <= "9" and int(i) >= base:
        print("Please, enter a valid number with this base.")
        continue
        
    if (base < 2 or base > 16) or (another_base < 2 or another_base > 16):
      print("Please, enter a base between 2 and 16.")
      continue
    for i in range(len(base_to_base)):
      if base_to_base[i] in letters:
        decimal += letters[base_to_base[i]] * (base ** (len(base_to_base) - i - 1))
      elif '0' <= base_to_base[i] <= '9':
        decimal += int(base_to_base[i]) * (base ** (len(base_to_base) - i - 1))
        
    if decimal == 0:
      return "0"
    else:
      while decimal > 0:
        based_number = symbols[decimal % another_base] + based_number
        decimal = decimal // another_base
      return based_number

def conversation():
  while True:
    choice = int(input("Press: \n1.decimal to binary \n2.binary to decimal \n3.decimal to hexadecimal \n4.hexadecimal to decimal \n5.base to base"))
    if choice == 1:
      print(decimal_to_binary())
    elif choice == 2:
      print(binary_to_decimal())
    elif choice == 3:
      print(decimal_to_hexadecimal())
    elif choice == 4:
      print(hexadecimal_to_decimal())
    elif choice == 5:
      print(base_to_base())
    else:
      print("Please, enter a valid number.")
      return None
    to_continue = input("Do you want to continue?").lower()
    if to_continue == "yes":
      continue
    elif to_continue == "no":
      break

print(conversation())
