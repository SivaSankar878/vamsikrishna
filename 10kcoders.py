#1.for loop
# Print numbers from 1 to 10.
for i in range(1,11):
    print(i,end=",")
print()

# Print all even numbers from 1 to 50.
for i in range(1,51):
    if i%2==0:
        print(i,end=",")
print()        

# Print the squares of numbers from 1 to 10.
for i in range(1,11):
    print(i*i,end=",")
print()

# Print each element of a list using a for loop.
list=[10,20,30,40,50,'pyhton','java']
for i in list:
    print(i,end=",")
print()    

# Find the sum of numbers from 1 to n.
n=int(input('enter the ending number:'))
su=0
for i in range(1,n):
    su+=i
    print("the sum of numbers upto n is:",su)
print()

# Print all numbers divisible by 3 and 5 between 1–100.
for i in range(1,101):
    if i%3==0 and i%5==0:
        print(i,end=",")
print()

#Count how many numbers between 1–100 are divisible by 7.
co=0
for i in range(1,101):
    if i%7==0:
        co+=1
print('the number of 7 divisibles 1 to 100 is:',co)
print()

# Print the multiplication table of any number given by user.
n=int(input('enter a number to print the table:'))
for i in range(1,11):
    print(n,'X',i,'=',n*i)
print()

#Print this pattern:
# *
# **
# ***
# ****
for i in range(5):
    for j in range(i):
        print('*',end="")
    print()
print        

# Print an inverted pattern:
# ****
# ***
# **
# *
for i in range(4,0,-1):
    for j in range(i):
        print("*",end="")
    print()
print()    

#Print all prime numbers between 1 and 100.
l=[]
for i in range(2,101):
    co=0
    for j in range(2,i):
        if i%j==0:
            co+=1
    if co==0:
       l.append(i)
print("the prime numbers between range 1 to 100 is:",l)          
print()

#Calculate the sum of digits of all numbers from 1 to 50.
for i in range(1,51):
    l=[]
    for j in range(1,i+1):
        if i%j==0:
            l.append(j)
    print(f'factors of {i} is:',l)
print()

# Print Fibonacci series using a for loop.
a,b=0,1
n=int(input("enter a nuner to print fibonacci series upto that number:"))
for i in range(n-1):
    a,b=a+b,a
    print(a)

#Print all numbers that are Armstrong numbers between 1–500.
li=[]
n=int(input("enter the ending range:"))
for i in range(1,n):
        k=0
        s=str(i)
        l=len(s)
        if l==3:
            for j in s:
                k+=int(j)**l
            if i==k:
                li.append(i)
print(li)    


#Display a pyramid pattern using nested loops.
n=int(input("enter the number:"))
for i in range(1,n):
    print(" "*(n-i),end=" ")
    for j in range(i):
        print('*',end=" ")
    print()    
print()

# 2.While Loops

# Print numbers from 1 to 10 using while loop.
n=1
while n<=10:
    print(n,end=" ")
    n+=1

# Print numbers from 10 to 1 (reverse order).
n=10
while n>0:
    print(n,end=" ")
    n-=1

#Find the sum of digits of a number.
k=23432
s=0
while k>0:
    n=k%10
    k=k//10
    s+=n
print(s)    

# Count how many digits are in a number.
co=0
n=91771683569502227765
while n>0:
    k=n%10
    co+=1
    n=n//10
print(co)    

# Print even numbers up to 50.
n=1
while n<=50:
    if n%2==0:
        print(n,end=" ")
    n+=1    

# Reverse a number (e.g., 123 → 321).
n=1234
l=''
while n>0:
    k=n%10
    n=n//10
    l+=str(k)
print(l)    

# Keep taking input until the user enters “stop”
while True:
    n=input('enter the input:')
    if n=='stop':
        break

#Check if a number is palindrome using while loop.
s=1234321
o=s
l=''
while s>0:
    n=s%10
    s=s//10
    l+=str(n)
if l==str(o):
    print('palindrome')
else:
    print('not a palindrome') 

s='madam'
k=s
l=''
i=len(s)-1
while i>=0:
    l+=s[i]
    i-=1
