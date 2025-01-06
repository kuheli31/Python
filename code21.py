#WAP to find maximum number from a list of numbers.

numbers = input("Enter the numbers: ")
# Example: 34 45 12 -8 89 67

numbers_list = numbers.split()
count = 0

# Count the number of elements
for number in numbers_list:
    count += 1
print(f"The length of the list is: {count}")

# Initialize `max` to the first number (converted to int)
max = int(numbers_list[0])

# Find the maximum number
for i in range(1, count):
    if int(numbers_list[i]) > max:
        max = int(numbers_list[i])

print(f"The maximum number is: {max}")
