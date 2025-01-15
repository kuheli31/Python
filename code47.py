#Class Method

class Person:
    name="anonymous"

    #def changename(self , name):
     #   self.__class__.name = "Kuheli"

    @classmethod
    def changename(cls , name):
        cls.name = name

p1 = Person()
p1.changename("Kuheli Bera")
print(p1.name)
print(Person.name)