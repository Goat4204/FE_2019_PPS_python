'''To count total characters in file, total words in file, total lines in file and frequency of
given word in file.'''

f=open("demo.txt","rt")
a=f.read()

def char(a):
    count=0
    for i in range(len(a)):
        if a[i]!=" ":
            count=count+1
        else:
            continue

def word(a):
    count=1
    if len(a)==0:
        print("File is Empty")
    else:
        for i in range(len(a)):
            if a[i]==" ":
                count=count+1
        return count

def freq(a):
    x=input("enetr the word to find frequency:")
    print("frequency of word: ",a.count(x))

def line(a):
    count=0
    x=a.splitlines(a)
    len(x)
    print(x,len(x))

line(a)