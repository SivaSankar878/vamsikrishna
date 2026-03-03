from abc import ABC,abstractmethod
import random
class Bank():
    @abstractmethod
    def create_account(self):
        pass
    @abstractmethod
    def deposite(self):
        pass 
    @abstractmethod
    def withdraw(self):
        pass
    @abstractmethod
    def details(self):
        pass
class PUNB(Bank):
    def create_account(self):
        self.holder_name=input("enter your name:")
        self.mobile_no=int(input('enter your mobile number:'))
        self.acc_no=random.randint(0000000000,9999999999)   
        self.ifcs='PUNB590100'
        self.balance=int(input('enter some amount to open the account:'))
        print('<-----Account Was Sucessfully Created----->')
        print("Account number is:",self.acc_no)
    def deposite(self):
        self.holder_name=input('enter a holder name:')
        self.Ac_no=int(input('enter account number to deposite amount:'))
        self.deposite_amount=int(input('enter amount to deposite:'))
        if self.acc_no==self.Ac_no:
            self.balance+=self.deposite_amount
            print("<---Amount was deposite succesfully---> \n Your Balance is:",self.balance)
        else:
            print("<---Amount was  not deposited---> \n Please Check Your Balance ")    
    def withdraw(self):
        self.holder_name=input('enter a holder name:')
        self.Ac_no=int(input('enter account number to withdraw:'))
        self.with_amount=int(input('enter withdraw amount:'))
        if self.acc_no==self.Ac_no and self.balance>self.with_amount:
            print("<----Before withdraw----> \n Your account balance is:",self.balance)
            self.balance-=self.with_amount
            print("<----After withdraw----> \n Your account balance is:",self.balance)
        else:
            print('Withdraw amount is morethan Balance,Please Check Your Balance') 
    def details(self):
        self.Ac_no=int(input('enter account number to get details:'))
        if self.acc_no==self.Ac_no:
            print('Account holder name:',self.holder_name)
            print('Account number is:',self.acc_no)
            print('IFCS code of the holder is:',self.ifcs)
            print('Balance Amount is:',self.balance)
            print('Account holder Mobile number is:',self.mobile_no)
obj=PUNB()
while True:
    print('1.Create a account \n 2.Deposite \n 3.Withdraw \n 4.Details \n 5.Exit')
    ch=int(input("Enter Your choice:"))
    if ch==1:
        print('<---Welcome to our bank--->')
        obj.create_account()
    elif ch==2:
        print('<---Welcome to deposite section--->')
        obj.deposite()
    elif ch==3:
        print('<---Welcome to withdraw section--->')
        obj.withdraw()
    elif ch==4:
        print('<---Welcome to details section--->')
        obj.details()
    elif ch==5:
        print('Thank you for banking with us!!!...')
        break    
    else:
        print('Invalid choice,enter correct choice:')                          

                
