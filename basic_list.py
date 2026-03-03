# 1.	Create a list of 5 integers.
# li=[1,2,3,4,5,6,7]
# print(li)
# 2.	Access the 3rd element of a list.
# print(li[3])
# 3.	Change the value at index 2.
# li[2]=9
# print(li)
# 4.	Append an element to the list.
# li.append(10)
# print(li)
# 5.	Insert an element at index 1.
# li.insert(1,21)
# print(li)
# 6.	Remove an element by value.
# li.remove(7)
# print(li)
# 7.	Remove an element by index.
# li.remove(li[1])
# 8.	Find the length of a list.
# t=len(li)
# print(t)
# 9.	Check if an element exists in a list.
# print(2 in li)
# 10.	Loop through a list and print each item.
# for i in li:
#     print(i)
# 11.	Sort a list in ascending order.
# li.sort()
# print(li)
# 12.	Sort a list in descending order.
# li.sort(reverse=True)
# print(li)
# 13.	Reverse a list using reverse().
# li.reverse()
# print(li)
# 14.	Reverse a list using slicing.
# k=li[::-1]
# print(k)
# 15.	Copy a list using slicing.
# l=li[0:7]
# print("this is a copy list of given list:",l)
# 16.	Copy a list using the copy() method.
# li.copy()
# print("this is the copy of list by using copy method:",li)
# 17.	Clear all elements in a list.
# li.clear()
# print(li)
# 18.	Count occurrences of a number.
# a=li.count(4)
# print(a)
# 19.	Find the index of a number.
# k=li.index(7)
# print(k)
# 20.	Concatenate two lists.
# li_1=[10,20,30,40]
# print(li+li_1)
# 21.	Repeat a list 3 times.
# print(li*3)
# 22.	Print every second element.
# for i in range(0,len(li),2):
#     print(i)
# 23.	Print elements from index 2 to 5.
# ind=li[2:6]
# print(ind)
# 24.	Check if all elements are positive.
# for i in li:
#     if i>0:
#         print("True")
#     else:
#         print("False")    
# 25.	Convert list to a string with commas.
# li_2=["apple","banana","carrot"]
# k=",".join(li_2)
# print(k)
# 26.	Find the max element.
# k=max(li)
# print(k)
# 27.	Find the min element.
# t=min(li)
# print(t)
# 28.	Sum all numbers in a list.
# i=sum(li)
# print(i)
# 29.	Square every number in a list.
# for i in li:
#     print(i**2)
# 30.	Filter even numbers from a list.
# z=[]
# for i in li:
#     if i%2==0:
#         z.append(i)
# print(z)        
# 31.	Filter odd numbers from a list.
# y=[]
# for i in li:
#     if i%2!=0:
#         y.append(i)
# print(y) 
# 32.	Find duplicates in a list.
# li=[1,2,1,1,2,2,2,8,6,5,4,4,5,6,7]
# l=[]
# d=[]
# for i in li:
#     if i not in l:
#         l.append(i)
#     else:
#         if i not in d:
#            d.append(i)
# print(d)

# 33.	Remove duplicates from a list.
# li=[1,2,1,1,2,2,2,8,6,5,4,4,5,6,7]
# l=[]
# for i in li:
#     if i not in l:
#         l.append(i)
# print(l)    
# 34.	Get unique elements using set().
# li_6=[1,2,1,1,2,2,2,8,6,5,4,4,5,6,7]
# k=set(li_6)
# print(k)
# 35.	Check if a list is empty.
# cou=0
# for i in li:
#     cou+=1
#     if cou>0:
#         continue
# print("list is not empty")
# 36.	Initialize a list of n zeros.
# n=int(input())
# print(list('0'*n))

# 37.	Swap two elements in a list.
# li[2],li[5]=li[5],li[2]
# print(li)
# 38.	Get last element of a list.
# print(li[-1])
# 39.	Convert a string to a list of chars.
# k="list of charecters"
# t=list(k)
# print(t)