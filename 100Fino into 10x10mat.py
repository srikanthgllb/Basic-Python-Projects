'''def Fino(n):
    a=0
    b=1
    for i in range(1,n+1):
        sum = a + b
        a=b
        b=sum
        return sum
        if i%10 == 0:
            print("/n")
        else:
            continue
'''
fibonacci_numbers = [0, 1]

# Step 2: Generate the remaining Fibonacci numbers up to 100
while len(fibonacci_numbers) < 100:
    next_fib = fibonacci_numbers[-1] + fibonacci_numbers[-2]
    fibonacci_numbers.append(next_fib)

# Step 3: Print the numbers in a 10x10 grid
for i in range(0, 100, 10):
    row = fibonacci_numbers[i:i + 10]
    print(" ".join(str(num) for num in row))