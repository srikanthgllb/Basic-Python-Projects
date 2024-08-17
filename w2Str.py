def MatchWords(s1,s2):
    c={}
    count=0
    s1=s1.replace("."," ")
    s2=s2.replace(".", " ")
    print(s2)
    for w in s1.split():
        c[w]=c.get(w,0)+1
        print(c)
    for w in s2.split():
        c[w]=c.get(w,0)+1
        print(c)

    for w,v in c.items():
        if v>1:
            count=count+1
    print(count)
    m=max(len(s1.split()),len(s2.split()))
    print(m)
    print("no of simalar words = ",count)
    print("percentage  of simalar words = ", (count/m)*100)

a='Ramu is very good boy'
b='Sonu is very good in cricket.He is tall'
MatchWords(a,b)