'''myList=[0,1,2,3,4,5,6,7,8,9]
UB=9
LB=0

index=0
item=0

found=False
index=LB

item=int(input("Please enter item to be found: "))
while(found==False or index==UB):
    
    for i in range(0,10):
        if(item==myList[i]):
            found=True
        else:
            index=index+1     
print(found)'''

myList=[0,1,2,3,4,5,6,7,8,9]
UB=9
LB=0

counter=0
item=0

found=False

item=int(input("Input number"))
while(found==False or counter==UB):
    for i in range(LB,UB):
        if(item==myList[i]):
            found=True
        else:
            counter=+1
    print(found)
    found=False
    item=int(input("Input number"))

        

