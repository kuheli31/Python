#WAP to calculate sum of even numbers from 1-100 including 1 & 100.
even=0
for i in range(1,101):
    if(i%2)==0:
        print(i)
        even=even+i
print(f"Sum of even numbers=",even)