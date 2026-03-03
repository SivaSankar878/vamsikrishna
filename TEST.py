# 1. Write a program to find the frequency of each character in a string. 
# t=input()
# for i in t:
#     cou=0
#     for j in t:
#         if i==j:
#             cou+=1
#     print(i,'=',cou)            
# 2. Write a program to count the number of words in a sentence. 
# 3. Write a program using a loop to print the multiplication table of a number.
# n=5
# for i in range(1,n):
#     if i==4:
#         for j in range(1,11):
#             print(i,"X",j,"=",i*j) 
# 4. Write a program using a loop to print all prime numbers between 1 and 50. 
s = int(input("Enter start: "))
e = int(input("Enter end: "))

for n in range(s, e+ 1):
    if n > 1:   
        cou = 0
        for i in range(2, n):
            if n % i == 0:
                cou += 1
        if cou == 0:   
            print(n)

                                
# 5. Write a program using a loop to calculate factorial of a number.   
# 6. Write a program using a loop to print Fibonacci series up to n terms. 
# 7. Write a program using a loop to find the sum prime  digits in a number. 