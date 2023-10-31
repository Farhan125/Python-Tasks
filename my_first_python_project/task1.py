from collections import Counter
input_text = input("Enter a text string: ")
cleaned_text = ''.join(char.lower() if char.isalpha() or char.isspace() else ' ' for char in input_text)
words = cleaned_text.split()
word_count = Counter(words)
sorted_word_count = sorted(word_count.items(),key=lambda x: x[1], reverse = True)
print("Word Frequency In Descending Order:")
for words, frequency in sorted_word_count:
    print(f"{words}: {frequency}")


