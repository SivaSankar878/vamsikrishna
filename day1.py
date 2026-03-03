#siva="A"
#print(ord(siva))
"""a=200
b="siva" 
c=3.14
print(a,end=" ")
print(type(a))
print(id(a))
print(b,end=" ")
print(type(b))
print(id(b))
print(c,end=" ")
print(type(c))
print(id(c))
A=0b1111
print(A)
B=0o26
print(B)
C=0xA01
print(C)"""
n=int(input())
for rows in range(n+1):
    for cols in range(rows):
        print("*",end=" ")
    print()        
