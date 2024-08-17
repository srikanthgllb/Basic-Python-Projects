#to prnt values between 2000 ana 3200
# that are divided by 7 and not multiple  by 5

# def ranger():
#     li=[]
#     for i in range(2000,3201):
#         if (i %7==0)and (i%5!=0):
#             #print (i)
#             li.append(str(i))
#     return li
# print(','.join(ranger()))

l=[str(x) for x in range(2000,3201) if (x %7==0)and (x %5!=0)]
print(','.join(l))

