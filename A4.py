'''To accept student’s five courses marks and compute his/her result. Student is passing if
he/she scores marks equal to and above 40 in each course. If student scores aggregate
greater than 75%, then the grade is distinction. If aggregate is 60>= and <75 then the
grade if first division. If aggregate is 50>= and <60, then the grade is second division. If
aggregate is 40>= and <50, then the grade is third division.'''

print("please enter your marks out of 100")
s1=float(input("Enters marks in maths:"))
s2=float(input("Enters marks in science:"))
s3=float(input("Enters marks in python:"))
s4=float(input("Enters marks in social studies:"))
s5=float(input("Enters marks in economics:"))

sum=s1+s2+s3+s4+s5
percent=sum/5

if(percent>=40):
    print("Contratulation you have been passed in exam!")
else:
    print("You are failed in exam :(")

#grading
if(percent>=75):
    print("Grade: Distinction")
elif(percent>=60 and percent<75):
    print("Grade: first division")
elif(percent>=50 and percent<60):
    print("Grade: second division")
elif(percent>=40 and percent<50):
    print("Grade: third division")
else:
    print("Grade: Fail")
