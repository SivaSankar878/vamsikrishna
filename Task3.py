# 1.	A company gives a discount based on purchase amount:
# If purchase amount > 5000 → 20% discount
# If purchase amount between 2000–5000 → 10% discount
# Otherwise → No discount
purchase_amount=10000
if purchase_amount >=5000:
    discount=purchase_amount*0.20
    print(discount)
elif purchase_amount >2000 and purchase_amount<5000:
    discount=purchase_amount*0.10
    print(discount)
else:
    print('no discount')    

# 2.	Write a program that accepts a 4-digit ATM PIN from the user. If correct → display “Access Granted”, else “Access Denied”.
ATM_PIN="1234"
correct_PIN="7234"
if ATM_PIN==correct_PIN:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")    
# 3.	Write a Python program to accept a number of days from the user and convert it into years, months, and days.
Days=1935
years=Days//365
Days=Days%365
months=Days//30
Days=Days%30
weeks=Days//7
Days=Days%7
print("years:",years,"months:",months,"weeks:",weeks ,"days:",Days)

# 4.	Write a Python program to accept an amount in rupees and convert it into the minimum number of currency notes of ₹500, ₹200, ₹100, ₹50, ₹20, ₹10, ₹5, ₹2, and ₹1.
amtrupess=976531
note500=amtrupess//500 
rem500notes=amtrupess%500 
note200=rem500notes//200 
rem200notes=rem500notes%200 
note100=rem200notes//100 
rem100notes=rem200notes%100 
note50=rem100notes//50 
rem50notes=rem100notes%50 
note20=rem50notes//20 
rem20notes=rem50notes%20 
note10=rem20notes//10 
rem10notes=rem20notes%10 
coin5=rem10notes//5 
rem5coins=rem10notes%5 
coin2=rem5coins//4 
rem2coins=rem5coins%4 
lastrem=rem2coins//1 
print(f'{note500} five hundered notes, {note200} two hundred notes, {note100} hundred notes, {note50} fifty notes, {note20} tweenty notes, {note10} ten notes, {coin5} five rupee coins, {coin2} two rupee coins, {lastrem} one rupee coin')