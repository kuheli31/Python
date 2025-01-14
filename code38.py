#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
#an empty dictionary & add one by one. Use subject name as key & marks as value.

phy=int(input("Enter marks for physics:"))
chem=int(input("Enter marks for chemistry:"))
math=int(input("Enter marks for maths:"))

subjects={}
subjects = {"Physics" : phy , "Chemistry" : chem , "Maths" : math}

print(subjects)
