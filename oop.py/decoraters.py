# def is_prime(prime):
#     def inner(s):
#         l=[i for i in range(2,s) if len([j for j in range(2,i) if i%j==0])==0]
#         print(l)
#     return inner    
# @is_prime
# def prime(a):
#     print(a)
# prime(22)    

def is_prime(prime):
    def inner(s):
        c=0
        for i in range(2,s):
            if s%i==0:
                c+=1
        if c==0:        
            print('prime')
        else:
            print('not a prime')    
        
    return inner    
@is_prime
def prime(a):
    print(a)
prime(19)
prime(11)
prime(22)