# # single inheritence
# class parent():
#     def skill(self):
#         self.p_name='siva'
#         self.p_age=45
#         print('parent class:',self.p_name,self.p_age)
# class child(parent):
#     def skills(self):
#         self.c_name='sankar'
#         self.c_age=24  
#         print('child class:',self.c_name,self.c_age)
# obj=child()
# obj.skill()  
# obj.skills()  

# # single inheritence with overriding
# class parent():
#     def skill(self):
#         self.p_name='siva'
#         self.p_age=45
#         print('parent class:',self.p_name,self.p_age)
# class child(parent):
#     def skill(self):
#         super().skill()
#         self.c_name='sankar'
#         self.c_age=24  
#         print('child class:',self.c_name,self.c_age)
# obj=child()
# obj.skill()