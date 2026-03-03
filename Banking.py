import random
class Bank():
   Holder_details=[]
   def Create_Account(self):
      Details={}
      Details['name']=input("Enter your name:")
      Details['Aadharno']=int(input("Enter your Aadharno:"))
      Details['mobile number']=int(input("Enter your mobile number:"))
      Details['IFCS code']='IFCS590100'
      # Details['Country']=input('Enter your country:')
      Details['Account Number']=random.randint(11111111111,99999999999)

      Account_Type=input("Select your account type Zero account or Savings account:").lower()

      while True:
        if Account_Type=='zero':
           n1=int(input('enter 500 to open zero account'))
           if n1>=500:
              Details['Balance']=n1
              break 
           else:
              print('please deposite 500 rupees')              
              
        elif Account_Type=='saving':
           n2=int(input('enter 1000 to open savings account'))
           if n2>=1000:
              Details['Balance']=n2
              break
           else:
              print('please deposite 1000 rupees')
      Bank.Holder_details.append(Details)
      print(Bank.Holder_details)

   def Deposite(self):
      while True:
         t1=input('enter holder name:')
         t2=int(input('enter account number:'))
         Deposite_amount=int(input('enter deposite amount:'))
         found=False
         for i in Bank.Holder_details:
            if i['Account Number']==t2 and i['name']==t1:
               i['Balance']+=Deposite_amount
               print('your balance amount is:',i['Balance'])
               print(i)
               found=True
               break
         if found:
            break
         else:
            print('Invalid account number or holder name.Try again!')
   def withdraw(self):
      r1=input('enter holder name:')
      r2=input('enter account number:')
      withdraw_amount=int(input('enter withdraw amount:'))
      
      for i in Bank.Holder_details:
         if i['Balance']>=withdraw_amount:
            i['Balance']-=withdraw_amount
            print('Balance:',i['Balance'])
            print(i)
         else:
            print('withdraw amount is greater than balance')

   def user_details(self) :
      m1=int(input('enter account number:'))
      for i in Bank.Holder_details:
         if i['Account number']==m1:
            for a,b in i.items():
               print(a,'==',b)

obj=Bank()
while True:
   print('Bank Menu /n 1.create account /n 2.Deposite /n 3.Withdraw /n 4.Details 5.Exit') 
   n3=input('select options:')
   if n3=='1':
      obj.Create_Account()
   elif n3=='2':
      obj.Deposite()
   elif n3=='3':
      obj.withdraw()
   elif n3=='4':
      obj.user_details()
   elif n3=='5':
      break                 

