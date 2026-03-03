# #using while loop rverese a number
# n=456
# temp=0
# while n!=0: #checking while loop condition
#     d=n%10  #in this step by using the modulus, it gives 6 
#     n//=10  #using floor division the value is 45
#     temp=temp*10+d #6 can be added to temp
# print(temp)  
# print() 
#  
# # print fibonacci series up to n terms using while
# a,b=0,1
# for i in range(5):
#     a,b=b,a+1
# print(a)

#perfect number
# n=28
# t=0
# for i in range(1,n):
#     if n%i==0:
#        t+=i
# if n==t:         
#     print("perfect number",t)     
# else:
#     print("not a perfect number")

#find the length of the number
# n=123213
# s=str(n)
# k=0
# for i in s:
#     k+=1 
# print(k)   
 
#without coverting a number into string find the length of the number
# n=int(input("enter a number:"))
# count=0
# while n!=0:
#     n=n//10
#     count+=1
# print(count)  

#reverse a integer without converting into string   
# n=int(input("enter a number:"))
# t=0
# while n!=0:
#     d=n%10
#     t=t*10+d
#     n=n//10
# print(t)   
     
#print even numbers addition and odd number addition 
# n=int(input("enter a number:"))
# even=0
# odd=0
# while n!=0:
#     d=n%10
#     n=n//10
#     if d%2==0:
#         even+=d
#     else:
#         odd+=d    
# print("even sum:",even)
# print("odd sum:",odd)

#prime number
# n=int(input("enter a number:"))
# fact=0
# for i in range(1,n+1):
#     if n%i==0:
#         fact+=1
# if fact==2:
#     print("prime number",n)   
# else:
#     print("not a prime number")

# sum of prime numbers in a integer using while loop 
n=int(input("enter a number:"))
sum=0
while n!=0:
    d=n%10
    n=n//10
    if d>0:
        cou=0
        for i in range (1,d+1):
            if d%i==0:
                cou+=1
        if cou==2:
            sum+=d
print(sum) 
