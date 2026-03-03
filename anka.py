# #factorial of a number
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# n=int(input())
# print(f"the factorial of {n}is {factorial(n)}")  
# print()

# #fibonacci series
# def fibonacci(n):
#     if n<=1:
#         return n
#     else:
#         return  fibonacci(n-1)+fibonacci(n-2)
# n=int(input())
# #for i in range(n):
# print(fibonacci(n),end=" ") 
# print()

# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
# n=int(input())
# if is_prime(n):
#     print(f"{n} is a prime number")   
# else:
#     print(f"{n} is not a prime number")
# print() 

# def maximum(arr):
#     t=max(arr)
#     return t
# arr=list(map(float,input().strip().split()))
# print(maximum(arr))
# print()

# #moving hash to the front
# def hash(s,length):
#     count=s.count("#")
#     s=s.replace("#","")
#     s="#"*count+s
#     return s
# s=input()
# length=len(s)
# print(hash(s,length))
# print()

# #prime number check
# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
# n=int(input())
# if is_prime(n):
#     print(f"{n} is a prime number") 
# else:        
#     print(f"{n} not a prime number")    
# print()  

# # sum of perfect numbers
# def is_perfect(n):
#     sum=0
#     for i in range(1,n):
#         if n%i==0:
#             sum+=i
#     return sum ==n       
# st=int(input("enter the starting number:")) 
# en=int(input("enter the ending number:"))
# t=0
# print(f"perfect number between {st} and {en} is")
# for i in range(st,en+1):
#        if is_perfect(i):
#           print(i) 
#           t+=i
# print("sum of perfect numbers:",t)

# #perfect number
# def perfect(n):
#     sum=0
#     for i in range(1,int(n/2)+1):
#         if n%i==0:
#             sum+=1
#         return sum
# n=int(input("enter the number:"))        
# if perfect(n):
#     print(f"{n} is a perfect number")
# else:
#     print(f"{n} not a pefect number") 
# print()

# #sum of prime numbers
# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
# s=int(input())
# e=int(input())
# t=0
# print(f"prime number between {s} and {e} is:")
# for i in range(s,e+1):
#     if is_prime(i):
#         print(i)
#         t+=i
# print("sum of prime numbers is:",t)   
# #This code is for finding the numbers of pairs whose sum = target 
# list1=[int(i) for i in input().split()]
# targ=int(input())
# def countPairs(l,k):
#     count=0
#     for i in range(0,len(l)):
#         for j in range(0,len(l)):
#             if(i!=j and l[i]+l[j]==k):
#                 count+=1/2
#     print(count)
# countPairs(list1,targ)             
 