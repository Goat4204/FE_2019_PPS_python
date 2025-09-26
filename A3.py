'''To accept N numbers from user. Compute and display maximum in list, minimum in list,
sum and average of numbers.'''


n=int(input("Enter the number of Numbers:"))
list=[]
for j in range(n):
    a=float(input("enter the value of number:"))
    list.append(a)
def maxi(list):
    for i in range(len(list)):
        for j in range(1,len(list)):
            key=list[i]
            if key<list[j]:
                key=list[j]
                i=j
            else:
                continue
    return key


print("maximun in list",maxi(list))
print("minimum in list",min(list))

i=0
temp=0
for i in range(len(list)):
    temp=temp+list[i]

sum=temp
avg=sum/(n)

print("Sum of all the numbers in list :",sum)
print("Avrage of all the numbers in list :",avg)

