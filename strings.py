#charecter counting
def count_char(string):
    for char in sorted(set(string)): 
        print(f"{repr(char)}={string.count(char)}",end=" ,")
string=input("enter the string:")
count_char(string) 
print()
#removing vowels
def remove_vowl(string):
    vowels="aeiouAEIOU"
    result=""
    for char in string:
        if char not in vowels:
            result+=char
    return result
string=input("enter the string:")  
print(remove_vowl(string))
print()
#counting vowels
def count_vowl(string):
    vowels="aeiouAEIOU"
    count=0
    for char in string:
        if char in vowels:
            count+=1
    return count
string=input("enter the string:")  
print(count_vowl(string))



                     
