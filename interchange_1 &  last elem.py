#Input=[1,2,3,4,5]
#Output=[5,2,3,4,1]

'''def getList():
    l=[]
    n=int(input("Enter total ele in list"))
    for i in range(n):
        tm=int(input("Enter a element"))
        l.append(tm)
    return l

list=getList()
print(list)
list[0],list[-1] = list[-1],list[0]
print("updated list",list)'''

myList=[88,8,4,6,98,3,5,77]
fele=myList[0]
lele=myList[len(myList)-1]

for i in myList:
     if myList[0]:
          myList[0]=lele
     if myList[len(myList)-1]:
          myList[len(myList)-1]=fele

print(fele)
print(lele)
print(myList)

#approach 1 using temp variable
myList=[88,8,4,6,98,3,5,77]
size=len(myList)

temp=myList[0]
myList[0]=myList[size-1]
myList[size-1]=temp

print("list after swap",myList)
print("--------------------------------------")

#approach 2 single line
print("list before swap",myList)
myList[0],myList[-1]=myList[-1],myList[0];
print("list after swap",myList)
print("--------------------------------------")

#approach 3 using tuple

myList=[88,8,4,6,98,3,5,77]
print("list before swap",myList)
get=(myList[-1],myList[0])
myList[0],myList[-1]=get

print("list after swap",myList)
print("--------------------------------------")

# approach 4 using * operand

myList=[88,8,4,6,98,3,5,77]
print("list before swap",myList)
start,*middle,end=myList
print(start)
print(middle)
print(end)
myList=[end,*middle,start]
print("list after swap",myList)
print("--------------------------------------")

#approach 5 using pop()

myList=[88,8,4,6,98,3,5,77]
first=myList.pop(0)
last=myList.pop(-1)
print("list after swap",myList)

myList.insert(0,last)
myList.append(first)
print("list after swap",myList)


