#Create student class that takes name & marks of 3 subjects as arguments in constructor.
#Then create a method to print the average.

class Student:
    def __init__(self , name , a , b, c):
        self.name=name
        self.avg=(a+b+c)//3

s1=Student("Kuheli" , 60 , 50 , 90)
print(s1.name)#Kuheli
print(s1.avg)#66

