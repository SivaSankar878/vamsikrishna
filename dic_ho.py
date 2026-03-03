#1.Square of Numbers
# Create a dictionary of numbers and their squares from 1 to 5
# Expected Output:{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# l={i:i*i for i in range(1,6)}
# print(l)

#2.Filter Even Numbers
# Create a dictionary with numbers 1 to 10 as keys and their squares as values, but only for even numbers
# Expected Output:{2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# l={i:i*i for i in range(1,11) if i%2==0}
# print(l)

#3.Character Count from String
# Given a string "success", create a dictionary of each character and its frequency
# Expected Output:{'s': 3, 'u': 1, 'c': 2, 'e': 1}

# s='success'
# tem={}
# co=0
# for i in s:
#     if i not in tem:
#         co=1
#         tem[i]=co
#     else:
#         co+=1
#         tem[i]=co   
# print(tem)                   
           
#4.Create Dictionary from Two Lists Given two lists: keys = ['a', 'b', 'c'],values = [1, 2, 3]
# Create a dictionary using comprehension Expected Output: {'a': 1, 'b': 2, 'c': 3}

# keys = ['a', 'b', 'c']
# values = [1, 2, 3]
# tem={}
# for i,j in zip(keys,values): 
#         tem[i]=j
# print(tem)   

# keys = ['a', 'b', 'c']
# values = [1, 2, 3]
# l={i:j for i,j in zip(keys,values)}     
# print(l)

#5.Invert Keys and Values Given dictionary: d = {'x': 10, 'y': 20, 'z': 30}
# Create a new dictionary where keys and values are swapped
# Expected Output: {10: 'x', 20: 'y', 30: 'z'}

# d = {'x': 10, 'y': 20, 'z': 30}
# t={}
# for keys,values in d.items():
#     t[values]=keys
# print(t)    

#6.Conditional Dictionary with Squares > 10
# Create a dictionary of numbers 1 to 10 with their squares, but include only those where the square is greater than 10
# Expected Output:{4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

# t={i:i*i for i in range(1,11) if i*i>10}
# print(t)

#7.Uppercase Keys
# Given list:letters = ['a', 'b', 'c']
# Create a dictionary with uppercase letters as keys and their ASCII values as values
# Expected Output:{'A': 65, 'B': 66, 'C': 67}

# l = ['a','b','c']
# t={}
# for i in l:
#     t[i.upper()]=ord(i.upper())
# print(t)    

#8.Dictionary with Odd/Even Labels
# Create a dictionary for numbers 1 to 5, where the value is "even" if the number is even, and "odd" if the number is odd
# Expected Output: {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}

# t={}
# for i in range(1,6):
#     if i%2==0:
#         t[i]='even'
#     else:
#         t[i]="odd"
# print(t)

#9.Count Length of Words
# Given a list of words:words = ["apple", "banana", "kiwi"]
# Create a dictionary with words as keys and their lengths as values
# Expected Output:{'apple': 5, 'banana': 6, 'kiwi': 4}

# w= ["apple", "banana", "kiwi"]
# t={}
# for i in w:
#     t[i]=len(i)
# print(t)    

#10.Filter Dictionary - Keep Items with Value Greater than 10
# Given dictionary:d = {'a': 5, 'b': 15, 'c': 25, 'd': 7}
# Create a new dictionary only with items where value > 10
# Expected Output:{'b': 15, 'c': 25}

# d = {'a': 5, 'b': 15, 'c': 25, 'd': 7}
# t={}
# for i,j in d.items():
#     if j>10:
#         t[i]=j
# print(t)        

# 1️⃣ Nested Dictionary of Squares
# Create a dictionary from numbers 1 to 3, where each key has a dictionary with its square and cube
# Expected Output:
# {
#   1: {'square': 1, 'cube': 1},
#   2: {'square': 4, 'cube': 8},
#   3: {'square': 9, 'cube': 27}
# }

# t={}
# for i in range(1,4):
#     t[i]={'square':i*i,
#           'cube':i*i*i}
# print(t)

#2.ASCII Mapping for Lowercase Letters
# Map each lowercase letter 'a' to 'z' to its ASCII value
# Expected Output:{'a': 97, 'b': 98, ..., 'z': 122}

# t={}
# for i in range(97,123):
#     t[chr(i)]=i
# print(t)   
  
#3.Create Reverse Word Dictionary
# Given list of words:words = ["cat", "dog", "bat"]
# Create a dictionary with words as keys and their reversed strings as values
# Expected Output:{'cat': 'tac', 'dog': 'god', 'bat': 'tab'}

# t={}
# w= ["cat","dog","bat"]
# for i in w:
#     t[i]=i[::-1]
# print(t)   

#2.a=[0,1,2,3,4,5,6,7,8,9]
#{'even': [0, 2, 4, 6, 8], 'odd': [1, 3, 5, 7, 9]}

# a=[0,1,2,3,4,5,6,7,8,9]
# e=[]
# o=[]
# for i in a:
#     if i%2==0:
#        e.append(i)
#     else:
#        o.append(i)
# print({'even':e,'odd':o})  

# 13. Dictionary with keys as numbers 1 to 5, values as list of factors
# Example: {1: [1], 2: [1,2], 3: [1,3], 4: [1,2,4], 5: [1,5]}
# t={}
# for i in range(1,6):
#     l=[]
#     for j in range(1,i+1):
#         if i%j==0:
#             l.append(j)
#     t[i]=l        
# print(t)

# 14.  Create a dictionary from a list of words, keys as words, values as word lengths, but only for words longer than 3 characters
# List: ["hi", "hello", "world", "is", "great"]

# l=["hi", "hello", "world", "is", "great"]
# t={}
# for i in l:
#     if len(i)>3:
#         t[i]=len(i)
# print(t)        

# 16. Given a dictionary with names and ages, create a dictionary of names of people age > 18
# people = {'John': 15, 'Alice': 25, 'Bob': 19}

# people = {'John': 15, 'Alice': 25, 'Bob': 19}
# t={}
# for i,j in people.items():
#     if j>18:
#         t[i]=j
# print(t)     

#17.{2: 'prime', 3: 'prime', 4: 'notprime', 5: 'prime', 6: 'notprime'}

# t={}
# for i in range(1,7):
#     co=0
#     for j in range(1,i):
#         if i%j==0:
#             co+=1
#         if co==1:
#             t[i]="prime"
#         else:
#             t[i]="not prime"
# print(t)  
                  
# k=[10,20,30,40]
# t={}
# for i in k:
#     t[i]=[j for j in range(1,i)if i%j==0 ]
# print(t)    

# k=[10,20,30,40]
# t={i:[j for j in range(1,i) if i%j==0 ] for i in k}
# print(t)

# for row in range(1,5):
#     for col in range(1,6):
#         if row==1 or row==3 or col==1 or col==5:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")    
#     print()                    
# l=[10,20,11,7,95]
# l1={x:'prime' if all(x%y!=0 for y in range(2,x))else 'not prime' for x in l}
# print(l1) 
# k='python'
# l={i:k.count(i) for i in k}
# print(l)

# a='hii madam'.split()
# l={i:'palindrome' if i[::-1]==i else 'not palindrome' for i in a }
# print(l)

l=[]
for i in range(2):
    k={}
    k['name']=input("enter a name:")
    k['age']=int(input("enter your age:"))
    k['marks']=int(input("enter a marks:"))
    k['salary']=int(input("enter your salary:"))
    l.append(k)
print(l)