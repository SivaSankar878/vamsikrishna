'pip install pyttsx3' 
# import pyttsx3

# k = 'Welcome to Python world'

# j = pyttsx3.init()
# voices = j.getProperty('voices')
# j.setProperty('voice', voices[0].id)
# j.setProperty('rate', 150)

# j.say(k)
# j.runAndWait()

# import pyttsx3
# import time

# j = pyttsx3.init()
# k=['siva','sankar','chakri','gopi']
# a={}
# for i in k:
#     j.say(i)
#     j.runAndWait()
#     time.sleep(1)
#     n=input("enter attendence:" )
#     if n=='p':
#         a[i]='Present'
#     else:
#         a[i]='Absent'    
# print(a)

# l=['apple','banana','mango']
# for i,l1 in enumerate(l,start=10):
#     print(i,l1)

# Random password generator
# import random
# import string
# pas_len=10
# ch=string.ascii_letters+string.digits+string.punctuation
# password=''.join(random.choices(ch,k=pas_len))
# print(password)

# n=5
# for row in range(n,0,-1):
#     print(" "*(n-row),end=" ")
#     for col in range(row):
#         print(chr(65+col),end=" ")
#     print()   

# import pyttsx3
# import time
# k=pyttsx3.init()
# l=['Gopi','sankar','tati']
# voices = k.getProperty('voices')
# k.setProperty('voice', voices[1].id)
# k.setProperty('rate', 150)

# for i in l:
#     k.say(i)
# k.runAndWait()

# import random
# import string
# def pass_che():
#     s=input('enter password:')
#     pas_len=int(input('enter pasword length:'))
#     ch=string.ascii_letters+string.digits+string.punctuation
#     l=''.join(random.choices(ch,k=pas_len))
#     while True:
#         if l==s:
#             print('found')
#             break
#         else:
#             print('notfound')    
# pass_che()

# import random
# print(random.random()) 
# print(random.randint(10,20))  
# print(random.uniform(10,20)) #random float values.
# print(random.randrange(10,20,1))
# h='abcdefghijklmnopqrstuvwxyz'
# print(random.choice(h)) #choice is used to pic a single char.
# print(random.choices(h,k=35)) #choices is used to pic morethan a single char,take more than index range.
# print(random.sample(h,k=10))  #sample is used to pic morethan a single char,it don't take more than index range.
# random.seed(5)  #random.seed() is used to the constant value for n times.
# print(random.random())
# l=[10,20,30,40,50]
# random.shuffle(l)
# print(l)

# import random
# p1=0
# p2=0
# while True:
#     n1=input('press Enter of p1:')
#     if n1=="":
#         c=random.randint(1,10)
#         p1+=c
#         if p1>=20:
#             print('player1 is win,score is:',p1)
#             break
#     n2=input('press Enter of p2:')
#     if n2=="":+
#         c1=random.randint(1,10)
#         p2+=c1
#         if p2>=20:
#             print('player2 is win,score is:',p2) 
#             break



import pyttsx3

a=pyttsx3.init()

voices=a.getProperty('voices')

a.setProperty('voice',voices[0].id)

a.setProperty('rate',150)

a.say('hii siva sankar,welcome to python pyttsx3')
 
a.runAndWait() 


# help('modules')   

#using if else conditions
n=int(input('enter the number of units:'))
current_bill=0
if n<=100:
    current_bill=n*5
elif n<=200:
    current_bill=(100*5)+(n-100)*7
else:
    current_bill=(100*5)+(100*7)+(n-200)*10     
print(current_bill) 

