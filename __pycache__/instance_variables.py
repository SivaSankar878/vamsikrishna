# class student():
#     def method(self):
#         print('this is a instance method')
# obj=student()
# obj.method()        

# class student():
#     def __init__(self):
#         name='siva sankar'
#         roll='y23ca053'
#         print(f'student name {name} and roll number {roll}')
# obj=student()

# class raju():
#     def __init__(self):
#         self.name='sankar'
#         self.age=23
#         self.phno=9177168356
#     def method(self):
#         self.surname='tati'
#         self.address='guntur'
# obj=raju()
# obj.method()
# obj.f_name='shiva'
# print(obj.__dict__)  


# #printing instance variables inside the class
# class employee():
#     def __init__(self):
#         self.emp_name='siva'
#         self.emp_age=24
#         self.emp_id='Y23CA053'
#     def method(self):
#         print(self.emp_name)
#         print(self.emp_age)
#         print(self.emp_id)
#         self.emp_address='Guntur'
#     def method1(self):
#         print(self.emp_address)
# obj=employee()      
# obj.method()  
# obj.method1()        

# #printing instance variables outside the class
# class employee():
#     def __init__(self):
#         self.emp_name='siva'
#         self.emp_age=24
#         self.emp_id='Y23CA053'
#     def method(self):
#         self.emp_address='Guntur'
#     def method1(self):
#         print(self.emp_address)
# obj=employee()  
# obj.method()    
# print(obj.emp_name)  
# print(obj.emp_age)
# print(obj.emp_id)
# print(obj.emp_address)

# class student():
#     def std(self,name,age):
#         self.name=name
#         self.age=age
# obj1=student()
# obj1.std('siva',24)
# obj2=student()
# obj2.std('sankar',25)
# print('object one std name:',obj1.name)
# print('object one std name:',obj1.age)
# print('object two std name:',obj2.name)
# print('object two std name:',obj2.age)

# # updating instance variables within the class
# class emp():
#     def __init__(self):
#         self.name='siva'
#     def method1(self):
#         print(f"employee name is: {self.name}")    
#         self.name='sankar'
#     def method2(self):
#         print(f'updated name is: {self.name}')    
        
# obj=emp()
# obj.method1()
# obj.method2()        

# # class variables  #writing variables in the class outside of the method and accessing the variable using class name.
# class student():
#     name='siva'
#     def method(self):
#         pass
# print(student.name)    


# # there are 2 ways to access the class method variables
# class emp():
#     @classmethod
#     def method(cls):
#         cls.name='Shiva'
#         print(cls.name) 
# emp.method() #by using cls name

# class stu():
#     @classmethod
#     def method1(cls):
#         cls.name='shankar'
#         print(cls.name)
# obj=stu
# stu.method1() #by using creating object

# # declaring class variable inside the constructor and cls method.
# class employee():
#     pin=522017
#     def __init__(self):
#         self.name='shiva'
#         employee.salary=25000
#     def method(self):
#         employee.adr='hyd'
#     @classmethod
#     def method1(cls):
#         cls.age=18 
#         print(cls.age)
# obj=employee()
# obj.method()
# obj.method1() 
# print(employee.__dict__)


# # accessing the local variables ouside the class and inside the class
# class employee():
#     name='Shiva'
#     def method(self):
#         self.sal=23000
#         print(self.name)
#         print(employee.name)
#     def method1(self): 
#         print(self.sal)   
# obj=employee()
# obj.method()
# obj.method1()
# print("***********************")
# print(employee.name)   #accessing outside the local variable
# print(obj.name)


# class gopi():
#     salary=70000
#     def method(self):
#         self.salary=135000
#         print(self.salary)
# obj=gopi()
# obj.method()  
# print("_______________")
# print(gopi.salary)   
               
        