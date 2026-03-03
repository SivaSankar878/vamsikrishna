for row in range(1,6):
    for col in range(1,6):
        if row==1 or row ==3 or col==1 or col==5:
            print("A",end=" ")
        else:
            print(" ",end=" ")
    print()
print()   

for row in range(1,6):
    for col in range(1,6):
        if row==1 or row==5 or col==1 or col==4 and row in [1,2,4,5] or row ==3 and col in [2,3]:
            print("B",end=" ")
        else:
            print(" ",end=" ")
    print()
print() 

for row in range(1,6):
    for col in range(1,6):
        if row==1 or row==5 or col==1:
            print("C",end=" ")
        else:
            print(" ",end=" ")
    print()
print() 

for row in range(1,6):
    for col in range(1,6):
        if col==1 or row==1 and col in [2,3] or row ==5 and col in[2,3] or row==2 and col==4 or row==3 and col==4 or row==4 and col==4 : 
             print("D",end=" ")
        else:
            print(" ",end=" ")
    print()
print() 

for row in range(1,6):
    for col in range(1,6):
        if row==1 or row==3 or row==5 or col==1: 
             print("E",end=" ")
        else:
            print(" ",end=" ")
    print()
print()

for row in range(1,6):
    for col in range(1,6):
        if row==1 or row==3  or col==1: 
             print("F",end=" ")
        else:
            print(" ",end=" ")
    print()
print()

for row in range(1,6):
    for col in range(1,6):
        if row==1 or col==1 or row==3 and col in [3,4,5] or row==4 and col in[3,5] or row==5 and col in [2,3,5]: 
             print("G",end=" ")
        else:
            print(" ",end=" ")
    print()
print()

for row in range(1,6):
    for col in range(1,6):
        if row==3 or col==5 or col==1: 
             print("H",end=" ")
        else:
            print(" ",end=" ")
    print()
print()

for row in range(1,6):
    for col in range(1,6):
        if row==1 or row==5 or col==3: 
             print("I",end=" ")
        else:
            print(" ",end=" ")
    print()
print()

for row in range(1,6):
    for col in range(1,6):
        if row==1 or col==3 or row==5 and col in[1,2] or row==4 and col==1: 
             print("J",end=" ")
        else:
            print(" ",end=" ")
    print()
print()

for row in range(1,6):
    for col in range(1,6):
        if col==1 or row==3 and col==2 or row==1 and col==4 or row==2 and col==3 or row==4 and col==3 or row==5 and col==4: 
             print("K",end=" ")
        else:
            print(" ",end=" ")
    print()
print()

for row in range(1,6):
    for col in range(1,6):
        if  row==5 or col==1: 
             print("L",end=" ")
        else:
            print(" ",end=" ")
    print()
print()        

for row in range(1,6):
    for col in range(1,6):
        if  col==5 or col==1 or row==2 and col in[2,4] or row==3 and col==3: 
             print("M",end=" ")
        else:
            print(" ",end=" ")
    print()
print()  

for row in range(1,6):
    for col in range(1,6):
        if  col==5 or col==1 or row==2 and col==2 or row==3 and col==3 or row==4 and col==4: 
             print("N",end=" ")
        else:
            print(" ",end=" ")
    print()
print()

for row in range(1,6):
    for col in range(1,6):
        if  row==5 and col in[2,3,4] or row==1 and col in [2,3,4] or col==1 and row in [2,3,4] or col==5 and row in [2,3,4]: 
             print("O",end=" ")
        else:
            print(" ",end=" ")
    print()
print()

for row in range(1,6):
    for col in range(1,6):
        if  row==1 or row==3 or col==1 or col==5 and row==2: 
             print("P",end=" ")
        else:
            print(" ",end=" ")
    print()
print()

for row in range(1,6):
    for col in range(1,6):
        if  row==4 and col in [2,3,4] or col==1 and row in [1,2,3,4] or row==1 and col in [2,3,4] or col ==4 and row in[2,3,4] or row==5 and col==5: 
             print("Q",end=" ")
        else:
            print(" ",end=" ")
    print()
print()

for row in range(1,6):
    for col in range(1,5):
        if  row==1 or col==1 or row ==2 and col ==3 or row ==3 and col ==2 or row ==4 and col ==3 or row ==5 and col ==4: 
             print("R",end=" ")
        else:
            print(" ",end=" ")
    print()
print() 

for row in range(1,6):
    for col in range(1,6):
        if  row==5 or row==1 or row==3 or col ==1 and row==2 or col==5 and row==4: 
             print("S",end=" ")
        else:
            print(" ",end=" ")
    print()
print()

for row in range(1,6):
    for col in range(1,6):
        if  row==1 or col==3: 
             print("T",end=" ")
        else:
            print(" ",end=" ")
    print()
print()

for row in range(1,6):
    for col in range(1,6):
        if  row==5 and col in [2,3,4] or col==1 and row in [1,2,3,4] or col==5 and row in [1,2,3,4]: 
             print("U",end=" ")
        else:
            print(" ",end=" ")
    print()
print()

for row in range(1,6):
    for col in range(1,6):
        if  row==1 and col in [1,5] or row==2 and col in [1,5] or row==3 and col in [1,5] or row==4 and col in [2,4] or row==5 and col==3: 
             print("V",end=" ")
        else:
            print(" ",end=" ")
    print()
print()

for row in range(1,6):
    for col in range(1,6):
        if  col==5 or col==1 or row==3 and col==3 or row==4 and col in [2,4]: 
             print("W",end=" ")
        else:
            print(" ",end=" ")
    print()
print()

for row in range(1,6):
    for col in range(1,6):
        if  row==col or row+col==6: 
             print("X",end=" ")
        else:
            print(" ",end=" ")
    print()
print()

for row in range(1,6):
    for col in range(1,6):
        if  row==1 and col in [1,5] or row ==2 and col in [2,4] or col==3 and row in [3,4,5]: 
             print("Y",end=" ")
        else:
            print(" ",end=" ")
    print()
print()

for row in range(1,6):
    for col in range(1,6):
        if  row==1 or row==5 or row==2 and col==4 or row==3 and col==3 or row==4 and col==2: 
             print("Z",end=" ")
        else:
            print(" ",end=" ")
    print()
print()
         

