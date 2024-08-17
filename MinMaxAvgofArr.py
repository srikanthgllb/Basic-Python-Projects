#sum,count,min,max,avg of array
def getarray():
    n=input("Enter the number of elements in array")
    array=[]
    for i in range(n+1):
        arr=int(input("enter the element"))
        array=array.append(arr)
    print(array)

#getarray()

a=[6,7,3,2,90,38,1.5]
print("Sum of Array",sum(a))
print("Count of Array",len(a))
print("Min of Array",min(a))
print("MAx of Array",max(a))
print("Avg of Array",sum(a)/len(a))
