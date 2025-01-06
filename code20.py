#WAP to calculate average height from a list of heights.
inHeight = input("Enter the height of students in cm: ")
height = inHeight.split()
sum=0
length=0
for i in height:
    sum+=int(i)
    length=length+1
else:
    avg = sum//length
    print("Average height of students is: ",avg)