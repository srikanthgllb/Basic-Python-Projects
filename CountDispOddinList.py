l = [43, 53, 56, 52, 46, 35, 867, 356, 3, 6]
b = list(filter(lambda x: x % 2 != 0, l))
print("l= ", l)
print("Odd numbers in l :", b)
count=0
for i in range(len(b)):
    count=count+1
print("Number of Odds in b : ",count)
