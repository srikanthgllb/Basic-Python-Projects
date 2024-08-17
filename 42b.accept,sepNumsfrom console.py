'''write a program which accepts a sequence of comma-separated numbers
from console and find the following 5,23,6,9,4,10
Min ,max,sum,avg,second Max'''



# m="6"
# print(type(m))
# b=int(m)
# print(type(b))
# N=input("Enter comma separated numbers ")
# print(N)
# m=N.split(",")
# print(m)
# print(type(N))
# print(type(m))
# sm=-5656
# mx=0
# sum=0
# for i in m:
#     j=int(i)
#     sum+=j
#     if j >sm:
#         sm=j
#     print(sm)
#     if mx < sm:
#         mx=sm
#     print(mx)
#
# print(type(N))
# print("SUM=",sum)
# print("avg=",sum/len(m))
# print("max=",mx)
# print("max2=",sm)
# print("Min= ",min(m))


print("Enter comma deprated numbers: ")
numstr=input()
lnum=[int(x) for x in numstr.split(",")]
print(lnum)
print("Minimum = %d" % min(lnum))
print("Maximum = ",max(lnum))
print("Sum= ",sum(lnum))
print("Scnd Max= ",sorted(lnum)[-2])
print("Avg= %.2f" % (sum(lnum)/len(lnum)))

