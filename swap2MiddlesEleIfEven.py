list=[5,10,25,15,50,88]
if len(list)%2 != 0:
    print("PLS enter even num iof elements in list")
else:
    n=len(list)//2
    m=n-1
    m1=list[n]
    m2=list[m]
    m1,m2=m2,m1
print(list)