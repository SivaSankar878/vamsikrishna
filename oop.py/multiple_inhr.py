# # multiple inheritence
# class father():
#     def method1(self):
#         self.f_name='veeraiah'
#         self.f_age=56
#         print("father name is:",self.f_name,"\n","father age is:",self.f_age)
# class mother():
#     def method2(self):
#         self.m_name='sarada'
#         self.m_age=51
#         print("mother name is:",self.m_name,"\n","mother age is:",self.m_age)   
# class child(father,mother):
#     def method3(self):
#         self.c_name='sankar'
#         self.c_age=25
#         print("child name is:",self.c_name,"\n","father age is:",self.c_age)   
# obj=child()
# obj.method1()          
# obj.method2()
# obj.method3()

# # multiple inheritence wth overriding
# class father():
#     def method(self):
#         self.f_name='veeraiah'
#         self.f_age=56
#         print("father name is:",self.f_name,"\n","father age is:",self.f_age)
#         super().method()
# class mother():
#     def method(self):
#         self.m_name='sarada'
#         self.m_age=51
#         print("mother name is:",self.m_name,"\n","mother age is:",self.m_age)   
# class child(father,mother):
#     def method(self):
#         super().method()
#         self.c_name='sankar'
#         self.c_age=25
#         print("child name is:",self.c_name,"\n","father age is:",self.c_age)   
# obj=child()
# obj.method()

# class father():
#     def method(self):
#         self.f_name='veeraiah'
#         self.f_age=56
#         print("father name is:",self.f_name,"\n","father age is:",self.f_age)
# class mother():
#     def method(self):
#         self.m_name='sarada'
#         self.m_age=51
#         print("mother name is:",self.m_name,"\n","mother age is:",self.m_age)   
# class child(father,mother):
#     def method(self):
#         father.method(self) #accesing without super and using class name
#         mother.method(self) #accesing without super and using class name
#         self.c_name='sankar'
#         self.c_age=25
#         print("child name is:",self.c_name,"\n","father age is:",self.c_age)   
# obj=child()
# obj.method()