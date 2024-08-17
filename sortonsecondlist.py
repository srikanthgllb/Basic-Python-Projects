def SortOnSecondList(list1,list2):

    z=zip(list2,list1)
    res=[x for _,x in sorted(z)]
    return res

a=['a','b','c','d','e','f','g','h','i']
b=[1,4,3,1,2,3,4,2,1]
print(SortOnSecondList(a,b))


#to find ascii value
char="D"
print(ord(char))

