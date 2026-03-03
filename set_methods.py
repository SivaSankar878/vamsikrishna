# set
# s={1,2,3,4,5,6,7,8,10}
# s.add(21) # by using add we can add only one element
# print(s)
# s.update([31,41,51]) # by using update we can add morethan one value
# print(s)
# s.pop() # by using pop we can only delete satrting element
# print(s)
# s.discard(10) # by using discard delete a particular value,if the set does not contain that paricular value it can't show any errors
# print(s)
# s.remove(10) #by using discard delete a particular value
# print(s)
# s.clear()#clear the set
# print(s)
# k=s.copy() #copy another duplicate
# print(k)
# s2={1,2,3,6,9,31,32,45}
# s2.issuperset(s)
# print("True")
# k=s.issubset(s2)
# print(k)
# y=s2.symmetric_difference(s)
# print(y)
# l=s2.intersection(s)
# print(l)
# k=s2.union(s) 
# print(k)
# o=s2.isdisjoint(s) #isdisjoint is used to check whether the two lists are contain different values or not
# print(o)
# s1={1,2,3,4,5,6}
# s2={3,4,2,8,9,10}
# print(s1-s2)
# print(s2-s1)
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))
# print(s2.difference(s1))
# print(s1.symmetric_difference(s2))

# d={'a':10,'b':11,'c':12,'d':13}
# for i,j in d.items():
#     if j%2==0:
#         d[i]*=2
# print(d)     

# 1️.Remove duplicates from the list: [5, 2, 3, 5, 4, 3, 2, 1] using a set.
# l1=[5, 2, 3, 5, 4, 3, 2, 1]
# k=set(l1)
# print(k)
# 2️.Create a set of unique  from the string "Programming".
# s="programming"
# k=set(s)
# print(k)
# 3️.Find the union of sets {1, 2, 3} and {3, 4, 5}.
# a={1, 2, 3}
# b={3, 4, 5}
# c=a.union(b)
# print(c)
# 4️. Find the intersection of sets {10, 20, 30} and {20, 30, 40, 50}.
# a={10, 20, 30}
# b={20, 30, 40, 50}
# t=a.intersection(b)
# print(t)
# 5️.Find the difference between {1, 2, 3, 4} and {2, 4}.
# a={1, 2, 3, 4}
# b={2, 4}
# i=a.difference(b)
# print(i)
# 6️. Check if {2, 3} is a subset of {1, 2, 3, 4, 5}.
# a={1, 2, 3, 4, 5}
# b={2, 3}
# print(b.issubset(a))
# 7.From the string "Hello World", create a set of unique characters.
# s="Hello World"
# k=set(s)
# print(k)
# 8.Add the element 99 to the set {11, 22, 33}.
# k={11, 22, 33}
# k.add(99)
# print(k)
# 9. Remove the element 55 from the set {44, 55, 66} using a safe method.
# t={44, 55, 66}
# t.discard(55)
# print(t)    
        