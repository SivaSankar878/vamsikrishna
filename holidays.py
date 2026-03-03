# List Comprehension

# 1. Generate a list of squares of numbers from 1 to 20.
# l=[i*i for i in range(1,21)]
# print(l)

# 2. Create a list of even numbers from 1 to 50.
# k=[i for i in range(1,51)]
# print(k)

# 3. From a list of words, extract those that start with a vowel.
# vowel='aeiou'
# k=['annual day','orange','elephant','umberella']
# p=[i for i in k if i[0].lower() in vowel]
# print(p)

# 4. Convert a list of temperatures in Celsius to Fahrenheit.
# l=['20','37','100','105']
# f=33.8
# k=[float(i)*f for i in l]
# print(k)

# 5. Flatten a 2D list into a 1D list.
# k=[[1,2,3],[4,5,6],[7,8,9]]
# l=[j for i in k for j in i]
# print(l)

# 6. Create a list of prime numbers between 1 and 50.
# l=[i for i in range(1,51) if len ([j for j in range(1,i+1) if i%j==0])==2]
# print(l)

# 7. Extract all numbers divisible by 3 or 5 from 1 to 100.
# k=[i for i in range(1,101) if i%3==0 and i%5==0]
# print(k)

# 8. Reverse each word in a given list of words.
# l=["hello","world","good","morning"]
# k=[i[::-1] for i in l]
# print(k)

# 9. Generate a list of tuples (number, square) for numbers from 1 to 15.
# k=[(i,i*i) for i in range(1,16)]
# print(k)
# 10. Filter out negative numbers from a given list.
# k=[-1,-10.4,5,6,7,5,-43,-94,-199]
# l=[i for i in k if i>0]
# print(l)

# String

# 1. Extract all vowels from a string.
# s='siva sankar'
# l=[]
# for i in s:
#     if i in 'aeiou':
#         l.append(i)
# print(l)        

# 2. Remove all digits from a string.
# s='12ahjswk383'
# s1=''
# for i in s:
#     if i.isdigit():
#         continue
#     else:
#         s1+=i
# print(s1)        

# 3. Count the frequency of each character in a string.
# s='siva sankar'
# l=''
# for i in s:
#     if i not in l:
#        cou=0 
#        for j in s:
#            if i==j:
#                cou+=1
#        print(i,':',cou) 
#        l+=i       


# 4. Convert all characters of a string into uppercase using comprehension.
# s='siva sankar'
# l=[i.upper() for i in s]
# print(l)

# 5. Replace spaces with underscores_
# s='good morning welcome to vs code'
# k=s.replace(" ","_")
# print(k)

# 6. Extract only alphabetic characters from "Python3.9 Version".
# s='dhsjidmam1839nme7373n'
# k=''
# for i in s:
#     if i.isalpha():
#         k+=i
# print(k)        

# 7. Reverse a string using comprehension.

# 8. Create a list of ASCII values of characters in "Hello" Bright
# k='Hello'
# l=[]
# for i in k:
#     l.append(ord(i))
# print(l)    

# 9. Keep only consonants from a given string.
# k='consonants'
# s='AEIOU'
# l=''
# for i in k:
#     if i.upper() not in s:
#         l+=i
# print(l)        

# 10. Find all unique characters in a string.
# s='hello world'
# l=''
# for i in s:
#     if i not in l:
#         cou=0
#         for j in s:
#             if i==j:
#                 cou+=1        
#         l+=i
#         if cou==1:
#             print(i,end=",")                              

# Dictionary Comprehension

# 1. Create a dictionary of numbers and their squares (1-10).
# d={i:i*i for i in range(1,11)}
# print(d)

# 2. Map each word in a list to its length.
# l=['siva','sankar','tati']
# d={i:len(i) for i in l}
# print(d)

# 3. Count frequency of each character in "banana".
# s='banana'
# d={i:s.count(i) for i in s}
# print(d)

# 4. Convert a dictionary of Celsius values to Fahrenheit.
# l=[10,20,30,40]
# d={i:i*33.8 for i in l}
# print(d)

# 5. Swap keys and values in a dictionary.
# d={'name':'siva','age':23,'height':5.10}
# d1={value:key for key,value in d.items()}
# print(d1)

# 6. Filter a dictionary to keep only even values.
# d={'siva':22,'sankar':25,'chakri':24,'abhi':22}
# d1={key:value for key,value in d.items() if value%2==0}
# print(d1)

