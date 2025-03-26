
def fact(num):
    a=num
    factorial=1
    while(num>0):
        factorial*=num
        num-=1
    return factorial

a=int(input("Enter a Number:"))
print("Factorial of",a,"is",fact(a))
