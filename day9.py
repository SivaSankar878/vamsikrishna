# 1.Find the frequency of each character in a string.
# n=input()
# for i in n:
#     fre=0 
#     for j in n:
#         if i==j:
#             fre+=1
#         else:
#             fre==1
#     print(i,'=',fre)                      
# 2.Remove all duplicate characters from a string.
# n=input()
# t=''
# for i in range (len(n)):
#     if n[i] not in t:
#         t+=n[i]
# print(t)         
# s="programming"
# r=""
# for i in range(len(s)):
#     if s[i] not in r: r+=s[i]
# print(r)


# 3.Find the longest word in a sentence.
# 4.Count how many times each word appears in a string.
# 5.Replace all spaces in a string with -.
# n=input()
# j=n.replace(" ","-")
# print(j)

# 6.check anagram or not
a='siva'
b='visa'
if len(a)==len(b):
    cou=0
    res=list(b)
    for i in a:
        if i in b:
            res.remove(i)
            cou+=1
    if cou==len(a):
        print('anagram')
    else:
        print('not anagram')                            
else:
    print('length is not matched not a angram')        
