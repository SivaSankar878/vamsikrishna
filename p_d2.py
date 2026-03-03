# # Python Problem-Solving Questions (90+) 
# # 1. Strings (15 Questions) 
# # 1. Reverse a string without slicing.
# s='gopi chand'
# r_s=''
# for i in s:
#     r_s=i+r_s
# print(r_s) 
    
# 2. Check if a string is a palindrome. 
# s='madam'
# k=s[::-1]
# if s==k:
#     print('palindrome')
# else:
#     print('not a palindrome') 

# # 3. Count vowels and consonants in a string. 
# s='siva sankar'
# vowel='aeiou'
# consonanats='bcdfghjklmnpqrstvwxyz'
# c_o=0
# c_c=0
# for i in s:
#     if i in vowel:
#         c_o+=1
#     if i in consonanats:
#         c_c+=1  
# print('vowels:',c_o)
# print('consonanats:',c_c)
          
# # 4. Remove duplicates from a string. 
# s='siva sankar'
# k=''
# for i in s:
#     if i not in k:
#         k+=i
# print(k)  
      
# # 5. Find the most frequent character in a string. 
# s='programming'
# l=max(s,key=s.count)
# print(l)

# # 6. Convert a sentence to title case manually. 
# k='hello world'.split()
# l=''
# for i in k:
#     l+=i[0].upper()+i[1:]
# print(l,end=" ")      
    
# # 7. Check if two strings are anagrams.
# str1='silent'
# str2='listen'
# if len(str1)==len(str2):
#     if sorted(str1)==sorted(str2):
#         print('anagram') 
#     else:
#         print("not a anagram") 
   
# # 8. Count the number of words in a string without split(). 
# s='hello everyone, now time is 7:00'
# cou=1
# for i in s:
#     if i==" ":
#         cou+=1
# print(cou)

# # 9. Remove all spaces from a string.
# s='hello everyone, now time is 7:00'
# l=''
# for i in s:
#     if i!=" ":
#         l+=i
# print(l)        
 
# # 10. Replace all occurrences of a character in a string.
# s='banana'
# rep=s.replace('a','x')
# print(rep)

# # 11. Find first non-repeating character. 
# s='nanapython'
# l=''
# co=0
# for i in s:
#     if s.count(i)==1:
#         print(i)
#         break

# # 12. Find longest word in a sentence.
# s='hello everyone, now time is 7:00'
# m=s.split()
# k=''
# for i in m:
#     if len(i)>len(k):
#         k=i
# print(k) 

# # 13. Check if a string contains only digits. 
# s='siva11'
# if s.isdigit():
#     print(True)
# else:
#     print(False) 

# # 14. Reverse words in a sentence.
# s='siva sankar tati'
# k=''
# for i in s:
#     k=i+k
# print(k)  

# s='siva sankar tati'.split()
# k=''
# for i in s:
#     k=i+" "+k
# print(k)  

# # 15. Implement atoi() (string to integer conversion). 
# s = "6783390"
# num = 0
# for i in s:
#     num = num * 10 + (ord(i) - ord('0'))
# print(num)

# # 2. Numbers / Math (15 Questions) 
# # 16. Check if a number is prime.
# n=int(input('enter number'))
# co=0
# for i in range(2,n):
#         if n%i==0:
#             co+=1
# if co==0:
#         print('prime')
# else:
#         print("not a prime")

# # 17. Find all prime numbers in a range.
# n=int(input("enter a number:"))
# l=[]
# for i in range(2,n):
#     co=0
#     for j in range(2,i):
#         if i%j==0:
#             co+=1
#     if co==0:
#         l.append(i)
# print(l)
             
# # 18. Factorial of a number (iterative & recursive). 
# n=int(input('enter a number:'))
# p=1
# for i in range(1,n+1):
#     p*=i
# print(p) 

# def fact(n):
#     if n==0 or n==1:
#         return 1 
#     else:
#         return n*fact(n-1)
# print(fact(5))

# 19. Generate Fibonacci series (iterative & recursive). 
# a,b=0,1
# n=int(input('enter a number:'))
# for i in range(n-1):
#     a,b=b,a+b
#     print(a)

# def fibo(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)
# print(fibo(9))
    
# # 20. Check if a number is Armstrong. 
# n=153
# temp=n
# d=0
# l=len(str(n))
# while temp>0:
#     n=temp%10
#     d+=n**l
#     temp//=10
# print(d)

# # 21. Find  LCM of two numbers.
# a=27
# b=12
# l=a if a>b else b
# for i in range(l,a*b+1):
#     if i%a==0 and i%b==0:
#         print(i)
#         break

# 22. Reverse a number without converting to string.
# n=12345
# temp=n
# k=0
# while temp>0:
#     digit=temp%10
#     k=k*10+digit
#     temp//=10
# print(k)

# # 23. Count digits in a number. 
# n=123454673
# temp=n
# co=0
# while temp>0:
#     dig=temp%10
#     co+=1
#     temp//=10
# print(co)

# # 24. Sum of digits of a number. 
# n=12345
# te=n
# s=0
# while te>0:
#     dig=te%10
#     te//=10
#     s+=dig
# print(s)

