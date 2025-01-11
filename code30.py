#Arbitrary Arguments

def add(*numbers):#tuple is (5,7,9) or arbitrary positional arguments is *
    c=0
    for i in numbers:
        c=c+i
    print(f"Sum is= {c}")
add(5,7,9)
add(1,2,3,4)