#To accept the number of terms a finds the sum of sine series.

a=int(input("enter the number to find sine series:"))
n=int(input("enter number of terms to sum:"))

for i in range(n+1):
    sine=((-1)**i)*((a**((2*i)+1))/((2*n)+1))

print("sum is ",sine)