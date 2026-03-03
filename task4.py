# 1. Print numbers from 1 to 10.
for i in range(1,11):
    print(i)
print()    
# 2. Print all even numbers from 1 to 20.
for i in range(1,21):
    if i%2==0:
        print(i)
print()
# 3. Print all odd numbers from 1 to 20.
for i in range(1,21):
    if i%2!=0:
        print(i)
print()
# 4. Print numbers from 10 to 1 in reverse order.
n=10
for i in range(n,0,-1):
    print(i)
print() 

# 5. Print the square of each number from 1 to 10.
for i in range(1,11):
    print(i**2)
print()    

# 6. Print the multiplication table of a given number (e.g., 5).
j=5
for i in range(1,11):
    print(i*j)
print() 

# 7. Find the sum of numbers from 1 to 100.
i=100
print((i*(i+1))//2)
print() 

# 8. Find the product of numbers from 1 to 10 (i.e., factorial of 10).
k=1
for i in range(1,11):
    k*=i
print(k)    

# 9. Print all numbers from 1 to 50 that are divisible by 5.
t=5
for i in range(1,51):
    if i%t==0:
        print(i)
print()

# 10. Print all numbers from 1 to 30 that are divisible by both 2 and 3
for i in range(1,31):
    if i%2==0 and i%3==0:
        print(i)
print()        