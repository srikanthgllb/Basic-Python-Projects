'''alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']


numerology_numbers = [1, 2, 3, 4, 5, 8, 3, 5, 1, 1,
                      2, 3, 4, 5, 7, 8, 1, 2, 3, 4,
                      6, 6, 6, 5, 1, 7]

z=zip(numerology_numbers,alphabets)
print(list(z))
name="srikanth"
Nam=name.split()
print(list(name))
#res=[x for _,x in sum(int(z))]
#print(res)

res=[x for _,name in sum(z) ]'''

# Define the numerology numbers for each alphabet
numerology_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8]

# Function to calculate the numerology of a name
"""def calculate_numerology(name):
 
    name = name.lower()# Convert the name to lowercase
    total_value = 0 # Initialize the total numerology value
    
    for char in name:# Iterate over each character in the name
        if char.isalpha():  # Check if the character is an alphabet
            index = ord(char) - ord('a')# Calculate the index (0 for 'a', 1 for 'b', etc.)
            total_value += numerology_numbers[index]# Add the corresponding numerology number to the total value
    
    # Reduce the total value to a single digit
    while total_value > 9:
        total_value = sum(int(digit) for digit in str(total_value))
    return total_value

name = input("Enter a name: ")# Accept a name from the user


numerology_value = calculate_numerology(name)# Calculate and print the numerology value
print(f"The numerology value of the name '{name}' is: {numerology_value}")
"""


def Num_Cal(name):
    name = name.lower()
    total = 0
    for char in name:
        if char.isalpha():
            index = ord(char) - ord('a')
            total += numerology_numbers[index]
    while total > 9:
        total = sum(int(digit) for digit in str(total))
    return total


name = input("Enter your name")
num = Num_Cal(name)
print(f"The Numerology value of ur name '{name}' is '{num}'")
