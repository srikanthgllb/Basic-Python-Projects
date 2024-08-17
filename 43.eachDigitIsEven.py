# Write a program ,which will find all such numbers
# between 1000 and 3000(both included) such that
# each digit of the numbers ia an even number.
#Input - 1002 - 1 is odd
#Input - 2002 -even

j = 5234
print("j = ",j)
d1 = j // 1000  # First digit (thousands place)
print("j // 1000 =",d1)
d1 = j % 1000  # First digit (thousands place)
print("j % 1000 =",d1)
d2 = (j // 100)  # Second digit (hundreds place)
print("j // 100 =",d2)
d3 = (j // 10)   # Third digit (tens place)
print("j // 10 =",d3)
d4 = j % 10     # Fourth digit (units place)
print("j %10 =",d4)

#Youtube
def IsAllEvenDigits(n):
    IsEvenDigits=True
    while n>0:
        t=n%10
        if t % 2 !=0:
            IsEvenDigits=False
            break
        n=int(n / 10)
    return IsEvenDigits

l=[str(x) for x in range(1000,3001) if IsAllEvenDigits(x)]
print(l)
print(','.join(l))


#ChatGPT
def isEven(x):
    # Check if the digit is even
    return x % 2 == 0


# Loop through the range 1000 to 3000 (inclusive)
for i in range(1000, 3001):
    # Extract each digit of the number
    d1 = i // 1000  # First digit (thousands place)
    d2 = (i // 100)  # Second digit (hundreds place)
    d3 = (i // 10)   # Third digit (tens place)
    d4 = i % 10  # Fourth digit (units place)

    # Check if all digits are even
    # if isEven(d1) and isEven(d2) and isEven(d3) and isEven(d4):
    #     print(i)


#My method
def isEvnDigit(num):
    for digit in str(num):
        if int(digit) % 2 != 0:
            return False
    return True


evenDigits = []

for i in range(1000, 3001):
    if isEvnDigit(i):
        evenDigits.append(i)

#print(evenDigits)
