#1. Check whether a given number is an Armstrong number.
# n=int(input("enter a number:"))
# s=str(n)
# l=len(s)
# result=0
# for i in s:
#     result+=int(i)**l
# if n==result:
#     print("armstrong number")
# else:
#     print("not armstrong number")      
# print()
#2. Print all the factors of a given number N.
# k=int(input("enter a number:"))
# for i in range(1,k):
#     if k%i==0:
#         print(i)
# print()
#3. Find the factorial of a given number N.
# t=int(input("enter a number:"))
# sum=1
# for i in range(1,t+1):
#     sum*=i
# print(sum)    

#4.Count the number of digits in a given integer N.
integer=int(input("enter a number:"))
s1=str(integer)
l1=len(s1)
count=0
for i in s1:
    count+=1
print(count)    