'''To copy contents of one file to other. While copying a) all full stops are to be replaced
with commas b) lower case are to be replaced with upper case c) upper case are to be
replaced with lower case.'''

f=open("demo.txt","rt")
a=f.read()

b=a.swapcase()
c=b.replace(".",",")

g=open("democopy.txt","w")
g.write(c)

f.close()
g.close()
h=open("democopy.txt","r")
print(h.read())