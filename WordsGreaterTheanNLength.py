"""
def ExtractWords(str,n):
    b=str.split()
    res = [x for x in b if len(x) >n]
    for i in res:
        print(i)
    return

string="My name iss ramu"
print(ExtractWords(string,3))"""

#write a program to read a string and Nlength and
# filter the first two words that are greater than N
# and merge the words.
## INPUT :'India is my country and its religions'
## 3
## OUTPUT : Icnoduinary
def function(str,n):
    newstr=[]
    temp=[]
    final=[]
    b=str.split()
    print("b= ",b)
    c=[x for x in b if len(x)>n]
    print("len(x)>n = ",c)
    newstr=c[:2]
    print("newstr = ",newstr)
    d=newstr[0][0]
    print("d=",d)
    y,z=0,0
    for i in newstr:
        temp=i[0]
        final.append(temp)
        print(final)
        



str='India is my country and its religions'
n=3
function(str,n)