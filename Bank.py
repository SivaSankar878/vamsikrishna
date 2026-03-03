# Write a nested function to perform the following on a bank account:
# Deposit amount
# Withdraw amount
# Check balance
# Use nonlocal to update the balance inside inner functions.
def bank():
    a=1000
    def dep_amo():
        nonlocal a
        d_a=int(input("enter deposite amount:"))
        a=a+d_a
        print("amount deposited. current amount",a)
    def wit_amo():
        nonlocal a
        w_a=int(input("enter withdrawal amount:"))
        if w_a>a:
            print("insufficient balance!")
        else:
            a=a-w_a
            print("amount withdrawn. current balance:",a)
    def che_amo():
        print("current balance:",a)
    while True:
        print("\n 1.Deposit\n 2.Withdraw\n 3.Check Balance\n 4.Exit")
        c=int(input("enter your choice:"))
        if c==1:
            dep_amo()
        elif c==2:
            wit_amo()
        elif c==3:
            che_amo()
        elif c==4:
            print("thankyou")
            break
        else:
            print('invalid choice please try again')                 
bank()

# calculator
def calculator():
    def addition():
        a=int(input('enter the first value:'))
        b=int(input('enter the second value:'))
        print("The addition of two values:",a+b)
    def subtraction():
        a=int(input('enter the first value:'))
        b=int(input('enter the second value:'))
        print("The subtraction of two values:",a-b) 
    def multiplication():
        a=int(input('enter the first value:'))
        b=int(input('enter the second value:'))
        print("The multiplication of two values:",a*b)   
    def modulus():
        a=int(input('enter the first value:'))
        b=int(input('enter the second value:'))
        if b==0:
            print('zero error')
        else:    
            print("The modulus of two values:",a%b)
    def floor_division():
        a=int(input('enter the first value:'))
        b=int(input('enter the second value:'))
        if b==0:
            print('zero error')
        else:
            print("The floor division of two values:",a//b)
    def division():
        a=int(input('enter the first value:'))
        b=int(input('enter the second value:'))
        if b==0:
            print('zero error')
        else:    
            print("The division of two values:",a/b)        
    def power():
        a=int(input('enter the first value:'))
        b=int(input('enter the second value:'))
        print("The power of two values:",a**b) 
    while True:
        print('1.Addtion\n2.Subtraction\n3.Multiplication\n4.Modulus\n5.Floor Division\n6.Division\n7.Power\n8.Exit')
        ch=int(input('enter a choice:'))
        if ch==1:
            addition()
        elif ch==2:
            subtraction()
        elif ch==3:
            multiplication()
        elif ch==4:
            modulus()
        elif ch==5:                    
            floor_division()
        elif ch==6:
            division()
        elif ch==7:
            power()
        elif ch==8:
            break
        else:
            print('enter your choice correctly:')
calculator()             



   