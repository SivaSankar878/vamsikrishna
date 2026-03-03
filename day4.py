#Dictionary 
D={'name':'sankar','age':23,'place':'Hyderabad'}
print(D['name'])
print(type(D))
D['name']='anand'
print(id(D))
print(D)

d1={'Sankar':{'office':91771,'Home':68356}}
print(d1['Sankar'])
print(d1['Sankar']['Home'])