'''To check whether input number is Armstrong number or not. An Armstrong number is an
integer with three digits such that the sum of the cubes of its digits is equal to the number
itself. Ex. 371.'''

num_og=int(input("enter the number:"))
num=num_og
n=len(str(num))
sum=0
while(num>0):
    dig=num%10
    sum += (dig ** n)
    num=num//10

if(sum==num_og):
    print("number is armstrong number")
else:
    print("number is not armstrong number")