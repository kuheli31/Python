#Constructors in OOPS

class Student:
    college= "ABC College"#Class attributes
    name="payal"#Class attr.
    #Creating parameterized  constructor
    def __init__(self,fullName,marks):
        self.name=fullName# object attribute >class attributes
        self.marks=marks

    def welcome(self):#methods
        print("Welcome student,",self.name)

    def getMarks(self):#methods
        return self.marks

s1=Student("Kuheli",98)
print(s1.name)#Kuheli
print(s1.marks)#98
print(s1.getMarks())#98 , calling methods
print(s1.welcome())#Welcome student,Kuheli , calling methods

print("\n")

s2=Student("Koyel",92)
print(s2.name)#Koyel
print(s2.marks)#92
print(s2.getMarks())#92
print(s2.welcome())#Welcome student,Koyel

#Class attributes
print(Student.college)