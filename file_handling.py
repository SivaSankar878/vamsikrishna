# # file handling
# # there are functions and modes
# # functions->open(),close(),read(),write()
# # modes-> x->create a new file,w->create a new file and write,a->append data into a existing file,r->read a file
# # syntax to use this (variable=function name('file name','mode')).
# k=open('file1.txt','x') #create a new file
# l=open('file2.txt','w')
# l.write('hey this is file handling') #creating a new file and write some content

# k=open('file1.txt','x')
# k.write('this is file1') #in above line create a new file but we cant give text in it because it is also created

# k=open('file3.txt','x')
# k.write('this is a new file with some text') #by using thisn create we can create  a new file and give text.

# l=open('file2.txt','w')
# l.write('this is a changed text') #we can give some text on a existing file but the data before writing is deleted.

# j=open('file2.txt','r')
# d=j.read()
# print(d)

# h=open('sum.py','r')
# k=h.read()
# print(k)
# h.close()

# with open('sum.py','r') as k:
#     d=k.read()
#     print(d)

# c=open('file3.txt','a')
# c.write(' java is added without clearing the content')

# j=open('file3.txt','r')
# j.seek(11)
# k=j.read()
# print(k)

# j=open('file3.txt','r')
# j.seek(0)
# # print(j.tell())
# k=j.read()
# print(k)

# with open('file53.txt','w+') as k:
#     k.write('good night guys!!!')
#     k.seek(0)
#     d=k.read()
#     print(d)

# with open('ch.txt','w+') as c:
#     c.write('this is a normal text')
#     c.seek(0)
#     d=c.read()
#     print(d)

# with open('file2.txt','r+') as r:
#     print(r.read())

# with open('file2.txt','r+') as d:
#     s=d.read()
#     print(s)
#     d.write('this is r+ mode')

# h=open('file2.txt','a+')
# h.write(' this is a+ mode')
# h.seek(0)
# d=h.read()
# print(d)

# read() ->used to access the all the data
# readline() ->used to print one by one line
# readlines() ->display the content in a list data type

# with open('file2003.txt','w') as m:
#     m.write('this is first line \n this is second line \n this is third line ')

# b=open('file2003.txt','r')
# k=b.read()
# print(k)   # read() ->used to access the all the data

# b=open('file2003.txt','r')
# print(b.readline())   # readline() ->used to print one by one line
# print(b.readline())

# c=open('file2003.txt','r')
# print(c.readlines())  #->display the content in a list data type

# #transfer data from one file to another file

# n=open('sum.py','r')
# m=open('file2004','w')
# d=n.read()
# m.write(d)

# k=open('patern.py','r')
# l=open('file2001.py','w')
# m=k.read()
# l.write(m)

# #transfer image from one file to another file

# n=open('anupama.jpg','rb')
# n1=open('newfile.jpg','wb')
# d=n.read()
# n1.write(d)

# #remove or delete a file 
 
# import os 
# if os.path.exists('file2001.py'):
#     os.remove('file2001.py')
# else:
#     print('file not exist')    

# k=open('siva123.txt','w+')
# l=k.read()
# m=k.write('siva sankar')
# print(m)

# import os
# if os.path.exists('siva123.txt'):
#     os.remove('siva123.txt')
# else:
#     print('file not found')    

# # length of the file

# k=open('file53.txt','r')
# l=k.read()
# print(len(l))

# #find lines in file
# b=open('file2003.txt','r')
# d=b.readlines()
# cou=0
# for i in d:
#     cou+=1
# print(cou)    

import pyttsx3
k=pyttsx3.init()
k.say('hey siva')
k.runAndWait()