#153 = 1^3 + 5^3 + 3^3 = 1+125+27 = 153
# 153 -> 3 digits
#1634 = 1^4 +6^4 +3^4 +4^4 = 1634

#write function to find no of digits
def getDigitCount(n):
    l=0
    t=n
    while(t>0):
        l += 1
        t = t//10
    return l

def getAmstrong(n):
    l=getDigitCount(n)
    s=0
    t=n
    while(t>0):
        s= s + pow(t % 10,l)
        print(s)
        t = t //10
        print("t=",t)
    return s

n=int(input("Enter a num :"))
if (n == getAmstrong(n)):
    print(n," is a Amstrong number ")
else:
    print(n,"is not an Amstrong number")





