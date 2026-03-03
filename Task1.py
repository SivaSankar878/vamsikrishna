#1.	Write a program to check whether a number is positive, negative, or zero.
number=25
if number==0:
	print('zero')
elif number>0:
	print('positive')
else:
	print('negative')		
	
#2.	Write a program to check whether a number is even or odd.
num1=99
if num1 % 2==0:
	print('even number')
else:
	print('odd number')	
	
#3.	Write a program to find the largest of two numbers.
A=27
B=98
if A>B:
	print('A is big')
else:
	print('B is big')	
	
#4.	Write a program to find the largest among three numbers.
a=99
b=45
c=675
if a>b & a>c:
	print('a is big')
elif b>c & b>a:
	print('b is big')
else:
	print('c is big')		

#5.	Write a program to check whether a person is eligible to vote (age ≥ 18).
age=24
if age>=18:
	print('eligible to vote')
else:
	print('not eligible to vote')	
	
#6.	Write a program to assign grades to a student based on marks:
# 	Marks ≥ 90 → A
# 	Marks ≥ 75 → B
# 	Marks ≥ 50 → C
# 	Otherwise → Fail
marks=97
if marks>=90:
	print('A')
elif marks>=75:
	print('B')
elif marks>=50:
	print('C')
else:
	print('Fail')	
			
#7.	Write a program to check whether a character is a vowel or consonant.
ch='O'
chr='AEIOUaeiou'
if ch in chr:
	print('vowel')
else:
	print('consonant')	
	
#8.	Write a program to check whether a number is a multiple of 3 and 5.
n=15
if n%3==0 and n%5==0:
	print('given number is a multiple of 3 and 5')
elif n%3==0:
	print('given number is a multiple of 3')
elif n%5==0:		
	print('given number is a multiple of 5')
else:
	print('given number is a multiple of 3 and 5')
		
#9.	Write a program to check whether a given character is uppercase, lowercase, digit, or special symbol.
charecter='a'
uc='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lc='abcdefghijklmnopqrstuvwxyz'
di='1234567890'
if charecter in uc:
	print('it contains in upper case')
elif charecter in lc:
	print('it contains in lower case')	
elif charecter in di:
	print('it contains in digits')
else:
	print('it contains in special symbol')	
		
#10.Write a program to check whether a number is divisible by 7 or not.
numb=765
if numb%7==0:
	print('numb is divisible by 7')
else:
	print('numb is not divisible by 7')
		
#11.Write a program to check whether a person is a senior citizen (age ≥ 60).
person_age=59
if person_age>=60:
	print('senior citizen')
else:
	print('not a senior citizen')	
		
#12.	Write a program to verify if a character is a vowel or consonant.
ch='O'
chr='AEIOUaeiou'
if ch in chr:
	print('vowel')
else:
	print('consonant')	