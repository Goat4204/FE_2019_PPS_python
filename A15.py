'''Write a python program that accepts a string from user and perform following string
operations- i. Calculate length of string ii. String reversal iii. Equality check of two
strings iii. Check palindrome ii. Check substring'''

a=input("enter the string:")

def equal(a):
    b=input("enter the string to check:")
    if a==b:
        print("strings are equal")
    else:
        print("strings are not equal")

def palindrome(a):
    x=a[::-1]
    for i in range(len(a)):
        if x==a:
            print("string is palindrome")
        else:
            print("string is not palindrome")
def substr(a):
    x=input("enter substring:")
    if x in a:
        print(x," is substring of ",a)
    else:
        print(x," is not substring of ",a)

def main():
    while True:
        
        print("1. length of string")
        print("2. reverse the string")
        print("3. check if its equal to a string")
        print("4. check if sting is palidrome")
        print("5. check if for substring")
        print("0. exit")

        ch=int(input("enter your choice:"))

        if(ch==1):
            print("length of string is:",len(a))
        elif(ch==2):
            print("reverse of stirng is:",a[::-1])
        elif(ch==3):
            equal(a)
        elif(ch==4):
            palindrome(a)
        elif(ch==5):
            substr(a)
        elif(ch==0):
            break
        else:
            print("wrong choice please select valid choice!!")

main()