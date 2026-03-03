# here is a small game rock, paper,scissor game.
import random
options=['rock','paper','scissor']
user_choice=input('enter a option:').lower()
computer_choice=random.choice(options)
if user_choice==computer_choice:
    print(" it's a tie!!")
elif (user_choice=='rock' and computer_choice=='scissor') or (user_choice=='paper' and computer_choice=='rock') or (user_choice=='scissor' and computer_choice=='paper'):
    print('user win')
else:
    print("computer win")    