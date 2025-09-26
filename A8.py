'''To accept two numbers from user and compute smallest divisor and Greatest Common
Divisor of these two numbers.'''

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
x=[]
y=[]
z=[]

#finding divisor of 1st number
for i in range(1,a+1):
    if a%i==0:
        x.append(i)

#finding divisor of 2nd number
for j in range(1,a+1):
    if b%j==0:
        y.append(j)


#finding comman divisors
for i in range(len(x)):
    for j in range(len(y)):
        if x[i]==y[j]:
            z.append(y[j])



print("divisor of ",a," :",x)
print("divisor of ",b," :",y)
print("comman divisor:",z)
print("smallest coman divisor:",min(z))
print("greatest comman diviser:",max(z))
