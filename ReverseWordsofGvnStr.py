
def RevwrdinStr(str1):
    li = str1.split(" ")
    new = []
    for word in li:
        word = str(word)

        word1=word.split()
        print(word1)
        word1[0], word1[-1] = word1[-1], word1[0]
        new.append(word)
    print(new)
    newli = li[::-1]
    newli2 = ''.join(newli)
    return newli2

str1 = "my name is ram, i am from arcot"
print(RevwrdinStr(str1))


'''def encrypt_string(input_string):
    words = input_string.split()
    encrypted_words = []

    for word in words:
        reversed_word = word[::-1]
        if len(reversed_word) > 1:
            encrypted_word = reversed_word[-1] + reversed_word[1:-1] + reversed_word[0]
        else:
            encrypted_word = reversed_word
        encrypted_words.append(encrypted_word)

    encrypted_string = ' '.join(encrypted_words)
    return encrypted_string

input_string = input("Enter a string: ")
print("Encrypted string: ", encrypt_string(input_string))
'''


'''def encrypt_string(input_string):
    # Split the input string into words
    words = input_string.split()
    print("words ",words)

    # Function to reverse a word and interchange the first and last character
    def encrypt_word(word):
        if len(word) > 1:
            # Reverse the word
            reversed_word = word
            print("reversed_word ",reversed_word)
            # Interchange the first and last character
            encrypted_word = reversed_word[-1] + reversed_word[1:-1] + reversed_word[0]
            print("encrypted_word ",encrypted_word)
        else:
            # If the word has only one character, no change is needed
            encrypted_word = word
        return encrypted_word

    # Encrypt each word in the list
    encrypted_words = [encrypt_word(word) for word in words]
    print("encrypted_words",encrypted_words)

    # Join the encrypted words back into a single string
    encrypted_string = ' '.join(encrypted_words)
    print("encrypted_string",encrypted_string)
    print(encrypted_string[0])
    #print(new_string)
    #return new_string


# Read a string from the user
input_string = input("Enter a string: ")

# Encrypt the string
encrypted_string = encrypt_string(input_string)

# Print the encrypted string
print("Encrypted string:", encrypted_string)
'''