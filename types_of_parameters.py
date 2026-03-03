# # positional arguments
# def std(name,age,marks,ph_no):
#     print('name:',name)
#     print('age:',age)
#     print('marks:',marks)
#     print('ph_no:',ph_no)
# std('sankar',23,97,9177168356) 
# print()

# # keyword arguments
# def std(name,age,marks,ph_no):
#     print('name:',name)
#     print('age:',age)
#     print('marks:',marks)
#     print('ph_no:',ph_no)
# std(ph_no=9177168356,name='sankar',age=23,marks=97)

# # default arguments
# def std(name,age,marks,ph_no=9177168356):
#     print('name:',name)
#     print('age:',age)
#     print('marks:',marks)
#     print('ph_no:',ph_no)
# std('sankar',23,97)

# # variable length arguments
# def add1(*a):
#     print(sum(a))
# add1(10,20)
# print()
# add1(10,20,30)
# print()
# add1(10,20,30,40)
# print()


# def add1(*a):
#     sum=0
#     for i in a:
#         sum+=i
#     print(sum)
# add1(10,20,30,40)        

# keyword length argument
# def fun(**a):
#     print(a)
# fun(age=16,name='sankar',marks=87)    

# def fun(a,b,*c,**d):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
# fun(10,20,30,40,50,name='sankar',age=19,address='guntur')

# def name():
#     global a 
#     a='siva'
#     print(a)
# name()
# print(a)    

# a=100
# def fun():
#     a=200
#     print(a)
# fun()
# print(a)    

# a=100
# def fun():
#     global a
#     a+=200
#     print(a)
# fun()
 
# a=100
# def fun():
#     b=500
#     print(a+b)
# fun()

# def f1():
#     a=100
#     def f2():
#         print(a)
#     f2()
# f1()          

# def f1():
#     a=100
#     def f2():
#         nonlocal a
#         a+=2000
#         print(a)
#     f2()
# f1()