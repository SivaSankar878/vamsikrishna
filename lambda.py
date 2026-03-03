# #these are the some arthematical operations done by lambda functions
# add=lambda a,b:a+b
# print(add(10,20))

# sub=lambda a,b:a-b
# print(sub(50,28))

# mul=lambda a,b:a*b
# print(mul(10,5))

# div=lambda a,b:a/b
# print(div(100,4))

# mod=lambda a,b:a%b
# print(mod(105,7))


# from functools import reduce
# l=[10,21,34,57,78,39]
# k=list(filter(lambda a:a%2==0,l))
# print(k)
# m=list(map(lambda a:a+2,k))
# print(m)
# r=reduce(lambda a,b:a+b ,m)
# print(r)

# #importing  functions ,variables,class

# from Exam import even_check
# even_check()

# import Exam
# Exam.even_check()

# from Exam import A
# obj=A()
# obj.even_check()

# from functools import reduce
# n=[1,2,3,4,5]
# l=reduce(lambda x,y:x+y ,n)
# print(l)

# l=[1,2,3,4,5,6]
# k=list(map(lambda x:x**2,l))
# print(k)

# l=[1,2,3,4,5,6]
# k=list(filter(lambda x:x%2==0,l))
# print(k)

# import time
# def loop_time(h):
#     def inner():
#         s_t=time.time()
#         h()
#         e_t=time.time()
#         print('time:',e_t-s_t)
#     return inner

# @loop_time
# def n():
#     for i in range(10):
#         print(i)
# n()
# def even_check(c):
#     def inner(a,b):
#         for i in range(a,b):
#             if i%2==0:
#                    print(i)
#     return inner
# @even_check
# def check(a,b):
#     for i in range(a,b):
        
#             print(i)
# check(20,30)

# def login_process(k):
#     def inner(j):
#         if j=='siva':
#             k(j)
#         else:
#             print('invalid username')
#     return inner

# @login_process
# def login(u):
#     print('welcome to 10k coders',u)
# login('siva')
# login('sai')


# def table(s):
#     def inner(m):
#         s(m) 
#     return inner
# @table
# def t(k):
#     for i in range(1,11):
#        if i%2==0:
#          print(k,'*',i,'=',k*i)
# t(3)

# def prime_check(a):
#     def inner(d):
#         c=0
#         for i in range(2,d):
#             if d%i==0:
#                 c+=1
#         if c==0:
#             print("Prime",end=",") 
#         else:
#             print('not prime',end=" ") 
#         a(d)
#     return inner
# @prime_check
# def prime(n):
#     print('The number is',n)
# prime(11)

# def outer(fun):
#     def inner(d,e):
#         fun(d,e)
#         for i in range(d,e):
#             c=0
#             for j in range(2,i):
#                 if i%j==0:
#                     c+=1
#             if c==0:
#                 print(i,end=" ")
#         print("\n")
#     return inner
# @outer
# def prime(a,b):
#     print(f"The prime numbers between the range of {a} and {b} is:",end=" ")
# prime(10,20)
# prime(30,40)
# prime(40,50)


# n=int(input("enter a number:"))
# l=[]
# for i in range(2,50):
#     c=0
#     for j in range(2,i):
#         if i%j==0:
#             c+=1
#     if c==0:
#         l.append(i)
#     if len(l)==n:
#         print(l)
#         break
        

# a=int(input("enter number a:"))
# b=int(input("enter number b:"))
# k=a if a>b else b
# for i in range(k,a*b+1):
#     if (i%a)==0 and (i%b)==0:
#         print(i)


# a=int(input("enter number a:"))
# b=int(input("enter number b:"))
# k=a if a<b else b
# t=[]
# for i in range(1,k):
#     if (a%i)==0 and (b%i)==0:
#         t.append(i)
# print(t[-1])


# st1=''
# st2=0
# s='abc3'
# for i in s:
#     if ord(i)>=65 and ord(i)<=90 or ord(i)>=97 and ord(i)<=120:
#         st1+=i
#     elif ord(i)>=48 and ord(i)<=57:
#         st2=ord(i)-48
#     else:
#         continue
# print(st1)
# print(type(st1))
# print(st2)
# print(type(st2))
# print(st1*st2)

# l=[1,2,5]
# s=[]
# for i in range(len(l)):
#     t=0
#     for j in range(len(l)):
#         if i!=j:
#             t+=l[j]
#     s.append(t) 
# print(s)

def ClimbingStairs(n):
    if n==1:
        return 1
    if n==2:
        return 2
    return ClimbingStairs(n-1)+ClimbingStairs(n-2)
print(ClimbingStairs(5))