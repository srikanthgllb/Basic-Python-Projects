import math
def sumofNN(n):
    sum = 0
    for i in range(n):
        sum =sum +i
        print(sum,i)
    return sum

#to find sum of suqures of first n number
def sumofNsq(n):
    sum = 0
    for i in range(1,n+1):
        #sum =sum + math.pow(i,2)
        sum = sum +i*i
        print(i,"^2 is",math.pow(i,2))
    return sum


n=int(input("Enter a number"))
print("Sum of squres of first",n,"Numbers is",sumofNsq(n))
#print(sumofNsq(4))

