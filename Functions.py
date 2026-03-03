# def even(a,b):
#     for i in range(a,b):
#         if i%2==0:
#             print(i)
# even(1,30)
# even(350,370)

# def length(a):
#     co=0
#     for i in a:
#         co+=1
#     print(co)
# length("python")
# length('java')
# length('good morning')

# def even_check(a):
#     if a%2==0:
#         print("even")
#     else:
#         print("odd")
# even_check(32)
# even_check(93)       

# # 1. Create a function to check whether a number is prime or not.
# def p_c(a):
#     co=0
#     for j in range(2,a):
#         if a%j==0:
#             co+=1
#     if co==0:
#         print('prime')
#     else:
#         print('not prime')
# p_c(7)                        
# p_c(11)
# p_c(20)

# #2. Create a function to print all prime numbers between a given range.
# def prime_range(a,b):
#     for i in range(a,b):
#         co=0
#         for j in range(1,i+1):
#             if i%j==0:
#                 co+=1
#         if co==2:
#             print(i)    
# prime_range(200,300) 

# #3. Create a function to implement swapcase functionality without using the built-in method.
# def swap(s):
#     return s.swapcase()
# print(swap('SivA'))
# print(swap('sAnKaR'))
# print(swap('TatI'))

# #4. Create a function to find the factorial of a number. 
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)           
# print(fact(5))    

# def fact(n):
#     p=1
#     for i in range(1,n+1):
#         p*=i
#     return p    
# print(fact(5))        

# #1.Prime Check:
# #Write a function is_prime(n) that checks whether a number is a prime number.
# def p_c(a):
#     co=0
#     for i in range(2,a):
#         if a%i==0:
#             co+=1
#     if co==0:
#         print("prime")
#     else:
#         print("not prime")
# p_c(7)                    

# #2. Sort List:
# #Write a function sort_list(lst) that returns the sorted list in ascending order.
# def sort_list(l):
#     return sorted(l,reverse=True)
# print(sort_list([12, 45, 67, 23, 89, 34, 56]))

# #3. Convert to Uppercase:
# #Write a function to_uppercase(text) that converts a string to uppercase without using the built-in upper() function.
# def to_uppercase(t):
#     s=''
#     for i in t:
#         if ord(i)>96:
#             j=ord(i)-32
#             s+=chr(j)
#     return s        
# print(to_uppercase('siva sankar'))        

# #4. Count Vowels:
# #Write a function count_vowels(s) that returns the number of vowels in a string.
# def count_vowels(s):
#     co=0
#     k='aeiouAEIOU'
#     for i in s:
#         if i in k:
#             co+=1
#     return(co)
# print(count_vowels('siva sankar tati'))

# #5. Even or Odd Check:
# #Write a function is_even(n) that returns True if the number is even, otherwise False.
# def is_even(n):
#     if n%2==0:
#         print(True)
#     else:
#         print(False)
# is_even(10)
# is_even(9) 

# #6. Factorial:
# #Write a function factorial(n) that returns the factorial of a number using a loop.
# def factorial(n):
#     f=1
#     for i in range(1,n+1):
#         f*=i
#     print(f)
# factorial(6)

# #7. Reverse a String:
# #Write a function reverse_string(s) that returns the reversed string.
# def reverse_string(s):
#     t=''
#     for i in s:
#         t=i+t
#     return t
# print(reverse_string('palindrome'))
    
# #8. Find Maximum:
# #Write a function find_max(lst) that finds and returns the maximum value in a list.
# def find_max(lst):
#     k=max(lst)
#     print(k)
# find_max([12, 45, 67, 23, 89, 34, 56])

# #9. Palindrome Check:
# # Write a function is_palindrome(s) that checks if a string is a palindrome.
# def is_palindrome(s):
#     k=s[::-1]
#     if s==k:
#         print('palindrome')
#     else:
#         print('not a palindrome')
# is_palindrome('madam')
# is_palindrome('sankar')            

# #10. Sum of List Elements:
# #Write a function sum_list(lst) that returns the sum of all elements in a list.
# def sum_list(lst):
#     k=sum(lst)
#     print(k)
# sum_list([12, 45, 67, 23, 89, 34, 56])
 
# def sum_list(lst):
#     s=0
#     for i in lst:
#         s+=i
#     print(s)
# sum_list([12, 45, 67, 23, 89, 34, 56])        

# #11. Print non Reputation character in a string and first non Reputation character?
# def non_repeating_chr(s):
#     l=''
#     for i in s:
#         if s.count(i)==1:
#             l+=i
#     print("these are the non repeating charecters in string:",l)    
#     print("this is the first non repeating charecter in string:",l[0])
# non_repeating_chr('good morning')        
                  

# #12. Find Second max value in a list 
# def s_h(lst):
#     k=sorted(lst)
#     print(k[-2])
# s_h([12, 45, 67, 23, 89, 34, 56]) 

# #13. Check Given number is Strong Number or not?                
# #14. print Prime numbers between 20 to 50 by using list comprehension 
# def p_c(a,b):
#     k=[i for i in range(a,b)if len([j for j in range(2,i)if i%j==0])==0]
#     print(k)
# p_c(20,50)    

# #15. Write a python code to Print ‘A’ Pattern
# def pattern(A):
#     for row in range(1,A):
#         for col in range(1,A):
#             if row==1 or row==3 or col==1 or col==5:
#                 print("A",end=" ")
#             else:
#                 print(" ",end=" ")    
#         print()
# pattern(6)

# #16. Write a Python code to Print ‘X’ Pattern
# def pattern(x):
#     for row in range(1,x):
#         for col in range(1,x):
#             if row==1 and col in [1,5] or row ==2 and col in [2,4] or row==3 and col==3 or row ==4 and col in [2,4] or row==5 and col in [1,5]:
#                 print("X",end=" ")
#             else:
#                 print(" ",end=" ")    
#         print()
# pattern(6) 

# # 17. Write a Python code to Check Anagram
# def Check_Anagram(a,b):
#     if len(a)==len(b):
#         if sorted(a)==sorted(b):
#             print("anagram")
#         else:
#             print("length matched but not a anagram")
# Check_Anagram('listen','silent')   

# #1.Create a user-defined function max_value() that returns the maximum value from a list. 
# #If the list contains both numbers and strings, handle them properly so the function still works without error.
# def max_value(lst):
#     k=[]
#     for i in lst:
#         if isinstance(i,(int,float)):
#             k.append(i)
#     print(max(k))
# max_value(['apple', 25, 'banana', 42, 'cherry', 100, 'grape', 7])   
 
# #2.Create a user-defined function title_case() that converts the first 
# #letter of each word in a string to uppercase (like the built-in title() function).
# def title_case(s):
#     for i in s:
#         k=s.title()
#     print(k)
# title_case("siva sankar tati")           