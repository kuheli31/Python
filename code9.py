# Ask for pizza size
size = input("Enter size of the pizza (S, M, L): ").lower()

# Initialize the bill based on the size
if size == 's':
    bill = 100
elif size == 'm':
    bill = 200
elif size == 'l':
    bill = 300
else:
    print("Please enter a valid input")
    exit()  # Exit the program if the size input is invalid

# Ask about pepperoni topping
topings = input("Do you need pepperoni on your pizza (Y/N): ").lower()
if topings == 'y':
    bill += 30 if size == 's' else 50  # Adjust topping price based on size

# Ask about extra cheese
cheese = input("Would you like to have extra cheese on it (Y/N): ").lower()
if cheese == 'y':
    bill += 20

# Display the total bill
print(f"Your total bill is {bill}")
