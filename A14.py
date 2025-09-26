#To accept from user the number of Fibonacci numbers to be generated and print
# the Fibonacci series.

n=int(input("how many number of fibonacci series u want:"))

def fibo(n):
    a=0
    b=1
    arr=[]
    for i in range(n):
        temp=b
        b=b+a
        a=temp
        arr.append(b)
    return arr

print(fibo(n))

