#Write a function that will take arbitrary number of arguments and multiply those arguments
#together . multiply(2,3,-6,8)   multiply(2,5,8,9,0,6)

def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

# Test cases
print(multiply(2, 3, -6, 8))  # Output: -288
print(multiply(2, 5, 8, 9, 0, 6))  # Output: 0
