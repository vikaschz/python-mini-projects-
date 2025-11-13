# 9. Number Guessing Game with History
# ● Use: List (store guesses), functions, loops
# ● Features:
# ○ User guesses a random number
# ○ Keep track of all guesses
# ○ Show guess history at the end

import random

# computer chooses one number
s = random.randint(1, 50)

guesses = []

def main():
    count = 0
    while True:
        user = int(input("Guess a number between 1 and 50: "))
        guesses.append(user)  # store guesses
        count += 1

        if user == s:
            print(f"✅ Correct! You guessed it in {count} tries.")
            print("Your guesses were:", guesses)
            break
        elif len(guesses) >= 10:
            print("❌ Guess limit completed! The number was", s)
            print("Your guesses were:", guesses)
            break
        elif user < s:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == "__main__":
    main()