if l==k:
    print('palindrome')
else:
    print("not a palindrome")        

# Find factorial of a number using while loop.
n=5
p=1
while n>=1:
    p*=n
    n-=1
print(p)    

# Print all multiples of 5 up to 100.
n=1
while n<=100:
    if n%5==0:
        print(n,end=" ")
    n+=1    

# Print Fibonacci series up to n terms.
n=int(input('enter the number:'))
a,b=0,1
while n>=1:
    a,b=a+b,a
    n-=1
    print(a,end=" ")    

# Generate a pattern using while loops.
n=5
i=1
while i<=n:
    j=1
    while j<=i:
        print("*",end=" ")
        j+=1
    print() 
    i+=1  

# Keep asking for a password until the correct one is entered.
while True:
    n=input('enter password:')
    if n.lower()=='correct':
        break


#3. Conditional Statements (if, elif, else)

# Check if a number is even or odd.
n=int(input("enter a number to check even or odd:"))
if n%2!=0:
    print('odd')
else:
    print('even')    

# Check if a number is positive, negative, or zero.
n=int(input("enter a number to check positive or negative or zero:"))
if n>0:
    print('positive')
elif n<0:
    print('negative')
else:
    print('zero')    

# Find the greatest of two numbers.
a=int(input('enter number a:'))
b=int(input('enter number b:'))
if a>b:
    print('a is big',a)
else:
    print('b is big',b)    

# Check if a character is a vowel or consonant.
c=input('enter a char to check whether the given char is vowel or consonant:')
if c.upper() in 'AEIOU':
    print('vowel')
else:
    print('not a vowel')    

# Check if a number is divisible by 5.
n=int(input('enter a number:'))
if n%5==0:
    print(n, 'is divisible by 5')
else:
    print(n, 'is not divisible by 5')    

# Find the greatest of three numbers.
a=int(input('enter a:'))
b=int(input('enter b:'))
c=int(input('enter c:'))
if a>b and a>c:
    print('a is big',a)
elif b>a and b>c:
    print('b is big')
else:
    print('c is big',c) 

# Check if a year is a leap year.
n=int(input('enter a year to check leap year or not:'))
if (n%4==0 and n%100!=0) or n%400==0:
    print('leap year')
else:
    print('not a leap year')    

# Print grade based on marks:
# >=90 → A
# 80–89 → B
# 70–79 → C
# <70 → Fail
marks=int(input('enter marks:'))
if marks>=90:
    print("A")
elif marks>=80 and marks<=90:
    print('B')
elif marks>=70 and marks<=79:
    print('C')
else:
    print('Fail')            


# Build a simple calculator (add, sub, mul, div).
a=int(input('enter number A:'))
b=int(input('enter number B:'))
c=input('enter the opertaion:')
if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)  
elif c=='*':
    print(a*b)
elif c=='%':
    print(a%b)   
else:
    print('enter a operation must in be +,-,%,*')
       
# Check if a string is palindrome.
s=input('enter a string:')
l=s[::-1]
if s==l:
    print('palindrome')
else:
    print('not a palindrome')  


# Check if three sides can form a valid triangle.
a=int(input('enter number A:'))
b=int(input('enter number B:'))
c=int(input('enter number C:'))
if a+b>c and b+c>a and c+a>b:
    print('it is a valid triangle')
else:
    print('not a valid triangle')    

# Check if a number is a perfect number.
n=int(input('enter a number to check whether a given number is a pefrct number or not:'))
s=0
for i in range(1,n):
    if n%i==0:
        s+=i
if s==n:
    print(s,'==',n,'is a perfect number.')
else:
    print(s,'==',n,'is not a perfect number.')            


# Classify a triangle as equilateral, isosceles, or scalene.
a=int(input('enter side a:'))
b=int(input('enter side b:'))
c=int(input('enter side c:'))
if a==b==c:
    print('equilateral triangle')
elif a==b or b==c or c==a:
    print('isosceles triangle') 
elif a!=b!=c:
    print('scalene triangle')       

