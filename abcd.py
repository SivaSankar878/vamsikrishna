# 1.	Flatten a nested list (one level deep).
# n=[[1,2,3],[4,5,6,],[7,8,9,10]]
# t=sum(n,[])
# print(t)
# print()

# n=[[1,2,3],[4,5,6,],[7,8,9,10]]
# l=[]
# for i in n:
#     for j in i:
#         l.append(j)
# print(l)    
    
# 2.	Sort list of strings by length.
# l=['siva','sankar','tati','string']
# for i in range(len(l)):
#     for j in range(0,len(l)-i-1):
#         if len(l[j])<len(l[j+1]):
#             l[j],l[j+1]=l[j+1],l[j]
# print(l)  
# l=[2,56,98,19,34,35]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[j]>l[j+1]:
#             l[j],l[j+1] = l[j+1],l[j]
# print(l)                      
# 3.	Get common elements from two lists.
# l1=[1,2,3,4,54,5,6]
# l2=[3,9,5,7,54,10,90]
# l3=[]
# for i in l1:
#     for j in l2:
#         if i==j:
#             l3.append(j)
# print(l3)            

# 4.	Get elements only in the first list.
# l1=[1,2,3,4,54,5,6]
# l2=[3,9,5,7,54,10,90]
# l3=[]
# for i in l1:
#         if i not in l2:
#             l3.append(i)
# print(l3)            
# 5.	Merge and remove duplicates from two lists.
# l1=[1,2,3,4,54,5,6]
# l2=[3,9,5,7,54,10,90]
# print(list(set(l1+l2)))
# 6.	Group list items into sublists of size 2.
# n= [12, -7, 0, 45, 23, -18, 34, 67, -3, 8, 91, -56, 14, 29, -42, 37, 5, -10]
# l1=[]
# for i in range(0,len(n),2):
#     l1.append(n[i:i+2])
# print(l1)
# 7.	Find second largest element.
# numbers = [12, -7, 0, 45, 23, -18, 34, 67, -3, 8, 91, -56, 14, 29, -42, 37, 5, -10]
# k=sorted(numbers)
# print(k)
# print(k[-2])
# 8.	Find third smallest element.
# numbers = [12, -7, 0, 45, 23, -18, 34, 67, -3, 8, 91, -56, 14, 29, -42, 37, 5, -10]
# k=sorted(numbers)
# print(k)
# print(k[2])
# 9.	Rotate list to the right by 2.
# l1=[1,2,3,4,54,5,6]
# k=2
# l2=l1[-k:]+l1[:-k]
# print(l2)
# 10.	Rotate list to the left by 3.
# l1=[1,2,3,4,54,5,6]
# k=2
# l2=l1[k:]+l1[:k]
# print(l2)
# 11.	Check if two lists are equal.
# l1=[1,2,3,4,5,6]
# l2=[3,4,5,6,3,7]
# if l1==l2:
#     print(True)
# else:
#     print(False)    
# 12.	Find all indices of a given value.
# l2=[3,4,5,6,3,7,3]
# k=3
# l3=[]
# for i in range(len(l2)):
#     if l2[i]==k:
#         l3.append(i)
# print(l3)        

# 13.	Check if list is palindrome.
# l2=[3,4,5,6,5,4,3]
# l=l2[::-1]
# if l2==l:
#     print("palindrome")
# else:
#     print("not a palindrome")    
# 14.	Generate a list of squares up to n.
# l2=[3,4,5,6,5,4,3]
# l3=[]
# for i in l2:
#     i=i*i
#     l3.append(i)
# print(l3)    
# 15.	Convert list of integers to list of strings.
# l2=[3,4,5,6,5,4,3]
# s=[]
# for i in l2:
#     s.append(str(i))
# print(s)

# 16.	Convert list of strings to integers.
# l2=['3', '4', '5', '6', '5', '4', '3']
# s=[]
# for j in l2:
#     s.append(int(j))
# print(s)    
# 17.	Remove all None values from a list.
# l=[1,2,None,3,None,4,5,None]
# for i in l:
#     if i==None:
#         l.remove(i)
# print(l)        
# 18.	Count positive and negative numbers.
# numbers = [12, -7, 73, 45, 23, -18, 34, 67, -3, 8, 91, -56, 14, 29, -42, 37, 5, -10]
# co_p=0
# co_n=0
# for i in numbers:
#     if i>0:
#         co_n+=1
#     else:
#         co_p+=1
# print(co_p)
# print(co_n)

# 19.	Pair each item with its index.
# numbers = [12, -7, 0, 45, 23, -18, 34, 67, -3, 8, 91, -56, 14, 29, -42, 37, 5, -10]
# l=[]
# for i in range(len(numbers)):
#     l.append([numbers[i],i])
# print(l)    

# 20.	Sum of each pair in a list of tuples.
# k=[(12, 0), (-7, 1), (0, 2), (45, 3), (23, 4), (-18, 5), (34, 6), (67, 7)]
# j=[]
# for i in k:
#     m=i[0]+i[1]
#     j.append(m)
# print(j)    

# 21.	Split a list in half.
# l=[1,2,3,4,5,6,7,8,9,10]
# mid=len(l)//2
# f_l=l[:mid]
# s_l=l[mid:]
# print(f_l)
# print(s_l) 

# 22.	Convert 2D list to 1D list.
# matrix = [
#     [12, -7, 0, 45, 23, -18],
#     [34, 67, -3, 8, 91, -56],
#     [14, 29, -42, 37, 5, -10]
# ]
# k=[]
# for i in matrix:
#     for j in i:
#         k.append(j)
# print(k)        



