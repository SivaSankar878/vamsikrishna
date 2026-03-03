# # LCM - lowest common multipler
# # ex-8,12
# # multiplers of(8)-8,16,24,32,40,48,56,64,72
# # multiplers of(12)-12,24,36,48,60,72,84,96
# # in the above multiplers we can see 48,72 on both but 48 is the lowest common multipler in both so that is the lcm of 8,12
# # here we write a program
# def Lcm(a,b):
#     k=a if a>b else b  
#     for i in range(k,a*b+1):
#         if i%a==0 and i%b==0:
#             print(i)
#             break
# Lcm(8,12)   

# # HCF-highest common factor
# # ex-8,12
# # factors of (8)-1,2,4
# # factors of (12)-1,2,3,4,6
# # in the above two factors 4 is the highest factors in both so 4 is the hcf of 8,4
# # here we write a program
# def Hcf(a,b):
#     hcf=0
#     k=a if a<b else b
#     for i in range(1,k+1):
#         if a%i==0 and b%i==0:
#             hcf=i
#     print(hcf)    
# Hcf(8,12)        
