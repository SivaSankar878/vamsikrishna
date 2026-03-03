
# # create user defined function to find prime numbers between two numbers. 
# def b_p(a,b):
#     l=[]
#     for i in range(a,b):
#         co=0
#         for j in range(2,a):
#             if i%j==0:
#                 co+=1
#         if co==0:
#             l.append(i)
#     print(l)
# b_p(50,60)     

# # create a function to fine the given number factors
# def factors(n):
#     for i in range(1,n):
#         if n%i==0:
#             print(i)
# factors(20)
# factors(40)
# factors(10) 
           
# def lcm(a,b):
#     max1=a if a>b else b
#     for i in range(1,max1):
#         if (max1*i)%a==0 and (max1*i)%b==0:
#            print(max1*i)
#            break
# lcm(10,20)     
# lcm(5,7)  

# # convert integer value into string
# l=156
# k='0123456789'
# tem=''
# while l>0:
#     d=l%10
#     l//=10
#     for i in range(len(k)):
#         if d==i:
#             tem=k[i]+tem
# print(tem,'===',type(tem))            

# k='PyThOn'
# res=''
# for i in k:
#     if ord(i)>=65 and ord(i)<=90:
#         d=ord(i)+32
#         res+=chr(d)
#     elif ord(i)>=97 and ord(i)<=122:
#         d1=ord(i)-32
#         res+=chr(d1)  
# print(res) 


# # 1. Create a user-defined function to convert a string into title case.
# def st_ti_case(s):
#     res=''
#     for i in s:
#         if ord(i)>=65 and ord(i)<=90:
#             d=ord(i)+32
#             res+=chr(d)
#         elif ord(i)>=97 and ord(i)<=122:
#             d1=ord(i)-32
#             res+=chr(d1)
#     print(res)
# st_ti_case('SiVa')
# st_ti_case('saNkaR') 

# # 2. Create a user-defined function to generate the Fibonacci series.
# def fibo(n):
#     a=1
#     b=1
#     for i in range(1,n-1):
#         a,b=b+a,a
#     print(a)    
# fibo(8)
# fibo(10)

# # 3. Create a user-defined function to print palindrome numbers between a given range.
# def pal_bet_range(s,e):
#     for i in range(s,e):
#         if i>10 and str(i)==str(i)[::-1]:
#             print(i)
# pal_bet_range(1,100)
# pal_bet_range(101,200)

# # 4. Create a user-defined function to print Armstrong numbers between a given range.
# def ar_b_r(a,b):
#     for i in range(a,b):
#         l=0
#         s=str(i)
#         for j in s:
#             l+=int(j)**len(s)
#         if i==l:
#             print(i)
# ar_b_r(200,1000)                

# # 5. Create a user-defined function to find the LCM of two numbers.
# def lcm(a,b):
#     k=a if a>b else b
#     for i in range(k,(a*b)+1):
#         if i%a==0 and i%b==0:
#             print(i)
#             break
# lcm(20,30) 
# lcm(7,5)
           
# # 6. Create a user-defined function to find the GCD (Greatest Common Divisor) of two numbers.
# def gcd(a,b):
#     k=a if a<b else b
#     for i in range(k,0,-1):
#         if a%i==0 and b%i==0:
#             print(i)
#             break
# gcd(10,20)
# gcd(60,120) 
# gcd(3,5)     

# n=1333884
# while n>=9:
#     sum=0
#     while n>0:
#         d=n%10
#         n=n//10
#         sum+=d
#     n=sum
# print(n)     

# def calci():
#     while True:
#         print("1.addition")
#         print("2.subtraction")
#         print("3:multiplcation")
#         print("4:modulus")
#         print("5:exit")
#         a=int(input("enter the first value:"))
#         b=int(input("enter the second value:"))
#         c=int(input("enter a choice from 1-5:"))
#         if c==1:
#             print(a+b) 
#         elif c==2:
#             print(a-b)
#         elif c==3:
#             print(a*b)
#         elif c==4:
#             print(a%b)
#         elif c==5:
#             exit     
#         else:
#             print("Invalid option please select from 1-5")       
# calci()        

# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     else:
#         return True  
# n=int(input("enter a number:"))
# high=n
# low=n       
# while True:
#     if is_prime(high):
#         print(high)
#         break
#     if is_prime(low):
#         print(low)
#         break
#     high+=1
#     low-=1  
# print(n)  



# def sum(n):
#     while n>9:
#         sum=0
#         while n>0:
#             d=n%10
#             n=n//10
#             sum+=d
#         n=sum
#     return n    
# n=int(input("enter a number:"))        
# print(sum(n)) 
           

