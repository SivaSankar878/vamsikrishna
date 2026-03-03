# 1.	Flatten a nested list (one level deep).
# k=[[1,2,3],[4,5,6],[7,8,9]]
# l=[]
# for i in k:
#     for j in i:
#         l.append(j)
# print(l)  
      
# 2.	Sort list of strings by length.
# fruits = [ "guva","apple","banana"]
# fruits.sort(key=len,reverse=True)
# print(fruits)
           
# 3.	Get common elements from two lists.
# l1=['siva ','sankar',123,456,789]
# l2=['sankar','tati',456]
# l3=[]
# for i in l1:
#     for j in l2:
#         if i==j:
#             l3.append(j)
# print(l3) 
           
# 4.	Get elements only in the first list.
# l1=['siva ','sankar',123,456,789]
# l2=['sankar','tati',456]
# k=[i for i in l1 if i not in l2]
# print(k)

# 5.	Merge and remove duplicates from two lists.
# l1=['siva ','sankar',123,456,789]
# l2=['sankar','tati',456]
# l3=list(set(l1+l2))
# print(l3)

# 6.	Group list items into sublists of size 2.
# l1=['siva ','sankar',123,456,789]
# k=[]
# for i in range(0,len(l1),2):
#     k.append(l1[i:i+2])
# print(k)    

# 7.	Find second largest element.
# s = [1, 2, 3, 4, 5, 6]
# k=sorted(s,reverse=True)
# print(k[1])

# 8.	Find third smallest element.
# s = [1, 2, 3, 4, 5, 6]
# k=sorted(s,reverse=True)
# print(k[2])

# 9.	Rotate list to the right by 2.
# s = [1, 2, 3, 4, 5, 6]
# k=s[-2:]+s[:-2]
# print(k)

# 10.	Rotate list to the left by 3.
# s = [1, 2, 3, 4, 5]
# k=s[3:]+s[:3]
# print(k)

# 11.	Check if two lists are equal.
# l1=[1,2,3,4,5]
# l2=[3,2,2,1,5]
# if l1==l2:
#     print(True)
# else:
#     print(False)

# 12.	Find all indices of a given value.
# l=[1,2,3,4,2,6,7,2,2]
# k=2
# m=[]
# for i in range(len(l)):
#     if l[i]==k:
#         m.append(i)
# print(m)   

# 13.	Check if list is palindrome.
# l=[1,2,3,4,2,6,7,2,2]
# if l==l[::-1]:
#     print(True)
# else:
#     print(False)  

# 14.	Generate a list of squares up to n.
# l=[]
# for i in range(1,10):
#     k=i*i
#     l.append(k)
# print(l)    

# 15.	Convert list of integers to list of strings.
# 16.	Convert list of strings to integers.
# 17.	Remove all None values from a list.
# l=[None,1,2,3,None,8,9,None]
# for i in l:
#     if i==None:
#         l.remove(i)
# print(l)    
    
# 18.	Count positive and negative numbers.
# l=[-1,-2,3,4,5,-10,-90,-75,86]
# p=0
# n=0
# for i in l:
#     if i>0:
#         p+=1 
#     else:
#         n+=1
# print(p,n)

# 19.	Pair each item with its index.
# l=[-1,-2,3,4,5,-10,-90,-75,86]
# k=[]
# for i in range(len(l)):
#     k.append((l[i],i))
# print(k)    

# 20.	Sum of each pair in a list of tuples.
# t=  [(1, 2), (3, 4), (5, 6)]
# k=[]
# for i,j in t:
#     k=i+j
#     print(k)    

# 21.	Split a list in half.
# l=[1,2,3,4,5,6,7,8,9,10,11]
# k=len(l)//2
# f=l[:k]
# s=l[k:]
# print(f)
# print(s)

# 22.	Convert 2D list to 1D list.
# s=[[1,2,3],[4,5,6]]
# l=[]
# for i in s:
#     for j in i:
#         l.append(j)
# print(l)

# 23.	Filter names starting with "A".
# 24.	Replace all negative numbers with 0.
# 25.	Sort list of dicts by key value.
# 26.	Get all prime numbers from a list.
# 27.	Check if list contains all unique items.
# 28.	Zip two lists into a list of tuples.
# 29.	Unzip a list of tuples into two lists.
# 30.	Sum of diagonal in a 2D list (matrix).
# 31.	Find longest string in list.
# 32.	Find frequency of each element.
# 33.	Move all zeros to end of list.
# 34.	Group by even and odd.