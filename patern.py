# n=5
# for rows in range(1,n+1):
#     for cols in range(1,n-rows+2):
#         print(chr(64+cols),end=" ")
#     print()
# print()

# for rows in range(1,n+1):
#     for cols in range(1,n-rows+2):
#         print(chr(96+cols),end=" ")
#     print()    
# print()

# for rows in range(1,n+1):
#     for space in range(1,n-rows+1):
#         print(" ",end="")
#     for cols in range(1,rows+1):
#         if cols==1 or cols==rows or rows==n:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")    
#     print()               

# for row in range(1,6):
#     for col in range(1,row+1):
#         print(chr(64+col),end=" ")
#     print() 
# print()   

# for row in range(1,6):
#     for col in range(1,6):
#         if col==1 or row==5 or row==2 and col in [1,2] or row==3 and col in [1,3] or row==4 and col in[1,4]:
#             print(col ,end=" ")
#         else:
#             print(" ",end=" ")
#     print()    
# print()

# for i in range(1,6):
#     for j in range(1,6):
#         if i==1 and j in [1,5] or i==2 and j in [2,4] or i==3 and j==3 or i==4 and j in [2,4] or i==5 and j in [1,5]:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")        
#     print()   
# print()

# A=65
# for i in range(1,6):
#     for j in range(1,6):
#         print(chr(A),end=" ")
#         A+=1
#     print()  
# print()               

# for i in range(1,6):
#     for j in range(1,i+1):
#         if i==1 or i==2 and j==2 or i==3 and j in [1,3] or i==4 and j in [2,4] or i==5 and j in [1,3,5]:
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#     print()            
# print()