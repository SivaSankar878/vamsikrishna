#calculator
a=100
b=30
c='/'
if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c=='%':
    print(a%b) 
elif c=='//':
    print(a//b)
elif c=='/':
    print(a/b)   
elif c=='**':
    print(a**b)  
else:
    print('no operations are done')    


#write a program to check wheather the given number is present in a range
a=999
if a in range(1,100):
    print('present')
else:
    print('not present')       

#find the year is leap year or not
n=2024
if (n%4==0 and n%100!=0)  or n%400==0: 
    print('leap year') 
else:
    print('not a leap year')                     

# 12. Write a program to accept a person's salary and calculate tax based on:
# Salary ≤ 2,50,000 ->No tax
# 2,50,001-5,00,000 ->5%   -> 300000-250000=50000
# 5,00,001-10,00,000 ->20% -> 600000-250000 ->350000*20/100
# 10,00,000 → 30% →1100000-250000 ->850000*30/100  
salary=300000
if salary<=250000:
    print('no tax')
elif salary >= 250001 and salary<=500000:
    sal=salary- 250000
    tax=sal*5/100
    print(tax)    
elif salary>=500001 and salary <=1000000:
    sal=salary- 250000
    tax=sal*20/100
    print(tax) 
elif salary > 1000000:
    sal=salary- 250000
    tax=sal*30/100
    print(tax)         