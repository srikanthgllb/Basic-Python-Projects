def findmax(lst,N):
    y=lst[:]
    y.sort(reverse=True)
    return y[:N]

list = [1,2,3,5,7,1.5,10,16]
print(findmax(list,4))

def findminprod(lst,N):
    y=lst[:]
    y.sort()
    print(y)
    new = y[:]
    prod=1
    for i in range(N):
        prod=prod*new[i]
    return prod






list = [1,2,3,5,7,1.5,10,16]
print(findminprod(list,4))
print(findmax(list,4))
