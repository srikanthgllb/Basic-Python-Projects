#repeatedly read i/p in the following pattern until Null return is presed by the user
# D 1000
# W 500
display :       deposit     withdraw
                   1000
                                 500
                    250
        total      1250          500
        balance    750

l=[]
def GetTransactions():
    print("Enter the Transcations-format=>{D 1000},{W 300}")
    while input is not None:
        i = input("")
        l.append(i)
        if i=="":
            break
    l.remove(l[-1])
    return l


def calcTransaction():
    total,Dtotal,Wtotal=0,0,0

    #m=GetTransactions()
    m=['D 2000', 'W 500', 'D 350']
    print(m)
    for x in  m:
        x=str(x)
        x.split(' ')
        #print(x)
        Mode=x[0]
        print(Mode)
        Amount=int(x[2:])
        print("Amount=",Amount)
        if Mode=='D':
            Dtotal+=Amount
        if Mode =='W':
            Wtotal+=Amount
    print("total=",Dtotal-Wtotal)

calcTransaction()