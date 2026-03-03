# # method overriding
# class g_parent():
#     def method(self,g_name,g_age):
#         self.g_name=g_name
#         self.g_age=g_age
# class parent(g_parent):
#     def method(self,g_name,g_age,p_name,p_age):
#         super().method(g_name,g_age)
#         self.p_name=p_name        
#         self.p_age=p_age
# class child(parent):
#     def method(self,g_name,g_age,p_name,p_age,c_name,c_age):
#         self.c_name=c_name
#         self.c_age=c_age
#         super().method(g_name,g_age,p_name,p_age)
#         print('grand father name:',self.g_name)        
#         print('grand father age:',self.g_age)
#         print('father name:',self.p_name)
#         print('father age:',self.p_age)
#         print('child name:',self.c_name)
#         print('child age:',self.c_age)
# obj=child()  
# obj.method('shiva',78,'sankar',50,'gopi',23)

# # constructor overrding
# class master():
#     def __init__(self,m_name,m_salary):
#         self.m_name=m_name
#         self.m_salary=m_salary
# class student(master):
#     def __init__(self,m_name,m_salary , s_name, s_salary):
#         self.s_name=s_name
#         self.s_salary=s_salary

#         super().__init__(m_name,m_salary) 

# class learner(student):
#     def __init__(self, m_name,m_salary ,s_name, s_salary,l_name, l_salary):

#         super().__init__(m_name,m_salary ,s_name,s_salary)               
#         print('master name,salary:',m_name,",",m_salary)
#         print('student name,salary:',s_name,",",s_salary)
#         print('learner name,slary:',l_name,",",l_salary)

# obj=learner('shankar',35000,'shiva',25000,'chakri',15000)






