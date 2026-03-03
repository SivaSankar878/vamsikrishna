# import random
# print(random.random())

# import random
# n=5
# while True:
#     k=random.randint(1,20)
#     if k==n:
#         print('correct guess:',k)
#         break
#     else:
#         print('not a correct guess:',k)


# #1.Write a Python program to generate a password using the random module. The user should input how many alphabets, special characters, and numbers they want in the password.
# import random
# import string
# def password():
#     k=''
#     spc=int(input("enter the number to give how many special charectres you need in your password:"))  
#     for i in range(1,spc+1):
#         s=random.choice(string.punctuation)
#         k+=s  
#     chr=int(input("enter the number to give how many charectres you need in your password:"))  
#     for i in range(1,chr+1):
#         c=random.choice(string.ascii_lowercase)
#         k+=c
#     num=int(input("enter the number to give how many numbers you need in your password:"))
#     for i in range(1,num+1):
#         n=random.choice(string.digits)
#         k+=n     
#     print(k)
# password()            

# #2.Write a Python program to play a “Guess the Number” game using the random module.
# import random
# def guess():
#     n=int(input("enter a number:"))
#     while True:
#         k=random.randint(1,1000)
#         if n==k:
#             print('correct guess, the number is',k)
#             break
#         else:
#             print('too high try again')       
# guess()  
      
# #3.Write a Python program for a two-player game where the first player to reach 20 points wins, using the random module.
# import random
# def win():
#     Raju=0
#     Gopi=0
#     while True:
#         R=random.randint(1,10)
#         Raju+=R
#         G=random.randint(1,10)
#         Gopi+=G
#         if Raju>20:
#             print('Raju won the game, Score is:',Raju)
#             break
#         if Gopi>20:
#             print('Gopi won the game, Score is:',Gopi) 
#             break
# win()
# import random 
# k=random.random() #it generates a number between 0 to 1
# print(k)

# k=random.randint(1,10) #it generates a number between the range
# print(k)

# k=random.randrange(1,100,10) #it generates a number between the range like for loop(start,stop,step)
# print(k)

# k=random.uniform(1,10) #it generates the float numbers between the range  
# print(k)

# k=random.choice('python',k=5) #it generates a single char
# print(k)

# l=random.choices('python',k=10) #it generate more chars based on k value,it returns in a list 
# print(l)

# random.seed(5) #by using seed in it generates same number every time
# print(random.randint(1,100))

# random.seed(5)
# print(random.choices('python',k=4)) #by using seed in it generates same  char every time
# print(random.choices('python',k=9))
# print(random.choices('python',k=7))

# n=[1,2,3,4,5,6]
# print(random.sample(n,k=1)) #sample generates more than one value like choices but it must be unique 
