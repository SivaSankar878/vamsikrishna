# we want to print the patterns by using for loop.
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i,end=" ")
#     print()     
# print()
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(j,end=" ")
#     print()
# print()
# for i in range(n,0,-1):
#     for j in range(1,n+1):
#         print(i,end=" ")
#     print()
# print()      
# for i in range(1,n+1):
#     for j in range(n,0,-1):
#         print(j,end=" ")
#     print()
# print()     

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j==3 or i==3:
#             print("?",end=" ")
#         else:
#             print(" ",end=" ")    
#     print()         
# print()    

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j==1 or i==1 or i==5 or j==5:
#             print("?",end=" ")
#         else:
#             print(" ",end=" ")    
#     print()         
# print() 
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==j or i==1 and j==5 or i==2 and j==4 or i==4 and j==2 or i==5 and j==1:
#             print("",end=" ")
#         else:
#             print(" ",end=" ")    
#     print()         
# print()   
# n=5    
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==j or i+j==n+1:
#             print("?",end=" ")
#         else:
#             print(" ",end=" ")    
#     print()         
# print() 
# s="programming"
# l=[]
# d=[]
# for i in s:
#     if i not in l:
#         l.append(i)  
#     else:
#         d.append(i)      
# print(d) 
    
# s='siva sankar'
# co=0
# for i in s:
#     if i in 'aeiouAEIOU':
#         co+=1
# print(co)
       
# s='programming'
# t=''
# for i in s:
#      t=i+t
# print(t) 
    
# s='programming'
# t=''
# for i in s:
#      t=i+t
# if s==t:
#      print(s,"palindrome",t)
# else:
#      print(s,"is not a palindrome",t)   
  
# k="string programming"
# t=[]
# for i in k:
#     if i not in t:
#         co=0
#         for j in k:
#             if i==j:
#                 co+=1
#         print(i,'=',co)
#         t.append(i)  
 
# s=input()
# t=s.title()         
# print(t)

# s="aaabbcccdddaaass"
# t=[]
# for ch in s:
#     if ch not in t:
#         t.append(ch)  
# print(t)

# s='Find the longest word in a given sentence'
# l=0
# k=''
# for ch in s.split():
#     if len(ch)>l:  
#         k=ch
# print(k,'=',len(ch))      

# s='Find the longest word in a given sentence'
# k=s.replace(" ","-")
# print(k) 

# s='abc123'
# co=0
# for i in s:
#     if i.isdigit():
#         co+=1
# print(co)

# s="a1b2c3"
# l=''
# d=''
# for i in s:
#     if i.isdigit():
#         d+=i
#     else:
#         l+=i
# print(l)  
# print(d,end=" ")          

# s="a1b2c3"
# print(s.isalphanumeric())

# marks = {"Rahul": 85, "Anita": 92, "Kiran": 78, "Sita": 95}
# max_value = max(marks.values())
# print( max_value)

# 3. Write a Python program to create a dictionary where alphabets are keys and their ASCII values are values.
# l=['a','b','c']
# tem={}
# for i in l:
#     tem[i]=ord(i)
# print(tem)    

# 4. Write a Python program to create a dictionary of numbers from 1 to 10 with their squares, but include only those numbers whose square is greater than 10.
# k=[6,7,8,9,10]
# tem={}
# for i in k:
#     tem[i]=i*i
# print(tem) 
   
# print(ord('@'))
# print(ord('#'))
# print(ord('$'))
# print(ord('%'))
# print(ord('&'))
# print(ord('*'))

# n=125
# while n>=0:
#     print(chr(n),n)
#     n-=1

# 1.   for x in range(2,2):
#               print(x) 

# for i in range(2,2):
#     print(i)
# 2. Print numbers 5 4 3 2 1 using loop 
# n=5
# for i in range(n,0,-1):
#     print(i,end=" ")
# n=5
# while n>0:
#     print(n,end=" ")
#     n-=1

# 3. Print prime number between 10 to 100 using while loop 
# s=10
# e=100
# k=[]
# while s<e:
#     cou=0
#     for i in range(1,s):
#         if s%i==0:
#             cou+=1
#     if cou==1:
#             k.append(s) 
#     s+=1           
# print(k)

# 4. Check given number perfect or not using while loop.
# n = 28
# i = 1
# cou = 0
# while i < n:
#     if n % i == 0:  
#         cou += i
#     i += 1
# if cou==n:
#     print('perfect')
# else:
#     print('not perfect')    