# 7. Create a dictionary where keys are numbers 1-10 and values are "even" or "odd".
# d={i:("even" if i%2==0 else "odd") for i in range(1,11)}
# print(d)

# 8. From two lists ['a','b','c'] and [1,2,3] create a dictionary.
# d1=['a','b','c']
# d2=[1,2,3]
# d={d1[i]:d2[i] for i in range(len(d1))}
# print(d)

# d1=['a','b','c']
# d2=[1,2,3]
# d={}
# for i,j in zip(d1,d2):
#     d[i]=j
# print(d)

# 9. create a dictionary of vowels and their counts in a string.
# s='siva sankar tati'
# k='AEIOUaeiou'
# d={i:s.count(i) for i in s if i in k}
# print(d)

# 10.create a dictionary with squares if a number is divisible by 3.
# d={i*i for i in range(1,100) if i%3==0}
# print(d)

# for loop

# 1. Print all numbers from 1 to 50.
# for i in range(1,51):
#     print(i,end=",")

# 2. Print multiplication table of 7.
# for i in range(1,11):
#     print('7','X',i,'=',i*7)

# 3. Calculate factorial of a number using a loop.
# n=5
# f=1
# for i in range(1,n+1):
#     f*=i
# print(f)    

# 4. Count vowels in a string.
# s='siva sankar tati'
# co=0
# for i in s:
#     if i.upper() in  'AEIOU':
#         co+=1
# print(co)        

# 5. Find the largest element in a list.
# k=[200,500,900,35,6700,354,1001]
# t=0
# for i in k:
#     if i>t:
#         t=i
# print(t)        

# 6. Print Fibonacci series up to 10 terms.
# n=10
# a=0
# b=1
# for i in range(n-1):
#     a,b=b+a,a
# print(b,a)

# 7. Reverse a string using a for loop.
# s='good afternoon guys'
# k=''
# for i in s:
#     k=i+k
# print(k)    

# 8. Count how many words are in a sentence (without using split).
# s='good afternoon guys'
# co=1
# for i in s:
#     if i==" ":
#         co+=1
# print(co)

# 9. Find all prime numbers between 1 and 100.
# s=2
# e=101
# l=[]
# for i in range(s,e):
#     co=0
#     for j in range(2,i):
#         if i%j==0:
#             co+=1
#     if co==0:
#         l.append(i)
# print(l)                

# 10. Print elements of a nested list row by row.
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i,end=" ")
#     print()    

# 11. Find the second largest number in a list.
# k=[200,500,900,35,6700,354,1001]
# f_h=0
# s_h=0
# for i in k:
#     if i>f_h:
#         f_h=i
#     else:
#         s_h=i
# print(s_h)            


# 12. Print only those numbers from a list that are divisible by both 2 and 3.
# l=[6,23,24,34,36,810,90]
# for i in l:
#     if i%2==0 and i%3==0:
#         print(i)

# 13. Given a list of words, print the word with the maximum length. 
# s=['siva','sankar','tati']
# l=0
# k=''
# for i in s:
#     if len(i)>l:
#         l=len(i)
#         k=i
# print(l,k)        

# 14. Find the sum of digits of each number in a list [123, 45, 7891] 
# v=[123, 45, 7891] 
# s=[]
# for i in v:
#     t=0 
#     for j in str(i):
#         t+=int(j)
#     s.append(t)
# print(s)                

# 15. Print all substrings of "ABC".
# s='abc'
# n=len(s)
# for i in range(n):
#     for j in range (i+1,n+1):
#         print(s[i:j])

# 16. Find and print all perfect numbers between 1 and 1000. 
for i in range(1,1001):
    if i==sum(j for j in range(1,i) if i%j==0):
        print(i)

# 17. From a sentence, print each word in reverse order.
# s='siva sankar tati'.split()
# for i in s:
#     print(i[::-1],end=" ")

# 5. While Loop

# 1. Print numbers from 1 to 20 using while loop.
# n=1
# while n<=20:
#     print(n)
#     n+=1

# 2. Sum of digits of a number.

# 3. Reverse a number (e.g., 123321).

# 4. Check if a number is palindrome.

# 5. Keep asking user input until they type "exit".

# 6. Find factorial of a number using while loop.

# 7. Print Fibonacci series up to n terms.

# 8. Count number of digits in a number.

# 9. Keep generating random numbers until you get a multiple of 7.