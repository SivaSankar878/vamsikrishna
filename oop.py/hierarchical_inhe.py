# # hierarchical inheritence
# class parent():
#     def method1(self):
#         self.p_name='veeraiah'
#         self.p_age=56
#         print('parent name:',self.p_name,"\n parent age:",self.p_age)
# class child1(parent):
#     def method2(self):
#         self.c1_name='gopi'
#         self.c1_age=25
#         print('child1 name:',self.c1_name,"\n child1 age:",self.c1_age)   
# class child2(parent):
#     def method3(self):
#         self.c2_name='sankar'
#         self.c2_age=23
#         print('child1 name:',self.c2_name,"\n child1 age:",self.c2_age)

# obj1=child1()
# obj1.method1()
# obj1.method2()

# obj2=child2()
# obj2.method1()
# obj2.method3()

# # hierarchical inheritence and overriding with using class name instead of super keyword
# class parent():
#     def method(self):
#         self.p_name='veeraiah'
#         self.p_age=56
#         print('parent name:',self.p_name,"\n parent age:",self.p_age)
# class child1(parent):
#     def method(self):
#         parent.method(self)
#         self.c1_name='gopi'
#         self.c1_age=25
#         print('child1 name:',self.c1_name,"\n child1 age:",self.c1_age)   
# class child2(parent):
#     def method(self):
#         parent.method(self)
#         self.c2_name='sankar'
#         self.c2_age=23
#         print('child1 name:',self.c2_name,"\n child1 age:",self.c2_age)

# obj1=child1()
# obj1.method()

# obj2=child2()
# obj2.method()

