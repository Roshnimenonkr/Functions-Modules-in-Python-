
def factorial(num):
    a=num
    fact=1
    while(num>0):
        fact*=num
        num-=1
    return fact

a=int(input("Enter a Number:"))
print("Factorial of",a,"is",factorial(a))
