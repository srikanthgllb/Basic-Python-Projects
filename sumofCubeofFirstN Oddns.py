def sumofcube(n):
    sum=0
    for i in range(1, n, 2):
        sum =sum + pow(i,3)
        print ("cube of ",i,"is",pow(i,3),"Total = ",sum)


print(sumofcube(10))