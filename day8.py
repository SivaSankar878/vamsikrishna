# Nested for loop and Nested while loop 
# using nested for loop print tables and using nested for else loop prime numbers in a range
# for i in range(1,6):
#     for j in range(1,11):
#         print(i,'X',j,'=',i*j)
#     print() 
# print()       

# for i in range(10,20):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i,end=" ")  
# using nestesd while loop print tables. 
# a=1
# while a<=5:
#     b=1
#     while b<=9:
#         b+=1
#         print(a,'X',b,'=',a*b)  
#     print()    
#     a+=1
          
# string data type 
# string is a primitive data type and immutable ,string contain indexing and slicing ,
#  the index is used to retrieve the single charecter adnd slicing is used to retreive more than one charecter
# the string have concatenantion operator which is used to merge two strings
# here there are some method s these are writen by using declaing a variable we are not able to perform a operation on it
# upper->it is used to covert the lower case letters into upper case
st='welcome to python'
s1=st.upper()
print(s1)
# lower->it is used to covert the upper case letters into lower case
st1='WELCOME TO PYTHON'
s2=st1.lower()
print(s2)
# capitalize->it is used to covert the letters into upper of the first char in string
st2='welcome to python'
s3=st2.capitalize()
print(s3)
# title->it is used to covert the string (if there is a space between same string) capital of the first letter
st3='welcome to python'
s4=st3.title()
print(s4)
# replace->it is used to replace a string with another string
st3='welcome to python'
s4=st3.replace('python','java')
print(s4)
# swapcase->it is used to covert the lower case letters into upper case and upper case letters into lower case
st4='wElcOme To PyThoN'
s5=st4.swapcase()
print(s5)
# count->it tells how many times a char is repeated 
st='welcome to python'
s1=st.count('o')
print(s1)
# starts with->checking the first char
st='welcome to python'
s1=st.startswith('W')
print(s1) 
# ends with->checking the last char
st='welcome to python'
s1=st.endswith('n')
print(s1)

