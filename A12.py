# To accept list of N integers and partition list into two sub lists even and odd numbers.

#input
n=int(input("enter number of intigers:"))
list=[]
for i in range(n):
    a=int(input("enter the intiger:"))
    list.append(a)

#sorting even and odd
even=[]
odd=[]
for i in range(len(list)):
    if list[i]%2==0:
        even.append(list[i])
    else:
        odd.append(list[i])

print("list of even numbers:",even)
print("list of odd numbers:",odd)
