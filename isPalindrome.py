str=input("Enter a word to chcek palindrome")

b=''.join(reversed(str))
if b==str:
    print(str + " is palindrome")
else:
    print(b," is not palindrome")


# if str == str[::-1]:
#     print(str+" is palindrome")
# else:
#     print(str," is not palindrome")