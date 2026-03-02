# Taking two numbers as input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Addition
addition = num1 + num2
print("Addition:", addition)

# Subtraction
subtraction = num1 - num2
print("Subtraction:", subtraction)

# Multiplication
multiplication = num1 * num2
print("Multiplication:", multiplication)

# Division (check division by zero)
if num2 != 0:
    division = num1 / num2
    print("Division:", division)
else:
    print("Division: Cannot divide by zero")

# Modulus
if num2 != 0:
    modulus = num1 % num2
    print("Modulus:", modulus)
else:
    print("Modulus: Cannot divide by zero")

# Floor Division
if num2 != 0:
    floor_div = num1 // num2
    print("Floor Division:", floor_div)
else:
    print("Floor Division: Cannot divide by zero")

# Exponentiation
power = num1 ** num2
print("Exponentiation:", power)