# # 25. Check if a number is perfect.
# n=28
# s=0
# for i in range(1,n):
#     if n%i==0:
#         s+=i
# if n==s:
#     print('perfect')
# else:
#     print('not perfect') 
    
# # 26. Find sum of first n natural numbers. 
# n=100
# s=0
# for i in range(1,n+1):
#     s+=i
# print(s)

# # 27. Count trailing zeros in factorial of a number. 
# n=10
# c=0
# te=n
# while te>0:
#     te=te//5
#     c+=te
# print(c)

# # 28. Check if a number is a palindrome. 
# n=101
# te=n
# s=0
# while te>0:
#     d=te%10
#     s=s*10+d
#     te=te//10
# if s==n:
#     print('palindrome')
# else:
#     print('not a palindrome')    

# # 29. Check if a number is a strong number. 
# # 30. Find nth term in Fibonacci series. 
# n=10
# a,b=0,1
# for i in range(1,n+1):
#     a,b=b+a,a
# print(a)

# 3. Lists / Arrays (15 Questions) 
# # 31. Find max & min in a list without using built-ins.
# l=[42, 7, 89, 15, 63, 28, 94, 51, 36, 77]
# min=l[0]
# max=l[0]
# for i in l:
#     if i>max:
#        max=i
#     if i<min:
#        min=i
# print('max:',max)
# print('min:',min)            

# # 32. Remove duplicates from a list.
# l=[5, 2, 7, 5, 9, 2, 7, 5, 1, 9,19,21,8,45]
# k=[]
# for i in l:
#     if l.count(i)==1:
#         k.append(i)
# print(k) 

# # 33. Find second largest element.
# l=[42,7,89,15,63,28,94,51,36,77]
# k=sorted(l)
# print(k[-2])

 
# # 34. Rotate a list by n elements. 
# l=[42,7,89,15,63,28,94,51,36,77]
# n=3
# k=l[n:]+l[:n]
# print(k)

# # 35. Merge two sorted lists.
# l1=[10,20,30,40]
# l2=[100,200,300,400] 
# l=l1+l2
# print(l)

# # 36. Find pairs with a given sum.
# l=[2,4,3,5,7,8,1,9]
# t=10
# t2=[]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==t:
#             t2.append((l[i],l[j]))
# print(t2)
            
# # 37. Subarray with maximum sum (Kadane’s Algorithm). 
# l = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# max_sum=l[0]       
# current_sum=l[0]   
# for i in range(1, len(l)):
#     current_sum = max(l[i], current_sum + l[i])
#     max_sum = max(max_sum, current_sum)
# print("Maximum Subarray Sum:", max_sum)

# # 38. Move all zeros to the end. 
# l=[10,0,21,0,34,0,23,0,0]
# l1=[]
# for i in l:
#     if i!=0:
#        l1.append(i)
# for i in l:
#     if i==0:
#        l1.append(i)
# print(l1)       

# # 39. Find missing number in a list of 1..n. 
# l=[1,2,3,4,5,7]
# n=len(l)+1
# mis_num=(n*(n+1))//2-sum(l)
# print(mis_num)

# l=[1,3,4,6,8,10]
# n=10
# mis_num=list(set(range(1,n+1))-set(l))
# print(sorted(mis_num))

# # 40. Check if list is palindrome.
# list=[1,2,3,4,5,4,3,2,1]
# if list==list[::-1]:
#     print('list is palindrome')
# else:
#     print('list is not a palindrome')  
  
# # 41. Flatten a nested list. 
# n=[[1,2,3],[4,5,6],[7,8,9]]
# list=[]
# for i in n:
#     for j in i:
#         list.append(j)
# print(list)        

# # 42. Find intersection of two lists.
# l1=[1,2,3,4,5,6]
# l2=[3,4,7,8,21,9]
# l3=[]
# for i in l1:
#     if i in l2:
#         l3.append(i)
# print(l3) 

# l1=[1,2,3,4,5,6]
# l2=[3,4,7,8,21,9]
# l3=list(set(l1)&set(l2))
# print(l3)   

# l1=[12,21,32,4,5,6]
# l2=[32,4,7,8,21,9]
# l=[i for i in l1 if i in l2]
# print(l) 
    
# # 43. Find union of two lists. 
# l1=[12,21,32,4,5,6]
# l2=[32,4,7,8,21,9]
# l=list(set(l1)|set(l2))
# print(l)

# # 44. Count frequency of each element.
# l=[10,20,30,20,30,40,70]
# c=0
# d={}
# for i in l:
#     d[i]=l.count(i)
# print(d)

# # 45. Sort a list without using sort().
# l=[62,25,44,73,12,1]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)
# # 4. Dictionaries / Sets (10 Questions) 
# # 46. Count frequency of elements using dictionary.
# s='siva sankar tati'
# d={}
# for i in s:
#     d[i]=s.count(i)
# print(sorted(d))
 
# # 47. Find common elements between two lists. 
# l1=[10,20,30,40,50,60]
# l2=[20,40,60,70,80,90]
# list=[i for i in l1 if i in l2]
# print(list)

