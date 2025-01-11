# *args and **kwargs of arbitrary arguments

def infoPerson(*args , **kwargs):
    for key,value in kwargs.items():
        print(key,value)
    print(args)
infoPerson(1,2,name="Ram",age=30,dept="CSE")
print("\n")
infoPerson(1,2,3,name="Tom",age=30,dept="CST")