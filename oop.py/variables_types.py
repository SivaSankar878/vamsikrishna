# oops-> object oriented programming syatem is programming paradigm,it 
# contains attributes and code manipulate data is called oops.
# there are 6 main pillars in oops these are also called as oops features.
# 1.class
# 2.object
# 3.abstraction
# 4.inheritence
# 5.polymorphism(the polymorphisms are two types method oveloading and method overriding.)
# 6.encapsulation

# class first_programme():
#     def even(self):
#         for i in range(10,20):
#             if i%2==0:
#                 print(i)

# obj=first_programme()
# obj.even()

# class str():
#     def swap(self,st):
#         res=''
#         for i in st:
#             if ord(i)>=65 and ord(i)<=91:
#                 d=chr(ord(i)+32)
#                 res+=d
#             elif ord(i)>=97 and ord(i)<=122:
#                 d1=chr(ord(i)-32)
#                 res+=d1
#         print(res)

# obj=str()
# obj.swap('sAnkAR')  


# #variables types
# # 1.instance variables
# # 2.local variables
# # 3.class variables

# # methods
# # 1.static methods
# # 2.instance methods
# # 3.class methods
# # 4.constructor methods

# class name():
#     def __init__(self):
        # self.name='siva' #instance variables
#         self.age=23
#         self.no=9177168356
#     def details(self):
#         self.pin='522017'
#         print(self.name)
#         print(self.age)
#         print(self.no)
#         print(self.pin)
# obj=name()
# obj.details()                              

# the instance variables can write inside the class,constructor,and instance method . 

# class abc():
#     def __init__(self,n,a,p):  #parameterized constructor
#         self.n1=n
#         self.a1=a
#         self.p1=p
#     def method(self):
#         print(self.n1)
#         print(self.a1)
#         print(self.p1)
# obj=abc('siva',23,522017)
# obj.method()            
        
# class student():
#     def __init__(self):
#         self.school='chakri'
#     def method(self,name,age,f_name,phno):  # parameters in method1 and accesing the parameters.
#         self.n1=name
#         self.a1=age
#         self.f1=f_name
#         self.p1=phno
#     def method2(self):
#         print(self.n1)
#         print(self.a1)        
#         print(self.f1)
#         print(self.p1)
# obj=student()
# obj.method('siva',23,"abcd",9898989)
# obj.method2()  


ph=input('phone no:')
digits={"1":'One',
        '2':'Two',
        '3':'Three',
        '4':'Four',
        '5':'Five',
        '6':'Six',
        '7':'Seven',
        '8':'Eight',
        '9':'Nine',
        '0':'Zero'}
number=""
for i in ph:
        number+=digits.get(i)+' '
print(number)        
        