# 4. Unique Words Counter
# ● Use: Set (unique words), functions, loops, strings
# ● Features:
# ○ Input a paragraph or sentence
# ○ Split words and count unique ones using set
# ○ Display unique words and count

import string
def unique_words_counter(text):
    text = text.translate(str.maketrans('', '', string.punctuation))

    text = text.lower()
    words = text.split()

    unique_words = set(words)
    for unique_word in unique_words:
        print(unique_word)
    total = len(unique_words)
    print(f"Total unique words: {total}")
paragraph = input("Enter a paragraph or sentence: ")
unique_words_counter(paragraph)


