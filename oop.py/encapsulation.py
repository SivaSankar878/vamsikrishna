# encapsulation
# binding data and code together ,by using the access modifiers we can protect the data.
# there are three types of access modifiers those are 
# 1.public ->we can access anywere  #name
# 2.private ->we can access only in the same class #__name
# 3.protected ->it acts like private in the same class public in the another calss #_name 

# public variable self,class variables
# class parent():
#     def __init__(self):
#         self.name='siva'
#     def method1(self):
#         print(self.name)   
# class child(parent):
#     def method2(self):
#         print(self.name)

# obj=child()
# obj.method1()
# obj.method2()

# class parent():
#     age=18
#     def __init__(self):
#         self.name='siva'
#     def method1(self):
#         print(self.name)   
# class child(parent):
#     def method2(self):
#         print(self.name)

# obj=child()
# obj.method1()
# obj.method2()
# print(obj.age) #we can access the class variables outside the class also

# private variables 
# class Bank:
#     def __init__(self):
#         self.__Balance=30000
#     def method(self):
#         print(self.__Balance)
# class sbi(Bank):
#     def method2(self):
#         pass
# obj=sbi()
# obj.method()
# print(obj._Bank__Balance)   

# class Bank:
#     def __init__(self):
#         self.__Balance=30000
#     def __method(self):
#         print(self.__Balance)
# class sbi(Bank):
#     def method2(self):
#         pass
# obj=sbi()
# obj._Bank__method()

class employees:
    def set1(self):
        self.emp_name='siva'
    def get1(self):
        return self.emp_name
    def set2(self):
        self.emp_age=23
    def get2(self):
        return self.emp_age
    def set3(self):
        self.emp_salary=25000
    def get3(self):
        return self.emp_salary
    def set4(self):
        self.emp_pin=522017
    def get4(self):
        return self.emp_pin
obj=employees()
obj.set1()
obj.set2()
obj.set3()
obj.set4() 
print("name:",obj.get1())   
print("age:",obj.get2())
print("salary:",obj.get3())
print("pincode:",obj.get4())
        