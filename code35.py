# Nested dictionary
student = {
    "keys" : "value",
    "name": "Kuheli Bera",
    "subjects": {
        "phy": 90.5,
        "chem": 85,
        "maths": 90
    },
    "roll": 45
}
print(student)

# Correct way to access the "phy" value
print(student["subjects"]["phy"])

#typecasted 
print(student.keys())