#Check whether a number is Armstrong or not.
n=int(input('enter a number to check whether a given number is armstrong or not:'))
s=0
m=n
l=len(str(n))
for i in range(l):
    k=n%10
    n=n//10
    s+=k**l
if s== m:
    print('armstrong number',s)
else:
    print('not a armstrong number',s)        


# Find whether a character is uppercase, lowercase, or digit.
n=input('enter a digit or alpha:')

if n.isdigit():
    print('it is a digit',n)
elif n.islower():
    print('lower case alphabet',n)
elif n.isupper():
    print('upper case alphabet',n)
else:
    print('not a digit or alphabet',n)        


#4.Strings (Operations and Methods)

#Find length of a string.
s='good morning'
length=0
for i in s:
    length+=1
print(length)      

# Convert string to uppercase and lowercase.
s='good morning'
print(s.upper())
print(s.lower())

# Count vowels in a string.
s='virat kholi'
vowels=['a','i','e','o','u']
co=0
for i in s:
    if i.lower() in vowels:
        co+=1
print(co)        

# Reverse a string.
s='virat kholi'
k=''
for i in s:  
    k=i+k 
print(k)    

# Find how many times a letter occurs in a string.
s='virat kholi'
n=input('enter a letter:')
co=0
for i in s:
    if i==n:
        co+=1
print(co)        
  
# Check if a string is palindrome.
s='madam'
k=s[::-1]
if s==k:
    print('palindrome')
else:
    print('not a plaindrome')    

s='madam'
k=''
for i in s:
    k=i+k
if s==k:
    print('palindrome')
else:
    print('not a palindrome') 

# Remove all spaces from a string.
s=' good afternoon everyone '
k=s.strip()
print(k)

# Replace vowels with *.
s='good afternoon everyone'
vowel='AEIOUaeiou'
k=s
for i in s:
    if i in vowel:
        k=k.replace(i,"*")
print(k)

# Split a sentence into words and count them.
s='good afternoon everyone ,glad to be here'.split()
co=0
for i in s:
    co+=1
print(co)    

# Find the longest word in a sentence.
s='good afternoon everyone ,glad to be here'.split()
l=0
l1=''
for i in s:
    if len(i)>l:
        l=len(i)
        l1=i
print(l1,'=',l)

# Remove duplicate characters from a string.
s='hello, world'
c=''
for i in s:
    if i not in c:
        c+=i
print(c)     
   
# Check if two strings are anagrams.
k='listen'
s='silent'
if len(k)==len(s):
    if sorted(k)==sorted(s):
        print('anagram')
    else:
        print('not anagram')    

# Count frequency of each character in a string.
s='hello world'
tem={}
for i in s:
    tem[i]=s.count(i)         
print(tem)
            
# Capitalize the first letter of each word in a sentence.
s='aa22Xa6 movie is going grand releasing above 121 countries'
k=s.title()
print(k)

# Find all substrings of a string.
k='good afternoon developers'.split()
if 'developers' in k:
        print(True)
else:
        print(False)    

#5.User-Defined Functions
#Create a function that prints “Hello World”.
def fun1():
    print('Hello World')
fun1()    

# Function that adds two numbers.
def add(a,b):
    print(a+b)
add(10,20)    

# Function that prints the square of a number.
def square(a):
    print(a**2)
square(10)    

# Function that checks if a number is even or odd.
def evn_check(a):
    if a%2==0:
        print('even')
    else:
        print('odd')  
evn_check(99)          

# Function that returns the sum of numbers in a string.
def sum_no(a):
    s=str(a)
    c=0
    for i in s:
        c+=int(i)
    print(c)
sum_no(12345)       

# Function that returns the sum of numbers in a string.
def s_li(l):
    k=0
    for i in l: 
        k+=i
    print(k)
s_li([10,20,30,40])  
      
# Function to find factorial of a number.
def fact(n):
    c=1
    for i in range(1,n+1):
        c*=i
    print(c)
fact(5)        

# Function that checks if a number is prime.
def p_c(n):
    co=0
    if n<2:
        print('not prime')
    for i in range(2,n):
        if n%i==0:
            co+=1
    if co==0:
        print('prime')
    else:
        print('not a prime')                
