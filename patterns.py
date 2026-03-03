n=6
for rows in range(1,n+1):
    for cols in range(1,n+1):
        print(rows,end=" ")
    print()
print()        
for rows in range(1,n+1):
    for cols in range(1,n+1):
        print(cols,end=" ")
    print()  
print()
for rows in range(1,n+1):
    for cols in range(1,rows+1):
        print(rows,end=" ")
    print()  
print()
for rows in range(1,n+1):
    for cols in range(1,rows+1):
        print(cols,end=" ")
    print()  
print()
for rows in range(1,n+1):
    for cols in range(1,n-rows+2):
        print(rows,end=" ")
    print()  
print()
for rows in range(1,n+1):
    for cols in range(1,n-rows+2):
        print(cols,end=" ")
    print()  
print()
for rows in range(1,n+1):
    for cols in range(1,n-rows+2):
        print(n-rows+1,end=" ")
    print()  
print()
for rows in range(1,n+1):
    for cols in range(1,n-rows+2):
        print(n-cols+1,end=" ")
    print()  
print()
for rows in range(1,n+1):
    for spaces in range(1,n-rows+1):
        print(" ",end=" ")
    for cols in range(1,rows+1):
        print(rows,end=" ")
    print()  
print()
for rows in range(1,n+1):
    for spaces in range(1,n-rows+1):
        print(" ",end=" ")
    for cols in range(1,rows+1):
        print(cols,end=" ")
    print()  
print()
for rows in range(1,n+1):
    for spaces in range(1,rows):
        print(" ",end=" ")
    for cols in range(1,n-rows+2):
        print(rows,end=" ")
    print()  
print()
for rows in range(1,n+1):
    for spaces in range(1,rows):
        print(" ",end=" ")
    for cols in range(1,n-rows+2):
        print(cols,end=" ")
    print()  
print()
for rows in range(1,n+1):
    for spaces in range(1,n-rows+1):
        print(" ",end="")
    for cols in range(1,2*rows):
        print("*",end="")
    print()  
print()
for rows in range(1,n+1):
    for spaces in range(1,rows):
        print(" ",end="")
    for cols in range(1,2*n-2*rows+2):
        print("*",end="")
    print()  
print()
for rows in range(1,n+1):
    for spaces in range(1,n-rows+1):
        print(" ",end="")
    for cols in range(1,2*rows):
        print("*",end="") 
    print() 
for rows in range(1,n+1):      
    for spaces in range(1,rows+1):
        print(" ",end="")  
    for cols in range(1,2*n-2*rows):
        print("*",end="")    
    print()  
print()
for rows in range(1,n+1):
    for spaces in range(n-rows+1):
        print(" ",end="")
    for cols in range(1,rows*2):
        print("*",end="")
    print() 
print()
for rows in range(1,n+1):
    for spaces in range(n-rows+1):
        print(" ",end=" ")
    for cols in range(1,rows+1):
        if cols==1 or cols==rows or rows==n:
          print("*",end=" ")
        else:
            print(" ",end=" ")  
    print() 
print() 
for rows in range(1,n+1):
    for cols in range(1,rows+1):
        print("*",end="")
    print()   
for rows in range(1,n+1):
    for cols in range(1,n-rows+1):
        print("*",end="")
    print()       
print()
for rows in range(1,n+1):
    for spaces in range(1,n-rows+1):
        print(" ",end="")
    for cols in range(1,rows+1):
        print("*",end="")
    print()
for rows in range(1,n):
    for spaces in range(1,rows+1):
        print(" ",end="")
    for cols in range(1,n-rows+1):
        print("*",end="")
    print()
a=1
b=2

for i in range (1,n+1):
    for space in range(1,1+n-i):
        print(" ",end=" ")
    if i%2==1:
        for j in range (i):
            print(a ,end=" ")
            a+=2
    else:
        for j in range(i):
            print(b,end=" ")
            b+=2
    print()
arr1=[1,9,16,4,36,25,49]
arr2=[9,49]
C_E=[x for x in arr1 if x in arr2]
print(C_E)
arr1=[8,27,64,100,738,992,9928]
f_l_n=max(arr1)
f_s_n=min(arr1)
print(f_l_n)
print(f_s_n)
arr=[1,9,16,4,36,25,49]
s_o_e=sum(arr)
print(s_o_e)
arr1=[8,27,64,100,738,992,9928]
print(arr1[::-1])
n=int(input())
arr1=[8,27,64,100,738,992,9928]
if n in list(arr1):
    i=arr1.index(n)
    print("yes , the existed number is:",n)
else:
    print("no")
        


                  
     