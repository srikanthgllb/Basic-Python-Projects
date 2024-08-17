#input (0-9) eg:2
#uotput 2+222+22222+2222222=2468

N=input("Enter a single digit number")
#Youtube

d1=N
d3=N * 3
d5=N * 5
d7=N * 7

res=int(d1)+int(d3)+int(d5)+int(d7)
print("{0} + {1} + {2} + {3} = {4} ".format(d1,d3,d5,d7,res))

#Mine
z=int(input("Enter no of combinations : "))
def isSinleDigit(num):
    if int(num)>=0 and int(num)<10:
        return True

if isSinleDigit(N) is True:
    l = []
    n = 1
    p = []
    r = 0
    for x in range(z):
        l.append(N * n)
        n+=2
        q = int(l[r])
        p.append(q)
        r += 1
    #print(l) # print(p)
    print(','.join(str(x) for x in l))
    print("Sum of integers=",sum(p))
else:
    print("Invalid Input")
    exit()
