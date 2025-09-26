'''To simulate simple calculator that performs basic tasks such as addition, subtraction,
multiplication and division with special operations like computing xy
and x!.'''

'''To accept the number and Compute a) square root of number, b) Square of number, c)
Cube of number d) check for prime, d) factorial of number e) prime factors'''

def addition(a,b):
    return a+b
def subtraction (a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def power(a,b):
    return a**b
def fact(a):
    x=1
    for i in range(1,a+1):
        x=x*i
    return x
def root(a):
    return a**0.5
def square(a):
    return a*a
def cube(a):
    return a**3
def prime(a):
    if a==1:
        return False
    elif a==2:
        return True
    elif a%2==0:
        return False
    else:
        for i in range(3,int(root(a))+1):
            if(a%i==0):
                return False
        return True
    
def factor(a):
    y = []
    divisor = 2
    while a > 1:
        if a % divisor == 0:
            y.append(divisor)
            a=a// divisor
        else:
            divisor += 1
    print(y)

def main():
    while True:
        n=int(input("Enter the number:"))
        print("1.addition")
        print("2.substraction")
        print("3.multiplication")
        print("4.division")
        print("5.factorial")
        print("6.to the power")
        print("7.square root")
        print("8.squre")
        print("9.cube")
        print("10.prime number check")
        print("11.prime factors")
        print("0. exit")
        ch=int(input("\nEnter your choice:"))

        if(ch==1):
            a=int(input("number to add:"))
            print(addition(n,a))
        elif(ch==2):
            a=int(input("number to substract:"))
            print(subtraction(n,a))
        elif(ch==3):
            a=int(input("number to muliplay:"))
            print(multiply(n,a))
        elif(ch==4):
            a=int(input("number to divde:"))
            print(divide(n,a))
        elif(ch==5):
            print(fact(n))
        elif(ch==6):
            a=int(input("power:"))
            print(power(n,a))
        elif(ch==7):
            print(root(n))
        elif(ch==8):
            print(square(n))
        elif(ch==9):
            print(cube(n))
        elif(ch==10):
            if(prime(n)):
                print("number is prime")
            else:
                print("number is not prime")
        elif(ch==11):
            factor(n)
        elif(ch==0):
            break
        else:
            print("wrong choice Try again")

main()