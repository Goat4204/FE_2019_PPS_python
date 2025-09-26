# To input binary number from user and convert it into decimal number.

str1=input("enter binary number:")
str=str1[::-1]
z=0
for i in range(len(str)):
    x=2**i
    if str[i]=='1':
        z=z+x
    elif str[i]=='0':
        continue
    else:
        print("Error use only 0 or 1 for binary number !!")

print(z)