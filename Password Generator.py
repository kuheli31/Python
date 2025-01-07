#Random password will be generated
import random

print("Welcome to the Password Generator!")
letterLength = int(input("How many letters would you like in your password?\n"))  # Convert to integer
symbolLength = int(input("How many symbols would you like?\n"))  # Convert to integer
numberLength = int(input("How many numbers would you like?\n"))  # Convert to integer

# Define the character sets
letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)] + [chr(i) for i in range(ord('a'), ord('z') + 1)]  # Upper and lowercase letters
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']
numbers = [str(i) for i in range(10)]  # Digits 0-9

#password generating
password=[]

# Add random letters
for i in range(letterLength):
    password.append(random.choice(letters))

#Adding random symbols
for i in range(symbolLength):
    password.append(random.choice(symbols))

#Adding random numbers
for i in range(numberLength):
    password.append(random.choice(numbers))

#shuffling the list in password
random.shuffle(password)

# Join the password list into a string
password=''.join(password)
print(f"Password is = {password}")
