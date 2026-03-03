# multilevel inheritence
# class grand_parent():
#     def method(self):
#         self.gp_name='sambaiah'
#         self.gp_age=81
#         print("grand parent name:",self.gp_name ,"\n","grand parent age:",self.gp_age)
# class parent(grand_parent):
#     def method1(self):
#         self.p_name='veeraiah'
#         self.p_age=56   
#         print("parent name:",self.p_name ,"\n","parent age:",self.p_age)
# class child(parent):
#     def method2(self):
#         self.c_name='sankar'
#         self.c_age=25  
#         print("parent name:",self.c_name ,"\n","parent age:",self.c_age)
# obj=child()
# obj.method()
# obj.method1()
# obj.method2()        

# # multilevel inheritence with overriding  
# class grand_parent():
#     def method(self):
#         self.gp_name='sambaiah'
#         self.gp_age=81
#         print("grand parent name:",self.gp_name ,"\n","grand parent age:",self.gp_age)
# class parent(grand_parent):
#     def method(self):
#         super().method()
#         self.p_name='veeraiah'
#         self.p_age=56   
#         print("parent name:",self.p_name ,"\n","parent age:",self.p_age)
# class child(parent):
#     def method(self):
#         super().method()
#         self.c_name='sankar'
#         self.c_age=25  
#         print("parent name:",self.c_name ,"\n","parent age:",self.c_age)
# obj=child()
# obj.method()
