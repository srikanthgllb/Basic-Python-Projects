
'''def GetUniqWords(str):
    lst = str.split()
    res = []
    for i in lst:
        if i not in res:
            res.append(i)
    return res

a = "ram is my friend and he is living in london"
print(GetUniqWords(a))'''

#We’ll take a string as input, find the unique words, and count their occurrences.
def count_unique_words(input_string):
    words = input_string.split()
    word_counts = {}

    for word in words:
        word = word.strip(".,!?")
        word = word.lower()

        # Update the word count in the dictionary
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Print the unique words and their counts
    for word, count in word_counts.items():
        print(f"{word}: {count}")

# Example usage
input_string = "This is a test. This is only a test. Testing, testing!"
count_unique_words(input_string)
