def getList():
    l=[]
    n=int(input("Enter total ele in list"))
    for i in range(n):
        tm=int(input(f"Enter a element {i+1} : "))
        l.append(tm)
    return l

list=getList()
print(list)
n=int(input("Enter a index of element which u want to swap"))
m=int(input("Enter a index of element which u want to swap"))
if len(list) > n >0 and len(list) > m>0:
    list[n], list[m] = list[m], list[n]
print(list)