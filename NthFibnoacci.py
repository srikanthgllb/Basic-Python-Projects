#fact 0, 1, 1, 2,3,5,8,13,21.
#    f0,f1,f2,f3, ....

''' #looping method
def NthFibo(n):
    a = 0
    b = 1
    if n == 0:
        return a
    elif n ==1:
        return b
    else:
        for i in range(2,n+1):
            sum=a+b
            a=b
            b=sum
            #print(i,sum)
        return sum
        '''

# RECURSIVE method
def NthFiboRecursive(n):
    if n ==0:
        return 0
    elif n==1:
        return 1
    else:
        return NthFiboRecursive(n-1) + NthFiboRecursive(n-2)

print("Nth Fibonacci finding: ")
print("=================================")
n=int(input("Enter a num for fibonaci :  "))
print(n,"th Fibonacci term is",NthFiboRecursive(n))


