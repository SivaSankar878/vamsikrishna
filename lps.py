# l=[100,200,900,200,400,500,700]
# l.sort()
# print("this is the minimum number in the list:",l[0])
# print("this is the maximum number in the list:",l[-1])
# print(l)

# l=[100,200,900,200,400,500,700]
# t=list(reversed(l))  
# print(t)

# l=[100,200,900,200,400,500,700]
# k=0
# for i in l:
#     k=l.count(i)
#     print(i,'=',k)    

# l=[100,200,900,200,400,500,700]
# k=[]
# for i in l:
#     if i not in k:
#         k.append(i)
# print(k)        

# l=[100,200,900,200,400,500,700]
# s=0
# for i in l:
#     s+=i
# print(s)    

# l=[100,200,900,200,400,500,700]
# s=[]
# for i in l:
#     if i not in s:
#         s.append(i)
#         s.sort()
# print(s[-2])   
# print(s)     
  
# l1=[1,2,3,5]
# l2=[6,7,8,9]
# l1.extend(l2)
# print(l1)

# l=[1, 2, 3, 5, 6, 7, 8, 9]
# ev=[]
# od=[]
# for i in l:
#     if i%2==0:
#         ev.append(i)
#     else:
#         od.append(i)
# print(ev)
# print(od)    

# l1=[1,2,3,5]
# l2=[1,2,3,5]
# if sorted(l1) == sorted(l2):
#     print("True") 
# else:
#     print("False") 

# l=[1,2,3,4,5]
# k=2
# k=k%len(l)
# r=l[-k:]+l[:-k]
# print(r)

# k=[[1,2],[3,4],[5]]
# l=[]
# for i in k:
#     for j in i:
#         l.append(j)
# print(l)        

# l=[1,2,3,4,5]
# t=6
# p=[]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==t:
#             p.append((l[i],l[j]))
# print(p)        

# 1.	Write a Python program to reverse a string by swapping elements (first with last, second with second last, and so on).
# s='string'
# k=''
# for i in s:
#     k=i+k
# print(k)    
# 2.	Write a Python program that first checks whether a given number exists in a sorted list using Binary Search?

# 1.	Flatten a nested list (one level deep).
# nested_list = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9, 10]
# ]

# l=sum(nested_list,[])
# print(l)        
# 2.	Sort list of strings by length.
# s_l = ["apple", "banana", "cherry", "date", "elderberry"]
# for i in range(len(s_l)):
#     for j in range(0,len(s_l)-i-1):
#         if len(s_l[j])>len(s_l[j+1]):
#             s_l[j],s_l[j+1]=s_l[j+1],s_l[j]
# print(s_l)  
# s_l = ["apple", "banana", "cherry", "date", "elderberry"]
# j=sorted(s_l,key=len)
# print(j)
# 3.	Get common elements from two lists.
# l1=[1,2,3,4,5,6]
# l2=[3,4,7,8,9,10]
# c_e=[]
# for i in l1:
#     for j in l2:
#         if i==j:
#             c_e.append(i)
# print(c_e)            
# 4.	Get elements only in the first list.
# l1=[1,2,3,4,5,6]
# l2=[3,4,7,8,9,10]
# li_in=[]
# for i in l1:
#     if i not in l2:
#         li_in.append(i)
# print(li_in)            
# 5.	Merge and remove duplicates from two lists.
# l1 = [1, 2, 3, 4, 5, 6]
# l2 = [3, 4, 7, 8, 9, 10]
# l1.extend(l2)
# l3=set(l1)
# l4=list(l3)
# print(l4)

# me=list(set(l1+l2))
# print(me)
# 6.	Group list items into sublists of size 2.
# l=[1,2,3,4,5,6,7,8,9,10]
# l1=[]
# for i in range(0,len(l),2):
#     l1.append(l[i:i+2])
# print(l1)    
# 7.	Find second largest element.
# l=[23, 87, 5, 42, 16, 78, 34, 90, 11, 67]
# k=sorted(l)
# print(k[-2])
# 8.	Find third smallest element.
# l=[23, 87, 5, 42, 16, 78, 34, 90, 11, 67]
# k=sorted(l)
# print(k[2])
# 9.	Rotate list to the right by 2.
# l=[23, 87, 5, 42, 16, 78, 34, 90, 11, 67]
# k=2
# li=l[-k:]+l[:-k]
# print(li)
# 10.	Rotate list to the left by 3.
# l=[23, 87, 5, 42, 16, 78, 34, 90, 11, 67]
# k=3
# li=l[k:]+l[:k]
# print(li)
# 11.	Check if two lists are equal.
# l1=[1,2,3,4,7,5]
# l2=[3,4,5,7,6,8]
# if l1==l2:
#     print(True)
# else:
#     print(False)    
# 12.	Find all indices of a given value.
# l1=[3, 5, 2, 3, 8, 3, 9]
# v=3
# ind=[]
# for i in range(len(l1)):
#     if l1[i]==v:
#         ind.append(i)
# print(ind)       
# 13.	Check if list is palindrome.
# l1=[3, 5, 2, 3, 8, 3, 9]
# l2=l1[::-1]
# if l1==l2:
#     print("palindrome")
# else:
#     print("not palindrome")
# 14.	Generate a list of squares up to n.
# n=int(input())
# l=[]
# for i in range(0,n):
#         l.append(i*i)
# print(l)        
# 15.	Convert list of integers to list of strings.
# numbers = [12, 45, 7, 89, 23, 56, 34, 78, 91, 10]
# s=[]
# for i in numbers:
#     s.append(str(i))
# print(s)    
# 16.	Convert list of strings to integers.
# s=['12', '45', '7', '89', '23', '56', '34', '78', '91', '10']
# t=[]
# for i in s:
#     t.append(int(i))
# print(t)    
# 17.	Remove all None values from a list.
# values = [12, None, 45, 7, None, 89, 23, None, 56]
# for i in values:
#     if i==None:
#         values.remove(None)
# print(values)    
# values = [12, None, 45, 7, None, 89, 23, None, 56] 
# while None in values:
#     values.remove(None)
# print(values)       
# 18.	Count positive and negative numbers.
# l=[12, -7, 45, -32, 0, 89, -56, 23, -91, 34]
# p=[]
# n=[]
# for i in l:
#     if i>0:
#         p.append(i)
#     else:
#         n.append(i)
# print(p)
# print(n)                
# 19.	Pair each item with its index.
# l=[12, -7, 45, -32, 0, 89, -56, 23, -91, 34]
# li=[]
# for i in range(len(l)):
#     li.append((i,l[i]))
# print(li)    
# 20.	Sum of each pair in a list of tuples.
# pairs = [(2, 3), (5, 7), (10, -4), (6, 6)]
# sum=[]
# for i in pairs:
#     t=i[0]+i[1]
#     sum.append(t)
# print(sum)    
# 21.	Split a list in half.
# numbers = [12, -7, 45, -32, 0, 89, -56, 97,23]
# mid=len(numbers)//2
# f_h=numbers[:mid]
# s_h=numbers[mid:]
# print(f_h)
# print(s_h)
# 22.	Convert 2D list to 1D list.
# matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# k=[]
# for i in matrix:
#     for j in i:
#         k.append(j)
# print(k)        
# matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# k=sum(matrix,[])
# print(k)