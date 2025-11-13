# Palindrome Checker
# ● Use: Functions, strings, loops
# ● Features:
# ○ Input a string

def is_palindrome(text):
    # Remove spaces and convert to lowercase
    cleaned = text.replace(" ", "").lower()

    # Check if string reads the same forward and backward
    return cleaned == cleaned[::-1]


def main():
    user_input = input("Enter a word or sentence: ")

    if is_palindrome(user_input):
        print("✔ It's a Palindrome!")
    else:
        print("✘ Not a Palindrome.")


if __name__ == "__main__":
    main()


