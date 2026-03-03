#Complex data type
H=2+3j
print(type(H))
print(H.real)
print(H.imag)

#List 
'''we can write a list in two ways shown below'''
f=[10,20,30,40]
print(f[2])
print(type(f))
k=list(['siva','gopi','anand'])
print(type(k))
t=k.append("uday")
print(k)
print(len(k))

#Tuple
# we can write a tuple by using (paranthesis.)
w=list()
x=set()
y=tuple()
z=dict()
print(type(w))
print(type(x))
print(type(y))
print(type(z))

#set
# we can write the set in {},but in list we can store only immutable data types like(int,float,string,complex,boolean,tuple).
set={1,2,3,4,8,5,3,2,3,2}
print(set)