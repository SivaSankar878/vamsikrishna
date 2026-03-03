# # Dictionarys
# # dictionary allows the length and it is mutable it means we can update or delete the data in the dictionary,we can access the data by using name of the keys.
# # in dict we can also use the immmutable and mutable data types for values but in keys we only use immutable data type
# n=dict()
# print(type(n))
# dic={'name':'siva','age':23,'salary':25000}
# print(dic)
# print(type(dic))
# print(id(dic))
# print(dic['name'])
# s={'name':'sankar','number':{'office':7199175358,'personal':9177168564}}
# print(s['number']['personal'])
# # we can add the data into dict
# res={'a':10,'b':20,'c':30}
# res['e']=34
# print(res)
# res.update({'d':45})
# print(res)
# res.pop('a')
# print(res)
# print(res.get('c'))
# print(res)
# print(len(res))
# print(res.popitem())
# # by using get method if the value is not found it gives none not error (in like set discard)
# for i in res.items():
#     print(i)
 
# for keys,values in res.items():
#     print(keys) 
#     print(values)
# res.setdefault('pin',100)
# print(res)
# h='python'
# tem={}
# for i in h:
#     if i not in tem:
#         tem[i]=1
#     else:
#         tem[i]+=1
# print(tem)    
# # by using set default
# h='python'
# tem={}
# for i in h:
#         tem.setdefault(i,0)
#         tem[i]+=1
# print(tem)                

# n=int(input())
# l=[]
# for i in range(n):
#     tem={}
#     tem['name']=input()
#     tem['age']=int(input())
#     tem['mobile number']=int(input())
#     l.append(tem)  
# m=input("enter name:")
# for i in l:
#     if i['name']==m: 
#         for a,b in i.items():
#             print(a,':',b)   
# a=['a','b','c']
# b=[1,2,3]
# temp={}
# for i in range(len(a)):
#     temp[a[i]]=b[i]
# print(temp)    
# res={'a':10,'b':11,'c':12,'d':13}
# for keys,values in res.items():
#     if values%2==0:
#         res[keys]=values*2
# print(res)        
# f=['warangal','karimnagar','jagtial']
# tem={}
# for i in f:
#     print(i,':',len(i))   

# f=['warangal','karimnagar','jagtial']
# tem={}     
# for i in f:
#     tem[i]=len(i)
# print(tem)    
# a={'name':'sankar','age':23}
# b={'salary':15000,'mno':9177716824}
# c={**a,**b}
# print(c)
# s=['a','b','c']
# tem={}
# for i in s:
#     tem[i]=ord(i)
# print(tem)    
# s={'a':1,'b':2,'c':1}
# tem={}
# for i,j in s.items():
#     tem.setdefault(j,[]).append(i)    
# print(tem)

# l=[10,11,23,12,7]
# tem={}
# for i in l:
#     if i%2==0:
#         tem[i]='even'
#     else:
#         tem[i]='odd'  
# print(tem)

# g=[11,23,7,9,12,5]
# tem={}
# for i in g:
#     cou=0
#     for j in range(1,i+1):
#         if i%j==0:
#                 cou+=1
#         else:
#              cou==0        
#         if cou==2:
#             tem[i]='prime'
#         else:
#             tem[i]='not prime'
# print(tem)
                    
# s='banana'
# tem={}
# for i in s:
#     if i not in tem:
#         tem[i]=1
#     else:
#         tem[i]+=1
# print(tem)    

# d=[{'name':'siva','marks':70,'id':102},
#    {'name':'sankar','marks':75,'id':101},
#    {'name':'kittu','marks':91,'id':103}]
# highest=d[0]
# for i in d:
#     if i['marks']>highest['marks']:
#         highest=i
# print(i)     

# d=[1,2,3,4,5]
# tem={}
# for i in d:
#     tem[i]=i*i
# print(tem)    

# # by using setdefault find the factors of a given number that factors must be stored in a list.
# l=[10,20,34,28]
# tem={}
# for i in l:
#     for j in range(1,i):
#         if i%j==0:
#             tem.setdefault(i,[]).append(j)
# print(tem)      

# l=[10,20,34,28]
# tem={}
# for i in l:
#     for j in range(1,i):
#         if i%j==0:
#             tem[i]=[j]
# print(tem)  

# l=[10,18,20]
# for i in l:
#     print(i)

