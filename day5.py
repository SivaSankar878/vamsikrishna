#operators
l1=[1,2,3,4]
l2=[6,7,8,9]
#l3=l1+l2
print(*l1,*l2)

t1=(23,45,65)
t2=(33,32,89)
print(t1+t2)
print(type(t1))

s1={2,3,6,7}
s2={89,91,56}
print(*s1,*s2)

d1={"name":"siva","id":1333884}
d2={"age":23}
print({**d1,**d2})

print(2 in l2)
print(3 not in l1)

print(23 in t1)
print(25 not in t2)


a=[1,1,1,1]
r=[]
sum=0
for i in a:
    if i not in r:
        r.append(i) 
for j in r:
    sum += j
print(sum)

a=10
b=20
a,b=b,a
print(a)
print(b)

