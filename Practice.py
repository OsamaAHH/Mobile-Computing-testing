'''sump=int(0)

P=int(input("Enter positive number"))
while(P<=0):
  print("Only positive number alowed.")
  P=int(input("Enter positive number"))


for i in range (0,P):
  P=int(input("Enter positive number"))
  sump=sump+P
  
print(sump)


x=[25,15,22,17,10,12]
y=[12,15,22,14,10,10]
sumxy=0
c=0
avg=0

for i in range(0,6):
  if(x[i]==y[i]):
    sumxy=sumxy+x[i]
    c=c+1
  

print(sumxy)
avg=sumxy/3
print(avg)



y=[29,3,4,-7,19]
x=[3,20,17,7,-3]
sumy=0
sumx=0

sumy=sum(y)
sumx=sum(x)

print(sumy)
print(sumx)

if(sumy>sumx):
  for i in range(0,4):
    if y[i]<0:
      print(y[i])
    else:
        for i in range(0,4):
          if x[i]<0:
            print(x[i])  



Even=[]
Odd=[]
e=0
o=-1
for i in range(0,50):
  e=e+2
  Even.append(e)
  


for i in range(0,50):
  o=o+2
  Odd.append(o)


print(Even)
print(Odd)



A=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
B=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]

c=input("Enter the alphabet: ")

D=[]
x=len(c)

y=str()

for i in range(x):
  D.append(c[i])
  for j in range (0,len(A)):
      if(D[i]==A[j]):
        print(B[j])
        y=y+B[j]

print(y)

n=str(input("Enter Name: "))
y=len(n)
Name=[]

for i in range(y):
  Name.append(n[i])

print(Name)
x=len(Name)

Vowels=["a","e","i","o","u"]
c=0
avg=0
avg1=0

for j in range(y):
  if(Name[j]=="a" or Name[j]=="e" or Name[j]=="i" or Name[j]=="o" or Name[j]=="u"):
       c=c+1


print(c)

avg1=len(n)
avg=c/avg1*100
print(avg)



myList=[70,46,43,27,57,41,45,21,14]

listl=len(myList)

for i in range(0,listl):
  for j in range(listl-1):
    if(myList[j]>myList[j+1]):
      temp=myList[j]
      myList[j]=myList[j+1]
      myList[j+1]=temp

print(myList)


pos = -1

def search(list, n):

  u=len(list)-1
  l=0

  while l<=u:

    m = (l+u) // 2

    if list[m] == n:

      globals()['pos']=m
      return True

    else:
      if list[m] < n:
        l = m + 1;

      else:
        u = list[m] -1;

  return False

list=[1,2,3,4,5,6,7,8,9]
n=int(input("Enter number: "))

if search(list,n):
  print("Found in ",pos+1)
else:
  print("Not found")




Stack=[]
TP=len(Stack)
BP=0

stackfull=10

''''''
while(TP < stackfull):
  num=int(input("Enter number: "))
  Stack.append(num)
  TP=TP+1

  print(Stack)
  
print("Stack is full, cannot push")


''''''
if (TP == BP):
  print("Stack is empty, cannot pop")

else:
  print(Stack[-1])
  TP = TP - 1



Q=[]

def enQ():
  element=input("Enter the number you want to add: ")
  Q.append(element)
  print(element," is added to the queue")

def deQ():
  if not Q:
    print("Queue is empty")
  else:
    e = Q.pop(0)
    print("Removed element: ",e)

def display():
  print(Q)

while True:
  print("Select the operation \n 1. Add \n 2. Remove \n 3. Display \n 4. Quit")
  choice = int(input())
  if choice == 1:
    enQ()
  elif choice == 2:
    deQ()
  elif choice == 3:
    display()
  elif choice == 4:
    break
  else:
    print("Enter the correct operation")



myList=[1,8,7,4,8,9,6,2,4]
newList=[]
UB=8
LB=0

key = 0

place = 0

for index in range (1,8):
  key = myList[index]
  place = index - 1

  if (myList[place] > key):
    while(place >= LB and myList[place] > key):
      temp = myList[place + 1]
      newList.append(temp)
      place = place -1
    myList[place + 1] = key
  

print(newList)
  
'''

f=open("alevel.txt","w")
f.write("This is a text")
f.close()









