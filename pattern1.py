n=5 
for rows in range(1,n+1):
    for cols in range(1,n+1):
        print(rows, end=" ")
    print()  
print()
for rows in range(1,n+1):
    for cols in range(1,n+1):
        print(cols, end=" ")
    print() 
print()
for rows in range(1,n+1):
    for cols in range(1,rows+1):
        print(rows, end=" ")
    print()
print()
for rows in range(1,n+1):
    for cols in range(1,rows+1):
        print(cols, end=" ")
    print()   
print()        

for rows in range(1,n+1):
    for cols in range(1,n-rows+2):
        print(cols, end=" ")
    print()   
print()  
for rows in range(1,n+1):
    for cols in range(1,n-rows+2):
        print(rows, end=" ")
    print()   
print()  
for rows in range(1,n+1):
    for cols in range(1,n-rows+2):
        print(n-rows+1, end=" ")
    print()   
print()  
for rows in range(1,n+1):
    for cols in range(1,n-rows+2):
        print(n-cols+1, end=" ")
    print()   
print()
for rows in range(1,n+1):
    for spaces in range(1,n-rows+1):
        print(" ",end="")
    for cols in range(1,rows+1):
        print(rows,end="")
    print()         
print()   
for rows in range(1,n+1):
    for spaces in range(1,n-rows+1):
        print("",end="")
    for cols in range(1,rows+1):
        print(cols,end="")
    print()         
print() 
for rows in range(1, n + 1):
    for spaces in range(1,rows-1+1):
        print(" ",end="")
    for cols in range(1,n-rows+2):
        print(rows,end="")
    print()
print()        
for rows in range(1, n + 1):
    for spaces in range(1,rows-1+1):
        print(" ",end="")
    for cols in range(1,n-rows+2):
        print(cols,end="")
    print()      
for rows in range(1, n + 1):
    for spaces in range(1,rows-1+1):
        print(" ",end="")
    for cols in range(1,n-rows+2):
        print(cols,end="")
    print() 
for rows in range(1,n+1):
    for spaces in range(n-rows+1):
        print(" ",end="")
    for cols in range(1,2*rows):
        print("*",end="")
    print()                 
print()
for rows in range(1,n+1):
    for spaces in range(rows):
        print(" ",end="")
    for cols in range(1,2*n-2*rows+2):
        print("*",end="")
    print()    
for rows in range(1,n+1):
    for cols in range(1,n+1): 
        if rows==1 or rows==n or cols==1 or cols==n :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()   
for rows in range(1,n+1):
    for cols in range(1,n+1): 
        if rows==3  or cols==3 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()             
for rows in range(1,n+1):
    for spaces in range(1,n-rows+1):
        print(" ",end="")
    for cols in range(1,rows+1): 
        if cols==1  or cols==rows or rows==n :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for rows in range(1,n+1):
    for cols in range(1,rows+1):
        print("*",end="")
    print()    
for rows in range(1,n+1):
    for cols in range(1,n-rows+1):
        print("*",end="")
    print() 
for rows in range(1,n+1):
    for space in range(1,n-rows+1):
        print(" ",end="")
    for cols in range(1,rows+1):
         print("*",end="")
    print()    
for rows in range(1,n):
    for space in range(1,rows+1):
        print(" ",end="")
    for cols in range(1,n-rows+1):
        print("*",end="")
    print()        