# # 48. Merge two dictionaries.
# d1={'name':'siva sankar','age':18}
# d2={'address':'guntur','salary':25000}
# d3=d1|d2
# print(d3) 

# d1={'name':'siva sankar','age':18}
# d2={'address':'guntur','salary':25000}
# m={**d1,**d2}
# print(m)

# # 49. Invert a dictionary (key ↔ value).
# di={'name': 'siva sankar', 'age': 18, 'address': 'guntur', 'salary': 25000}
# d2={}
# for i,j in di.items():
#     d2[j]=i
# print(d2) 

# # 50. Find unique elements in a list using set.
# l=[1,2,3,3,4,4,4,3,2,2,4,10]
# print(set(l)) 

# # 51. Remove duplicate values in dictionary.
# d={'a':10,'b':20,'c':10,'d':30,'e':20,'f':40}
# d1={}
# values=[]
# for i,j in d.items():
#     if j not in values:
#         d1[i]=j
#         values.append(j)
# print(d1)

# 52. Check if two dictionaries are equal. 
# 53. Sort dictionary by value. 
# 54. Create a dictionary from two lists. 
# 55. Count number of keys with certain value. 
# 5. Loops / Patterns (10 Questions) 
# # 56. Print numbers 1–100.
# for i in range(1,101):
#     print(i,end=" ")
# # 57. Print even numbers 1–50. 
# for i in range(1,51):
#     if i%2==0:
#         print(i,end=" ")
# # 58. Print odd numbers 50–100.
# for i in range(50,100):
#     if i%2!=0:
#         print(i,end=" ") 
# # 59. Print square of numbers 1–10.
# for i in range(1,11):
#     print(i*i,end=" ") 
# # 60. Sum of first n natural numbers.
# s=0
# for i in range(10):
#     s+=i
# print(s)    

# # 61. Print multiplication table.
# n=int(input('enter a number:'))
# for i in range(1,11): 
#     print(n,'*',i,'=',n*i)

# # 62. Reverse a number using while loop.
# n=123456
# temp=n
# k=0
# while temp>0:
#     d=temp%10
#     k=k*10+d
#     temp=temp//10
# print(k) 

# # 63. Print triangle/star pattern. 
# for row in range(1,6):
#     for col in range(1,6):
#         if row==3 or row==1 and col==3 or row==2 and col in [2,4] :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ") 
#     print()
           
# # 64. Print pyramid pattern of numbers.
# n=5
# for row in range(1,n):
#     for space in range(1,n-row+1):
#         print(" ",end=" ")    
#     for col in range(row*2-1):
#         print("*",end=" ")
#     else:
#         print(" ")

# for rows in range(1,n+1):
#     for space in range(1,n-rows+1):
#         print(" ",end="")
#     for cols in range(1,rows+1):
#          print("*",end="")
#     print()  

# 65. Print diamond pattern using stars.
# n=5
# for row in range(1,n):
#     for space in range(1,n-row+1):
#         print(" ",end=" ")    
#     for col in range(row*2-1):
#         print("*",end=" ")
#     else:
#         print(" ")
# for row in range(n,0,-1):
#     for space in range(n-row):
#         print(" ",end=" ")
#     for col in range(row*2-1):
#         print("*",end=" ")
#     else:
#         print(" ")        
 
# 7. OOP / Classes (10 Questions) 
# 66. Create BankAccount class with deposit/withdraw/check balance. 
# # 67. Rectangle class with area & perimeter.
# class Rectangle():
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#     def area(self):
#         print("area of triangle:",self.length*self.breadth)
#     def perimeter(self):
#         print("perimeter of rectangle:",2*(self.length+self.breadth))
# obj=Rectangle(10,5)
# obj.area()
# obj.perimeter()

# class Rect():
#     def area(self,len,bre):
#         print('area:',len*bre)
#     def peri(self,len,bre):
#         print('perimeter:',2*(len+bre))
# obj=Rect()
# obj.area(10,6)
# obj.peri(11,12)
# 68. Circle class with area & circumference. 
# 69. Inheritance: Person → Employee. 
# 70. Implement class method and static method. 
# 71. Encapsulation: private attributes & getters/setters. 
# 72. Polymorphism: method overriding. 
# 73. Operator overloading: add two objects. 
# 74. Implement a simple calculator using class methods. 
# 8. File Handling (10 Questions) 
# 86. Count words, lines, characters in a file. 
# 87. Find longest word in a file. 
# 88. Copy content from one file to another. 
# 89. Remove all vowels from a text file. 
# 90. Count frequency of words in a file. 
# 91. Append text to a file. 
# 92. Read file backwards line by line. 
# 93. Check if file is empty. 

# help('modules')

'password'
import random
a=int(input("no of alphabets:"))
b=int(input("no of integers:"))
c=int(input('no of special characters:'))
a1='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
a2='0123456789'
a3='!@#$%^&*/?'
password=""
for i in range(a):
    k=random.choice(a1)
    password+=k
for i in range(b):
    k=random.choice(a2)
    password+=k
for i in range(c):
    k=random.choice(a3)
    password+=k
print(password)