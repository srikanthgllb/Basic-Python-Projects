#filter even number
#using lambda expression

def isEven(n):
    return (n%2 == 0)

a=[1,2,3,4,6,8,7,9,10,53]
b=list(filter(isEven,a))

c=list(filter(lambda x : x %2 == 0,a))
print(b)
print("Using lambda",c)