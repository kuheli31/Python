#WAP to print the FIzzBuzz number. If a number is divisible by 3 , then its "Fizz" and if the number 
#divisible by 5 then its "Buzz" otherwise if divisible by both 3 & 5 then its FizzBuzz Number and if 
#its nothing then print the number only.

for i in range(1,101):
    if(i%3)==0 and (i%5)==0:
        print("FizzBuzz")
    elif(i%5)==0:
        print("Buzz")
    elif(i%3)==0:
        print("Fizz")
    else:
        print(i)



