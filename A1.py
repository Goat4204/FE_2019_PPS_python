'''To calculate salary of an employee given his basic pay (take as input from user).
Calculate gross salary of employee. Let HRA be 10 % of basic pay and TA be 5% of
basic pay. Let employee pay professional tax as 2% of total salary. Calculate net salary
payable after deductions.'''

sal=float(input("Enter your salary:"))

hra=sal/10
ta=(sal*5)/100
gross_sal=hra+sal+ta
tax=(2*sal)/100
net_sal=gross_sal-tax

print("you entered salary :",sal)
print("HRA :",hra)
print("TA :",ta)
print("Gross Salary :",gross_sal)
print("TAX :",tax)
print("your final net salary :",net_sal)