p_c(6)                        

# Function to count vowels in a string.
def c_v(s):
    c=0
    for i in s:
        if i.lower() in 'aeiou':
            c+=1
    print(c)
c_v('siva sankar')            

# Function to return maximum element from a list.
def r_m_v(l):
    return max(l)
print(r_m_v([30,40,400]))

def r_mv(l):
    l1=0
    for i in l:
        if i>l1:
            l1=i
    return l1
print(r_mv([89,54,91.5]))        

# Function to reverse a string.
def rev_str(s):
    s1=''
    for i in s:
        s1=i+s1
    return s1
print(rev_str('kholi'))  

# Function that checks if a string is palindrome.
def c_p(s):
    k=''
    for i in s:
        k=i+k
    if k==s:
        print('palindrome')
    else:
        print('not a plaindrome')    
c_p('siva')
c_p('madam')

# Function to return all prime numbers between two numbers.
def p_b_r(s,e):
    for i in range(s,e):
        co=0
        for j in range(2,i):
            if i%j==0:
                co+=1
        if co==0:       
            print(i,end=" ")
p_b_r(10,20)            

# Function that removes duplicates from a list.
def r_d(l):
    k=[]
    for i in l:
        if i not in k:
            k.append(i)
    print(k)
r_d([10,20,10,30,90,60,20])        

# Function to find Fibonacci sequence up to n.
def fibo(n):
    a,b=0,1
    for i in range(n):
        a,b=a+b,a
        print(a,end=" ")
fibo(10)            

# Function that checks if two strings are anagrams.
def anagram(s1,s2):
    if len(s1)==len(s2):
        if sorted(s1)==sorted(s2):
            print('anagram')
        else:
            print('not a anagram')
    else:
        print('not a angarm') 
anagram('silent',"listen")    
anagram('pavann','chakri')               

#6.List Data Type
# Create a list and print all elements.
l=[]
for i in range(10,101,10):
    l.append(i)
print(l)

# Find the length of a list.
l=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
le=0
for i in l:
    le+=1
print(le) 

l=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(len(l))   

# Find the sum of all numbers in a list.
l=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
su=0
for i in l:
    su+=i
print(su)    

l=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(sum(l))

# Find the avg of all numbers in a list.
l=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
l1=len(l)
l2=sum(l)
print("the avg of list is:",l2/l1)

# Add a new element to a list.
l=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
l.append(110)
print(l)

# Remove an element from a list.
l=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
l.remove(100)
print(l)

# Find maximum and minimum elements without using max() or min().
l=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print('minimum nuber in the above list is:',min(l))
print('minimum nuber in the above list is:',max(l))

# Remove duplicates from a list.
l=[10, 20, 30, 10,20]
for i in l:
    while l.count(i)>1:
        l.remove(i)
print(l)

# Reverse a list without using .reverse().
l=[101,102,103,104,105,106,107,108]
k=[]
for i in l:
    k=[i]+k
print(k)    

# Create a list of squares from 1–10.
l=[i**2 for i in range(1,11)]
print(l)

# Find how many even numbers are in a list.
l=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for i in l:
    if i%2==0:
        print(i,end=" ")

# Sort a list manually (without built-in sort).
l=[20,3,5,54,7,98]
n=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print(l)            

# Find the second largest element in a list.
l=[20,3,5,54,7,98]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print("this is the second largest in list:",l[-2])            

# Find all pairs that sum to a given target number.
l=[2,7,9,4,3,6]
t=9
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==t:
            print((l[i],l[j]),end=",")
            

# Merge two sorted lists into one sorted list.
L1= [12, 45, 7, 33, 20]
L2= [50, 3, 17, 45, 8]
l3=sorted(L1)+sorted(L2)
print(sorted(l3))

# Find intersection and union of two lists (without sets).
l1=[10,20,30]
l2=[30,40,50]
l3=[]
l4=l1[:]
for i in l2:
    if i in l1 :
        l3.append(i)
    else:
        l4.append(i)    
print("the intersection of l1,l2 is:",l3)                     
print("the union of l1,l2:",l4)   

