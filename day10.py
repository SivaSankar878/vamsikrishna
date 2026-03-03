# today is another data type List
# by using index we can retrive the value index from a list index(value)
# l1=[11,12,13,14,15,16,17,'python','java','developer'] 
# t=l1[5]
# print(t)
# there is a method (append()), by using the append we can only add a single value at the end of the list.
# l1=[11,12,13,14,15,16,17,'python','java','developer']
# l1.append('Full Stack Developer')
# print(l1)
# we can add more than 1 value in the list by using extend()
# l1=[11,12,13,14,15,16,17,'python','java','developer']
# l2=[250,23,'sap','programming']
# l1.extend(l2)
# print(l1)
# there is a method (pop()), by using the pop we can only delete a single value at the end of the list, and also give the index(2) we can delete the value at index in 2.
# l1=[11,12,13,14,15,16,17,'python','java','developer']
# l1.pop()
# print(l1)
# l1.pop(7)
# print(l1)
# remove()  is also a method for deleting a particular value by using the value not using the index.
# l1=[11,12,13,14,15,16,17,'python','java','developer']
# l1.remove('python')
# print(l1)
# sort() is  used for sort the values in a list in ascending order,using sort(reverse=true) we can convert into descending order.
# l1=[23,43,234,54,87,12,21,3,5,7,8]
# l1.sort()
# print(l1)
# value=sorted(variable name) it is not a list method,it supports in non primitive data types,and also done descending order value=sorted(variable name,reverse=true).
# it is another sorting function
# l1=[23,43,234,54,87,12,21,3,5,7,8]
# t=sorted(l1,reverse=True)
# print(t)
# count() is used to count the variable frequency.
# l1=[1,1,1,1,2,2,3,3,4,5,6,5,4,3]

# print(l1.count(1))
# copy() is also used for copy the reference of a list not the objects in the list.
# l1=[1,1,1,1,2,2,3,3,4,5,6,5,4,3]
# l2=l1.copy()
# print(l2)
# there is also a min(),max() values to find the min and max values in a list.
# sum() is used to add the all values in a list.
# l1=[1,1,1,1,2,2,3,3,4,5,6,5,4,3]
# l2=min(l1)
# l3=max(l1)
# l4=sum(l1)
# print(l2)
# print(l3)
# print(l4)
# we can create object for methods ,the functions not need to create a object.
# by using extend we can add two lists list1.extend(list2).
# l1=[1,2,3,4]
# l2=[100,200,300] 
# l1.extend(l2)
# print(l1)
# l2=[100,200,300]
# su=0
# for i in l2:
#     su+=i
# print(su)          

# find even numbers in a list.
# li=[1,2,3,4,5,6,7,8,9,10]
# sum=[]
# for i in range(len(li)+1):
#     if i%2==0:
#         sum.append(i)
# print(sum)    

# l1=[11,12,13,14,15,16,17,'python','java','developer'] 
# for i in l1:
#     if type(i)==int and i%2==0:
#         print(i)  
# replace the even value with value+20
#  
# f=[1,2,4,5,8,9]   
# for i in range(len(f)):
#     if f[i]%2==0:
#         f[i]=f[i]+20
# print(f)    
# avg in a list
# l1=[1,1,1,1,2,2,3,3,4,5,6,5,4,3]
# avg=0
# sum=0
# for i in l1:
#     sum+=i
#     avg=sum/len(l1)
# print(avg)
# insert
li1=[1,2,3,5,6,7,8,98,8,34,5,43]
li1.insert(7,2000)
print(li1)