# d1={'a':200,'b':300}
# d2={'a':200,'c':400}
# d={}
# for i in d1:
#     d[i]=d1[i]+d2.get(i,0)
# for i in d2:
#     if i not in d:
#         d[i]=d2[i]
# print(d) 
# d3=d1.copy()
# for key,value in d2.items():
#     if key in d3:
#         d3[key]+=value
#     else:
#         d3[key]=value    
# print(d3)    

    
# n=5
# pro=1
# for i in range(1,n+1): # 1 2 3 4 5
#     pro*=i  #1*1=1, 1*2=2 ,2*3=6 ,6*4=24 ,24*5=120
#     print(pro,'==',i) 

# # Fibonacci    
# n=10
# a,b=0,1
# for i in range(n-1):
#     a,b=b,a+b
# print(a,end=' ')    

# # 1. Write a Python program to sort a dictionary by its keys.
# di={'name':'siva','age':23,'salary':24000,'id':1026}
# k=sorted(di.items())
# print(k)

# # 2. Write a Python program to find the maximum value in a dictionary.
# students = [
#      {"name": "Rahul", "age": 20, "marks": 85},
#      {"name": "Anita", "age": 21, "marks": 92},
#      {"name": "Kiran", "age": 19, "marks": 78}
# ]
# hig=0
# for i in students:
#     if i['marks']>hig:
#         hig=i['marks']
# print(hig) 
    
# res=[{'name':'kumar','department':'it'},
#      {'name':'sai','department':'sales'},
#      {'name':'ravi','department':'it'},
#      {'name':'arjun','department':'hr'}]
# tem={}
# for i in res:
#     d=i['department']
#     if d not in tem:
#         tem[d]=1 
#     else:
#         tem[d]+=1
# print(tem)                 

# res=[{'name':'kumar','department':'it'},
#      {'name':'sai','department':'sales'},
#      {'name':'ravi','department':'it'},
#      {'name':'arjun','department':'hr'}]
# tem={}
# for i in res:
#     d=i['name']
#     t=i['department']
#     if d  not in tem:
#         tem[d]=1
#     else:
#         tem[d]+=1
# print(tem)            

# d={'physics':75,'maths':78,'social studies':65,'telugu':89,'hindi':98}
# for i,j in d.items():
#     print(i,'=',j)

# student={"name":"rahul",'age':20,'marks':85}
# print(student['name'],'=',student['marks'])
# student.update(marks=100)
# student.update([('marks',23)])
# print(student)
# student.update(grade='A')
# print(student)

# student={"name":"rahul",'age':20,'marks':85}
# student.pop('age') #pop is used to delete a particular item
# student.popitem() #popitem deletes the last item in a dict
# print(student)

# s="banana"
# tem={}
# for i in s:
#     if i not in tem:
#         tem[i]=1
#     else:
#         tem[i]+=1
# print(tem)  

# d1={'a':10,"b":20}
# d2={'c':30,"d":40}
# tem=dict(**d1,**d2)
# tem1=(d1|d2)
# print(tem,tem1)        

# di={'a':100,'b':200,'c':70}
# h=0
# for i,j in di.items(): 
#     if j>h:
#         h=j
# print(h)      

# k={'a':1,"b":2}
# t={}
# for i,j in k.items():
#       t[j]=i
# print(t)      

# keys=["name","age"]
# values=["sankar",23]
# tem={}
# for i in range(len(keys)):
#     tem[keys[i]]=values[i]
# print(tem)    

# marks={'siva':65,'sankar':77,"diks":98}
# for i, j in marks.items():
#     k=dict(sorted(marks.items()))
# print(k)

# students = {
#     "Rahul": 85,
#     "Anita": 92,
#     "Kiran": 85, 
#     "Sita": 78,
#     "Vikram": 92,  
#     "Meena": 70
# }
# tem={}
# for i,j in students.items():
#     if j not in tem.values():
#         tem[i]=j 
# print(tem)        

# d={'a':10,"b":20,"c":40}
# c=0
# for i,j in d.items():
#     c+=j
# print(c)    

# # Write a program to find common keys in two dictionaries.
# d={'a':10,'b':20,'c':30}
# d1={'c':40,'a':50}
# tem=[]
# for i in d.keys():
#     if i in d1.keys():
#         tem.append(i)
# print(tem)        
