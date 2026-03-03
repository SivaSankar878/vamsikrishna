# #1. Write a program to find the Highest Common Factor (HCF) of two numbers.
# def hcf(a,b):
#     k=a if a<b else b
#     for i in range(k,0,-1):
#         if a%i==0 and b%i==0:
#             print(i)
#             break
# hcf(6,10)        

# #2. Check whether a number is prime using list comprehension.
# m=int(input("enter a number:"))
# k=["prime" if len([j for j in range(2,m) if m%j==0])==0
#    else "not prime"]
# print(k)

# #3. Write a program to print the nearest prime number to a given number.
# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     else:
#         return True
# n=int(input())     
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


# #4. Print the first 9 prime numbers in serial order.
# l=[i for i in range(2,100) if len([j for j in range(2,i) if i%j==0])==0]
# print(l[:9])

# #5. Using the setdefault() method, count the frequency of each character in a given string.
# s=input("enter a string:")
# freq={}
# for i in s:
#     freq.setdefault(i,0)
#     freq[i]+=1
# print(freq)    

# #6. Print each letter of the alphabet in order, and if the letter is a vowel and also a prime-numbered position in the alphabet, highlight it.
# k=[]
# v=['A','E','I','O','U']
# l=[ i for i in range (2,27) if len([j for j in range(2,i) if i%j==0])==0]
# for m in range(65,91):
#         k.append(chr(m))
# for i,j in enumerate(k,start=1):
#      if j in v and i in l:
#             print("*",end=" ")
#      else:
#             print(j,end=" ")       
    

# #7. Sort a list without using the built-in sort() method.
# l=[103,90,76,354,980,81,9,30]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)  


# def bank():
#     a=1000
#     def de_amo():
#         nonlocal a
#         d_a=int(input("eneter deposit amount:"))
#         a=a+d_a
#         print('amount should be deposited, your current balance is:',a)
#     def wi_amo():
#         nonlocal a
#         wi_amo=int(input("enter withdrawal amount:")) 
#         if wi_amo>a:
#             print('you have lesser amount than withdraw amount')
#         else:    
#             a=a-wi_amo
#             print('amount should be withdraw, your current balance is:',a)
#     def che_bal():
#         print('your current balance is:',a)

#     while True:
#         print("1.deposit\n2.withdraw\n3.check balance\n4.exit")
#         ch=int(input("enter your choice:"))
#         if ch==1:
#             de_amo()
#         elif ch==2:
#             wi_amo()
#         elif ch==3:
#             che_bal()
#         elif ch==4:
#             print('thankyou for banking with us....')
#             break
#         else:
#             print('please select your choice')
# bank()


