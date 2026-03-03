# # 1) Write a Python program to find the sum of prime digits in a given number.
# # Example: n = 35271 → prime digits are 3, 5, 7 → sum = 15.
# n=int(input("enter a number:"))
# sum=0
# while n!=0:
#     d=n%10
#     n=n//10
#     if d>0:
#         cou=0
#         for i in range (1,d+1):
#             if d%i==0:
#                 cou+=1
#         if cou==2:
#             sum+=d
# print(sum) 

# # 2) Write a Python program to calculate the sum of even digits in a given number.
# # Example: n = 48269 → even digits are 4, 8, 2, 6 → sum = 20.
# n=int(input("enter a number:"))
# te=0
# while n!=0:
#     d=n%10
#     n=n//10
#     if d%2==0:
#         te+=d
# print(te)        
# # 3) Write a program to print whether the sum of even digits in a number is odd or even.
# # Example: n = 92641 → even digits are 2, 6, 4 → sum = 12 → output: "Even".
# n=int(input("enter a number:"))
# te=0
# while n!=0:
#     d=n%10
#     n=n//10
#     if d%2==0:
#         te+=d
# if te%2==0:
#     print("even")
# else:
#     print("odd")


# 1.	Find the sum of elements in a list (without using sum()).
# list1=[1,2,3,4,5,6,7,8,9,10]
# sum=0
# for i in list1:
#     sum+=1
# print(sum)    


# 2.	Count the frequency of each element in a list.
# list2=[1,1,2,3,4,5,4,6,7,10]
# count=0
# li3=[]
# for i in list2:
#     if i in li3:
#         count+=1
#     else:
#         count=1
#     print(i,'=',count) 

# list2 = [1, 1, 2, 3, 4, 5, 4, 6, 7, 10]
# for i in set(list2):
#     print(i, "=", list2.count(i))
               

# 3.Remove duplicates from a list.
# li=[10,20,30,20,30,40,50]
# l2=[]
# for i in li:
#     if i not in l2:
#         l2+=[i]
# print(l2)      

# li=[10,20,30,20,30,40,50]
# l2=[]
# for i in li:
#     if i not in l2:
#         l2.append(i)
# print(l2)   

# 4.  Merge two lists into one. Without using + and
# Extend  method() in python
# t=[]
# list1=[1,2,3,4,5,6,7,8,9,10]
# list2=[1,1,2,3,4,5,4,6,7,10]
# for i in list1:
#     t.append(i)
# for i in list2:     
#     t.append(i)
# print(t)


# 1.Reverse the lists without using list methods.
# j=[100,'indu',200,300,'python']
# t=[]
# for x in j:
#     t=[x]+t
# print(t)
# 2.Finding second maximum element.
# s=[100,200,1000,200,500,200]
# m1,m2=0,0
# for x in s:
#     if x>m1:
#         m2=m1
#         m1=x
#     elif m2<x<m1:
#         m2=x
# 3.Matching element in a list.(attempts=2)
# j=['indu','100','0123456789','kbhp']
# for i in range(2):
#      n=input("Enter:")
#      if n in j:
#          print("Found,The list is:",j)
#          break
#      else:
#          print("Not found")
# else:
#      j.clear()
#      print("Attempts are over,List is deleted")

# 4.Bubble sort Asc order
# n=[10,50,5,7,43,51]
# for i in range(len(n)):
#     for j in range(len(n)):
#         if n[i]<n[j]:
#             n[i],n[j]=n[j],n[i]
# print(n)            
# 5.bubble sort desc order
# n=[10,50,5,7,43,51]
# for i in range(len(n)):
#     for j in range (len(n)):
#         if n[i]>n[j]:
#             n[i],n[j]=n[j],n[i]
# print(n)
# 6.add 20 to the even number   
# d=[10,20,15,11,7]
# for i in range(len(d)):
#     if d[i]%2==0:
#         d[i]=d[i] +20
# print(d)     

#7.add 20 to the number if it is prime.
# n=[10,50,5,7,43,51]
# for i in range(len(n)):
#     co=0
#     for j in range(2,n[i]):
#         if n[i]%j==0:
#             break
#     else:    
#         n[i]+=20
# print(n)            

# t=[2,5,6,7,8,3,4]
# k=10
# for i in range(len(t)):
#     for j in range(i+1,len(t)):
#         if t[i]+t[j]==k:
#             print(t[i],"+",t[j],"=",t[i]+t[j])     

# l=[1,0,1,0,1,0,1,0,1,0]              
# for i in range(len(l)):
#     for j in range(len(l)):
#         if l[i]<=l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)  

# l=[1,0,1,0,1,0,1,0,1,0]              
# for i in range(len(l)):
#     for j in range(len(l)):
#         if l[i]>=l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)

# l=[10,20,20,30,40,30,70,10]
# t=[]
# for i in l:
#     cou=0
#     if i not in t:
#         t.append(i)
#         for j in l:    
#             if i == j:
#                 cou+=1
#         print(i,"=",cou)  
# print()

# l = [10, 20, 20, 30, 40, 30, 70, 10]
# t = []   

# for num in l:
#     if num not in t:  
#         t.append(num)
#         count = 0
#         for x in l:
#             if x == num:
#                 count += 1
#         print(num, "=", count)


   
