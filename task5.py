# 1.	Print the first n odd numbers.
n=int(input("enter n value:"))
for i in range(n):
    if i%2!=0:
        print(i)
# 2.	Print the first n even numbers.
for i in range(n):
    if i%2==0:
        print(i)
# 3.	Print numbers from n down to 1.
for i in range(n,0,-1):
        print(i)
# 4.	Print numbers from 1 to n in steps of 2.
for i in range(1,n,2):
        print(i)
# 5.	Print numbers from 1 to n in steps of 3.
for i in range(1,n,3):
        print(i)
# 6.	Print the sum of squares of first n numbers.
for i in range(n):
        print(i**2)
# 7.	Print the sum of cubes of first n numbers.
for i in range(n):
        print(i**3)
# 8.	Print the product (multiplication) of first n natural numbers.
l=0
for i in range(n):
      l*=i
print(l)      

# 9.	Print only the numbers between 1 and n that end with digit 5.
for i in range(n):
      if i%10==5:
           print(i) 

# 10.	Count how many numbers between 1 and n are divisible by 4.
count=0
for i in range(n):
      if i%4==0:
            count+=1
print(count)            
# 11.	Count how many numbers between 1 and n are not divisible by 2.
count1=0
for i in range(n):
      if i%2!=0:
            count1 +=1
print(count1)  
# 12.	Print the square of only even numbers between 1 and n.
for i in range(1,n):
        if i%2==0:
              print(i**2)
# 13.	Print the cube of only odd numbers between 1 and n.
for i in range(1,n):
        if i%2!=0:
              print(i**3)
# 14.	Print all numbers between 1 and n that are divisible by both 2 and 3.
for i in range(1,n):
      if i%2==0 and i%3==0:
            print(i)
# 15.	Print all numbers between 1 and n that are divisible by either 2 or 5.
for i in range(1,n):
      if i%2==0 or i%5==0:
            print(i)
# 16.	Find the sum of numbers between 1 and n that are divisible by 7.
t=0
for i in range(1,n):
      if i%7==0:
            t+=i
print(t)            
# 17.	Find the sum of numbers between 1 and n that are not divisible by 3.
s=0
for i in range(1,n):
      if i%3!=0:
            s+=i
print(s) 