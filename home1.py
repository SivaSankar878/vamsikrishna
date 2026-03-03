# 1. Create a string with your name and print it.
# n=input("enter a string:")
# print(n)

# 2. Get the first character from the string.
# print(n[0])

# 3. Get the last character from the string.
# print(n[-1])

# 4. Concatenate two strings.
# a="siva"
# b='sankar'
# c=print(a+b)

# 5. Repeat a string 3 times.
# a="siva"
# print(a*3)

# 6. Slice the first 5 characters.
# g="siva sankar"
# print(g[0:5])

# 7. Reverse a string using slicing.
# g="siva sankar"
# print(g[::-1])

# 8. Check if a substring exists in a string.
# k="siva sankar".split()
# g="sankar"
# if g in k:
#     print("yes, exist")
# else:
#     print("not found!")
    
# 9. Find the length of a string.
# k="hello python"
# print(len(k))

# 10. Convert string to uppercase.
# k="hello python"
# print(k.upper())

# 11. Convert string to lowercase.
# k="hello python"
# print(k.lower())

# 12. Capitalize the first letter.
# k="hello python"
# print(k.capitalize())

# 13. Convert a string to title case.
# k="hello python"
# print(k.title())

# 14. Remove leading spaces using lstrip().
# k=" india going tonight to lifting the trophy "
# print(k.lstrip())

# 15. Remove trailing spaces using rstrip().
# k=" india going tonight to lifting the trophy "
# print(k.rstrip())

# 16. Remove both ends' spaces using strip().
# k=" india going tonight to lifting the trophy "
# print(k.strip())

# 17. Replace all spaces with underscores.
# k=" india going tonight to lifting the trophy "
# print(k.replace(" ","_"))

# 18. Count how many times a character appears.
# k=" india going tonight to lifting the trophy "
# print(k.count('i'))

# 19. Find index of a character using find().
# k=" india going tonight to lifting the trophy "
# print(k.find("i"))

# 20. Use rfind() to find last occurrence.
# k=" india going tonight to lifting the trophy "
# print(k.rfind("i"))

# 21. Use index() to find substring position.
# k=" india going tonight to lifting the trophy ".split(' ')
# l="trophy"
# m=k.index(l)
# print(m)

# 22. Split a string by spaces.
# k=" india going tonight to lifting the trophy "
# print(k.split())

# 23. Join a list of words into a string.
# k='siva sankar'
# m=''
# for i in k:
#     m=' '.join(i)
#     print(m,end="")
#     
# 24. Check if string starts with "Hello".
# s="HELLO siva , how are you"
# print(s.startswith("HELLO"))

# 25. Check if string ends with "world".
# s="HELLO siva , how are you"
# print(s.endswith("you"))

# 26. Check if a string is digit.
# d='1253678'
# print(d.isdigit())

# 27. Check if a string is alphabet.
# k='abjduk16738'
# print(k.isalpha())

# 28. Check if a string is alphanumeric.
# k='snskaqk178393'
# print(k.isalnum())

# 29. Get ASCII value of a character.
# a='c'
# print(ord(a))

# print("this is the ascii value of capital C",ord("C"))

# 30. Convert ASCII to character.
# print(chr(97))

# 31. Remove punctuation from string.
# s="!siva @are u & using *any (ai) {tools}?"
# p="{}[]!@#$%^&*(()_~)"
# k=''
# for i in s:
#     if i in p:
#         continue
#     else:
#         k+=i
# print(k)        

# 32. Swap case of all characters.
# k="SiVA sAnkaR"
# print(k.swapcase())

# 33. Count total words in a string.
# k="india going tonight to lifting the trophy"
# co=0
# for i in k.split( ):
#     co+=1
# print(co)  
#   
# 34. Count total sentences in a string.
# k='india. have. so many. world cups.'
# co=0
# for i in k:
#     if i.endswith("."):
#         co+=1
# print(co)   
#  
# 35. Convert string to list of characters.
# k="india going tonight to lifting the trophy"
# l=[]
# for i in k:
#     l.append(i)
# print(l)    

# 36. Convert list of characters to string.
# k=['a','b','c','d','e']
# s=''
# for i in k:
#     s+=i
# print(s)    