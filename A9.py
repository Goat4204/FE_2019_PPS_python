'''To accept a number from user and print digits of number in a reverse order.'''

a=int(input("enter any number:"))
rev=0


while a>0:
    x=a%10
    rev=rev*10+x
    a=a//10

print(rev)
