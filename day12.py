# 1. Rearrange Even & Odd Indexed Elements
# Given a list, place elements at even indices first, then odd indices.
# Example: [10, 20, 30, 40, 50] → [10, 30, 50, 20, 40].

# l=[10,20,30,40,50]
# t=[]
# s=[]
# for i in range(len(l)):
#     if i%2==0:
#         t.append(l[i])
#     else:
#         s.append(l[i])
# print(t+s)   


# 2. Flatten a Nested List
# Convert a 2D list into a 1D list.
# Example: [[1, 2], [3, 4], [5]] → [1, 2, 3, 4, 5]
t=[[1, 2], [3, 4], [5]]
k=[]
for i in t:
    for j in i:
        k.append(j)
print(k)    


# 3.Second Largest & Second Smallest
# Find the second largest and second smallest numbers in a list.
# l1=[10, 30, 50, 20, 40, 10, 20, 4, 45, 99, 6]
# for i in range(len(l1)):
#     for j in range(i+1,len(l1)):
#         if l1[i]>l1[j]:
#             l1[i],l1[j]=l1[j],l1[i]
# print(l1)
# print("second highest is:",l1[-2])
# print("second lowest is:",l1[1])     