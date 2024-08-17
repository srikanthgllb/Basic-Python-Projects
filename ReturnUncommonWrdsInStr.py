# Input  'Ramu is my friend'
#         'Somu is my boy'
#
# Output ['Ramu','Somu','friend','boy']
# a={}
# a["Ramu"]=1
# print(a)  #--> {'Ramu:1'}
# b=a.get("Ramu")
# print(b)
# a.get("Somu") #print nothing
# b=a.get("Somu",15) #--> if somu has value return somu
#                    # else return 15
# a.get("Ramu",2)# -->print ramu's value if present
#                 #else return 2.
#                 # -->already Ramu has value 1
#                 # it print 1
# print(b)


def FindUnCommon(s1,s2):
    # create dictionary
    c={}
    print(c)
    #built dict using s1
    for w in s1.split():
        c[w]=c.get(w,0)+1
        print(c)
    # built dict using s2
    for w in s2.split():
        c[w] = c.get(w, 0) + 1
        print(c)

    #print results(w=word in dict ,v=its value(count))
    for w,v in c.items():
        if v==1:
            print(w)
    return

a='Ramu is my friend my'
b='Somu is my boy'
FindUnCommon(a,b)