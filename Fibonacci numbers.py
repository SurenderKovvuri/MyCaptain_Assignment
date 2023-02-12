n = int(input("Enter a number: "))
n1=0
n2=1
print("The Fibonacci Numbers are: ")
print(n1,",",n2,end="")

for i in range(2, n):
    next= n1 + n2
    print(",",next,end="")
    n1=n2
    n2=next
