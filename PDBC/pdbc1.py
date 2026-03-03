import random
import mysql.connector
con=mysql.connector.connect(user='root',host='localhost',password='Siva@2002')
cursor=con.cursor()
sql='create database IF NOT EXISTS punb'
cursor.execute(sql)
cursor.execute('use punb')
cursor.execute('''create table bank_account(holder_name varchar(50),age int,aadhar_no bigint,mobile bigint
    ,ifsc varchar(20),account_type varchar(20),account_number bigint,address varchar(50),balance int)''')
class Bank:
    def create_account(self):
        h_n=input("Enter holder name:")
        h_a=int(input('Enter holder age:'))
        a_n=int(input('Enter aadhar number:'))
        m_n=int(input('Enter mobile number:'))
        ifsc='PUNB0590100'
        a_t=input('Select account type ==> savings/zero:')
        acc_no=random.randint(5901000100010000,5901000100019999)
        address=input('Enter Your Adress:')
        bal=1000 if a_t=='savings' else 100
        insert_data="insert into bank_account values('%s',%s,%s,%s,'%s','%s',%s,'%s',%s)"
        cursor.execute(insert_data%(h_n,h_a,a_n,m_n,ifsc,a_t,acc_no,address,bal))
        print('Your Account Was Sucessfully Created!!!!....')
        con.commit()
    def deposit(self):
        print('Welcome to the deposite section!!!!')
        a_no=int(input('Enter Account Number to deposite:'))
        d_a=int(input('Enter Amount to deposite:'))
        cursor.execute('update bank_account set balance=balance+%s where account_number=%s',(d_a,a_no))
        print('Amount deposited Sucessfully...')
        con.commit()
    def withdraw(self):
        print('Welcome to the withdraw section!!!!')
        acc_no=int(input('Enter Account number:'))
        wi_am=int(input('Enter amount to withdraw:'))
        cursor.execute(f'select balance from bank_account where account_number={acc_no}')
        data=cursor.fetchone()
        if wi_am<data[0]:
            cursor.execute('update bank_account set balance=balance-%s where account_number=%s',(wi_am,acc_no))
            print('Amount Withdraw Sucessfully....')
        else:
            print('Check your balance')
        con.commit()
    def check_balance(self):
        print('This is Check Balance section.......')
        acc_no=int(input('Enter account number:'))
        cursor.execute(f'select balance from bank_account where account_number={acc_no}')
        data=cursor.fetchone()
        print('Your balance is:',data[0])
    def details(self):
        print('This is Details section.......')
        acc_no=int(input('Enter account number:'))
        cursor.execute(f'select * from bank_account where account_number={acc_no}')
        data=cursor.fetchone()
        print(f'''\n Holder Details 
                Holder_Name:{data[0]} 
                Holder_Age:{data[1]} 
                Aadhar_Number:{data[2]} 
                Mobile_Number:{data[3]} 
                IFSC:{data[4]} 
                Account_Type:{data[5]} 
                Account_Number:{data[6]} 
                Address:{data[7]} 
                Balance:{data[8]}''')
obj=Bank()
while True:
    print('''1.Create Account
            2.Deposit
            3.Withdraw
            4.Check Balance
            5.Details
            6.Exit''')
    n=int(input('Please select an option:'))
    if n==1:
        obj.create_account()
    elif n==2:
        obj.deposit()
    elif n==3:
        obj.withdraw()
    elif n==4:
        obj.check_balance()
    elif n==5:
        obj.details()
    elif n==6:
        break
    else:
        print('please select correct option')
con.close()