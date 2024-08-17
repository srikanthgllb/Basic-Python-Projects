#My technique

def createDelimiter(str):
    z=[]
    a=str.split()
    print(a)
    b=a[::-1]
    print(b)
    for i in b:
        z.append(i)

        z.append("*")
    print(z)
    y=" ".join(z)
    print(y)


str="sri is my name "
#print(createDelimiter(str))

#Another technique
def SplitStarJoin(str):
    b=list(reversed(str.split(" ")))
    return "*".join(b)

str="sri is my name "
#print(SplitStarJoin(str))


#INPUT sri is my name
#OUTPUT name * my ** is *** sri
def SplitJoinMultipleStar(str):
    z=[]
    a=str.split()
    print(a)
    b=a[::-1]
    print(b)
    x = 0
    for i in b:
        z.append("*" * x)
        z.append(i)
        x+=1

    print(z)
    y=" ".join(z)
    print(y)


str="sri is my name "
print(SplitJoinMultipleStar(str))
