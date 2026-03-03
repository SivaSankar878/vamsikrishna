

# f='pythondeveloper'
# count=0
# for i in range (len(f)):
#         count+=1
# print(count)        

# t=20
# for i in range(1,t):
#         if t%i==0:
#                 print(i)

# k=1
# for i in range(1,6):
#        k*=i
# print(k)                

# a = 153
# r = str(a) 
# t = len(r) 
# z = 0      
# for i in r:
#     z += int(i) ** t
# print(z)         
# print(z == a)    
 

#while loop
# i=1
# t=0
# while i<=10:
#     t+=i
#     i+=1
# print(t)

# t=0
# while t<=50:
#     print(t)
#     t+=2
# print()

# t=1
# while t<=50:
#     print(t)
#     t+=2
# print()      

# t=1
# sum=0
# while t<=50:
#     sum+=t
#     t+=1
# print(sum)

#palindrome
# s='madam'
# t=''
# for i in  s:
#     t=i+t
# if  s==t:
#     print('palindrome')   
# else:
#     print('not a palindrome')    

#table    
# i=1
# while i<11:
#     print(i*5) 
#     i+=1   

# print 1 to 10 and -1 to -10  and -10 to -1   
# t=-1
# while t>=-10:
#     print(t)
#     t-=1
# print()
# t=-10
# while t<=-1:
#     print(t)
#     t+=1    
# for i in range(-1,-10,-1):
#     print(i)

# for i in range(-10,-1,+1):
#     print(i)  
  
# n=1
# while n<=100:
#     print(n)
#     n+=1
# print()    
# n=1
# result=0
# while n<=100:
#     result+=n
#     n+=1 
# print(result) 
   
#  factorial by using while loop
# n=1
# re=1
# while n<=5:
#     re*=n
#     n+=1
# print(re)   

#Armstrong number checking
n=153
s=str(n)
l=len(s)
res=0
for i in s:
    res+=int(i)**l
print(res==n)   