# j='python developer'.split()
# l=[len(i) for i in j ]
# print(l)

# l=[2*i for i in range(1,11)]
# print(l)

# n=10
# l=[ [i] for i in range(1,n) if n%i==0]
# print(l)

# a=[10,20,30]
# b=[100,200,300]
# l=[(i+j) for i,j in zip(a,b)] 
# print(l)

# 1.Flatten a 2D list into a 1D list using list comprehension.
# l=[[1,2,3],[4,5,6],[7,8,9]]
# f=[j for i in l for j in i]
# print(f)

# 2.Extract all digits from a given string. s = "abc123def456"
# s="abc123def456"
# t=''
# for i in s:
#     if i.isdigit():
#         continue
#     else:
#         t+=i
# print(t)

# s="abc123def456"
# l=[i for i in s if i.isdigit()]
# print(''.join(l))      
# k=[i for i in s if i.isalpha()]  
# print(''.join(k))

# 3.Create a list of all numbers from 1–100 that are divisible by both 3 and 5.
# s=int(input())
# e=int(input())
# l=[]
# for i in range(s,e):
#     if i%3==0 and i%5==0:
#         l.append(i)
# print(l)   

# using list comprehension
# s=int(input())
# e=int(input())
# n=[i for i in range(s,e) if i%3==0 and i%5==0]
# print(n)

# 4.Build a list of tuples (number, square) for numbers from 1–10.
# s=int(input())
# e=int(input())
# l=[]
# for i in range(s,e):
#     l.append((i,i*i))
# print(l)    

# 5.Print prime numbers between 10 to 50 using list comprehension ?
# s=int(input())
# e=int(input())
# p=[i for i in range(s,e) if len([j for j in range(3,i) if i%j==0])==0]
# print(p)

# a=['java','python','c++']
# b=['html','css','java script']
# k={i:j for i,j in zip(a,b)}
# print(k)

# m=[1,2,3,2,1,6,9,6,8,6]
# k={i for i in m if i%2==0}
# print(k)

# 1) Write a list comprehension in Python that checks whether each number in a given list is "prime" or "not prime" and returns the result as a list.
# n=[1, 2, 3, 4, 5, 16, 17, 19, 20]
# l=["prime" if len([i for i in range(1,j+1) if j%i==0])==2
#    else "not prime"
#    for j in n]
# print(l)


# 2)  Using list comprehension, generate a 2D list with the following structure
# input=[[1,2,3],[4,5,6],[7,8,9]] ==> output=[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
# input=[[1,2,3],[4,5,6],[7,8,9]]
# output=[[row[i] for row in input] for i in range(len(input[0]))]
# print(output)

# 3)  Using list comprehension, generate a list of tuples mapping ASCII values to characters for uppercase letters A, B, C.
# l=['A','B','C','D']
# K=[(i,ord(i)) for i in l]
# print(K)

# k=[i for i in range(10,30) if all(i%j!=0 for j in range(2,i))]
# print(k)

# m=11
# l=[i for i in range(1,m) if m%i==0]
# if len(l)==1:
#     print("prime")
# else:
#     print("not prime")    

# r=[10,11,12,13,14]
# k=["even" if i%2==0
#    else "odd"
#     for i in r ]
# print(k)

# k=[[1,2],[3,4],[5,6],[7,8],[9,10]]
# for i in k:
#     for j in i:
#         if j%2!=0:
#             print(j)

# k=[[1,2],[3,4],[5,6],[7,8],[9,10]]
# l=[j for i in k for j in i if j%2!=0]
# print(l)            

# r=['python','java','c++']
# k=[j for i in r for j in i if j in 'AEIOUaeiou']
# print(k)

# k=[[1,2,3],[4,5,6],[7,8,9]]

# r=[[x,y] for x,y in enumerate(range(1,10))]
# print(r)

# r=[i for i in range(1,11)]
# print(r)

# r=tuple(i for i in range(1,11))
# print(r)

# 1.	Write a Python program to print all palindrome numbers between two given numbers.
# k=[i for i in range(100,120) if str(i)==str(i)[::-1]]
# print(k)

# 2.	Write a Python program to print all Armstrong numbers between two given numbers.
# k=[i for i in range(10,10000) if i== sum(int(j)** len(str(i)) for j in str(i)) ]
# print(k)

        
# 3.   	input=[11,12,13,15,16,19]===    output=[‘prime’,notprime,’prime’,’notprime’,’notprime’,’prime’]  using list comprehension.
# t=[11,12,13,15,16,19]
# k=["prime"  if len([j for j in range(1,i) if i%j==0])==1 
#    else "not prime" for i in t]
# print(k)

# 4.	write python program to check given strings are anagram or not
# k='listen'
# m='silent'
# if len(k)==len(m):
#     if sorted(k)==sorted(m):
#             print("anagram")
#     else:
#          print("not  a  angarm")         
# else:
#     print("not  a  angarm")      

#by using the list comprehension 
# k='listen'
# m='silent'
# l=["anagram" if len(k)== len(m) and sorted(k)==sorted(m) else "not anaram"]
# print(l)

# 5.  	Write a Python program to print the first n prime numbers.
# k=[i for i in range(10,100) if len([ j for j in range(1,i) if  i%j==0])==1]
# print(k)

# 6.	write a python program to check given number prime or not using list comprehension.
# m=9
# k=["prime" if len([j for j in range(1,m) if m%j==0])==1
#    else "not prime"]
# print(k)

# 7.	Write a Python program to reverse a string by swapping characters (without using loops or built-in reverse functions, slicing ).
# k='string'
# y=''
# for i in k:
#     y=i+y
# print(y)