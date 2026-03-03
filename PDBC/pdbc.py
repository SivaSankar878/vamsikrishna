import mysql.connector
import random
sql="create database IF NOT EXISTS bank_pdbc"
con=mysql.connector.connect(user='root',host='localhost',password='Siva@2002')
cursor=con.cursor()
cursor.execute(sql)
cursor.execute('use bank_pdbc')
cursor.execute('''create table IF NOT EXISTS hol_det(hol_name VARCHAR(50),aadhar_no BIGINT,mobile BIGINT,ifsc VARCHAR(20),acc_no BIGINT,acc_type VARCHAR(50),balance INT)''')
class Bank:
    def create_account(self):
        h_name=input('Enter holder name:')
        aa_no=int(input("enter aadhar number:"))
        mobile_no=int(input("Enter mobile number:"))
        ifsc="PUNB059100"
        ac_no=random.randint(590100010000,590100099999)
        ac_type=input("enter type of account==>savings/zero:")
        balance=500 if ac_type=='savings' else 100
        insert_data="insert into hol_det values('%s',%s,%s,'%s',%s,'%s',%s)"
        cursor.execute(insert_data%(h_name,aa_no,mobile_no,ifsc,ac_no,ac_type,balance))
        con.commit()
    def deposit(self):
        acc_no=int(input("Enter account number:"))
        deposit_amount=int(input("enter deposit amount:"))
        cursor.execute('update hol_det set balance=balance+%s where acc_no=%s',(deposit_amount,acc_no))
        con.commit()
    def withdraw(self):
        acc_no=int(input("Enter account number:"))
        withdraw_amount=int(input("enter withdraw amount:"))
        cursor.execute(f'select balance from hol_det where acc_no={acc_no}')
        data=cursor.fetchone()
        if withdraw_amount<data[0]:
            cursor.execute('update hol_det set balance=balance-%s where acc_no=%s',(withdraw_amount,acc_no))
        else:
            print("Check your balance")
        con.commit()
    def check_balance(self):
       acc_no=int(input("Enter account number:"))
       cursor.execute(f'select balance from hol_det where acc_no={acc_no}')
       data=cursor.fetchone()
       print("Your balance is:",data[0])
    def details(self):
        acc_no=int(input('enter account number:'))
        cursor.execute(f'select * from hol_det where acc_no={acc_no}')
        data=cursor.fetchone()
        print(f'''\n holder details
              holder name:{data[0]}
              aadhar number:{data[1]}
              mobile number:{data[2]}
              ifsc:{data[3]}
              account number:{data[4]}
              account type:{data[5]}
              balance:{data[6]}''')
        
obj=Bank()
while True:
    print('''
          1.create account
          2.deposite
          3.withdraw
          4.check balance
          5.details
          6.exit''')
    n=int(input('select your choice:'))
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
        print('Enter correct choice')
con.close()