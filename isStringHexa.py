a='a'
print("a-",ord(a))
a='z'
print("z-",ord(a))
a='A'
print("A-",ord(a))
a='Z'
print("Z-",ord(a))
str="1234567S890AbcDe"
b=set(str)
print(b)

for i in b:
    if (i.isdigit() or
            (ord(i)>64 and ord(i)<71) or
            (ord(i)>96 and ord(i)<103)):
        continue
    else:
        print("the string is not hexa")
        break
else:
    print("the string is hexa")

