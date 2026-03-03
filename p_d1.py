# # 1.	Write a list comprehension to generate numbers from 0 to 9.
# l=[i for i in range(0,10)]
# print(l)

# # 2.	Generate a list of squares of numbers from 1 to 10.
# l=[i*i for i in range(1,11)]
# print(l)

# # 3.	Create a list of even numbers from 1 to 20.
# l=[i for i in range(1,21) if i%2==0]
# print(l)

# # 4.	Extract each character from the string "python" using list comprehension.
# k='python'
# l=[i for i in k]
# print(l)

# # 5.	Convert all characters of "python" to uppercase using list comprehension.
# k='python'
# l=[i.upper() for i in k]
# print(l)

# # 6.	Generate all numbers between 1 and 20 that are multiples of 3 or 5.
# l=[i for i in range(1,21) if i%3==0 and i%5==0]
# print(l)

# # 7.	Create a list of squares of odd numbers between 1 and 15.
# l= [i*i for i in range(1,16) if i%2!=0]
# print(l)

# # 8.	Generate all numbers between 50 and 100 that end with digit 5.
# l=[i for i in range(50,101) if i%10==5]
# print(l)

# # 9.	Reverse each word in the list ["apple", "banana", "cherry"].
# l=["apple", "banana", "cherry"]
# l1=[i[::-1] for i in l]
# print(l1)

# # 10.	Remove all zeros from the list [10, 0, 20, 30, 0, 40].
# l=[10, 0, 20, 30, 0, 40]
# for i in l:
#     if i==0:
#         l.remove(i)
# print(l)   
     
# # 11.	Create all pairwise sums of [1,2,3] and [10,20,30] using list comprehension.
# l=[1,2,3]
# k=[10,20,30]
# s=[a+b for a,b in zip(l,k)]
# print(s)

# # 12.	Generate a 3×3 matrix using nested list comprehension.
# matrix=[[3*i+j for j in range(1,4)] for i in range(3)]
# print(matrix)

# # 13.	Flatten the list [[1,2,3],[4,5],[6]] using list comprehension.
# l=[[1,2,3],[4,5],[6]]
# for i in l:  
#     for j in i:
#         print(j,end=' ')

# # 14.	Generate a list of squares for even numbers and cubes for odd numbers from 1–10.
# l=[i**2 if i%2==0 else  i**3 for i in range(1,11) ]
# print(l)

# # 15.	Create a multiplication table (1–3 × 1–3) using nested list comprehension.
# table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
# print(table)

# # 16.	Extract vowels from the string "Python".
# s='python'
# v='aeiou'
# s1=''
# for i in s:
#     if i not in v:
#         s1+=i
# print(s1)        

# # 17.	Generate a list of ASCII values for the string "ABC".
# s='ABC'
# for i in s:
#     print(ord(i))

# # 18.	Generate uppercase alphabets A–Z using list comprehension.
# l=[chr(i) for i in range(65,92)]
# print(l)

# # 19.	Capitalize every word in "hello world python".
# s="hello world python".split()
# for i in s:
#     k=i.capitalize()
#     print(k,end=" ")    

# # 20.	Print "Even" or "Odd" for numbers 1–10 using list comprehension.
# l=['Even' if i%2==0 else 'Odd' for i in range(1,11)]
# print(l)

# # 21.	Find the length of each word in ["Ajay","Python","Django"].
# s=["Ajay","Python","Django"]
# l=[len(i) for i in s]
# print(l)

# 22.	Extract file extensions from ["data.csv","report.pdf","image.png"].
# # 23.	Create a dictionary where keys are numbers 1–5 and values are their squares.
# d={}
# for i in range(1,6):
#     d[i]=i*i
# print(d)

# # 24.	Map characters of "ABC" to their ASCII values using dictionary comprehension.
# l='ABC'
# d={}
# for i in l:
#     d[i]=ord(i)
# print(d) 

# # 25.	Combine ['a','b','c'] and [1,2,3] into a dictionary using comprehension.
# k=['a','b','c']
# s=[1,2,3]
# d={}
# for i,j in zip(k,s):
#     d[i]=j
# print(d)    

# # 26.	Generate all prime numbers between 1 and 100 using list comprehension.
# l=[i for i in range(2,100) if len([j for j in range(2,i) if i%j==0])==0]
# print(l)

# # 27.	Create all possible pairs (x, y) from [1,2,3] and [3,1,4] where x ≠ y.
# x=[1,2,3]
# y=[3,1,4]
# k=[]
# for i in x:
#     for j in y:
#         if i!=j:
#             print((i,j))

# # 28.	Generate palindrome numbers between 1 and 100.
# l=[i for i in range(1,101) if str(i)==str(i)[::-1]]
# print(l)

# # 29.	Add elements from two lists [1,2,3] and [10,20,30] using list comprehension.
# a=[1,2,3]
# b=[10,20,30]
# l=[i+j for i,j in zip(a,b)]
# print(l)

# # 30.	Extract all student names from [{'name':'Ajay','marks':80},{'name':'Riya','marks':90}].
# l=[{'name':'Ajay','marks':80},{'name':'Riya','marks':90}]
# k=[i['name'] for i in l]
# print(k)

# # 31.	Generate all palindromic numbers between 1 and 1000.
# l=[i for i in range(1,1001) if str(i)==str(i)[::-1]]
# print(l)

# # 32.	Get all words starting with 'a' from ['apple','ant','banana','ball'].
# l=['apple','ant','banana','ball']
# k=[i for i in l if i.startswith('a') ]
# print(k)

# # 33.	Generate numbers between 1 and 20 that are divisible by 2 or 3. 
# l=[i for i in range(1,21) if i%2==0 or i%3==0]
# print(l)

# # 34.	Generate all coordinate pairs [x, y] where x and y range from 0 to 2.
# co=[(i,j) for i in range(3) for j in range(3)]
# print(co)