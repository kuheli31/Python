#WAP which will select a random name from a list of names and the person will have to pay for everyone's food bill.

import random
names = input("Enter the names of the people separated by commas: ")

namesList = names.split(",")
billPayer = random.randint(0, len(namesList) - 1)

print(f"{namesList[billPayer]} will pay the bill today.")