A=[1,4,5,3,6,8,2,10,34,23,1,5,56]
mx = 0
mx2=0
for i in range(len(A)):
    if A[i] > mx:
        mx2 = mx  # Update mx2 before updating mx
        mx = A[i]
    elif A[i] > mx2 and A[i] != mx:
        mx2 = A[i]
print("max of A",(mx))
print("Second max of A",(mx2))