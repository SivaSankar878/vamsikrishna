"""#finding the largerst number in array between the range
arr=[1,3,-1,-3,5,3,6,7]
k=3
n=len(arr)
result=[]
for i in range(n-k+1):
    max_value=arr[i]
    for j in range(i,i+k):
        if arr[j]>max_value:
          max_value=arr[j]
    result.append(max_value)
    s=print(max_value,end="")""" 

"""array.sort()
ss=array[1]
sl=array[-2]
print(array) 
print(max(array)) 
print(min(array)) 
print(ss)
print(sl)"""
#unique and repeated elements in a array
n=int(input("enter how many values in array:"))
array=list(map(int,input(f"enter {n} separated values:").split()))
unique=[]
repeat=[]
seen=set()
for i in array:
    if i not in seen:
       unique.append(i)
       seen.add(i)
    else:
        if i not in repeat:
          repeat.append(i) 
print(unique)
print(repeat)            
 


