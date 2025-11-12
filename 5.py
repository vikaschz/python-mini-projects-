# 5. Number Stats
# ● Use: List (numbers), functions, loops
# ● Features:
# ○ Input multiple numbers into a list
# ○ Functions to find max, min, average
# ○ Count how many are even/odd

num_list = []

def number_list(size):
    for i in range(size):
        num = int(input(f"Enter num {i+1}: "))
        num_list.append(num)
    print(num_list)


def maximum_number():
    maximum = max(num_list)
    print(f"The maximum number in list is: {maximum}")


def minimum_number():
    minimum = min(num_list)
    print(f"The manimum number in list is: {minimum}")


def check_average():
    average = sum(num_list) / len(num_list)
    print(f"The average of number list is: {average:.2f}")


def count_even_odd():
    even = 0
    odd = 0
    for num in num_list:
        if num % 2 == 0:
            even += 1
        else:
            num % 2 != 0
            odd += 1
        
    print(f"Total even numbers: {even}")
    print(f"Total odd numbers: {odd}")


while True:
    print("===========================")
    print("\n1. add numbers to list")
    print("2. check maximum")
    print("3. check minimum")
    print("4. check average")
    print("5. count even/odd numbers")
    print("6. Exit")
    print("===========================")

    choice = input("Enter your choice: ")

    if choice == "1":
        number_list_size = int(input("Enter the size of number list: "))
        number_list(number_list_size)

    elif choice == "2":
        maximum_number()

    elif choice == "3":
        minimum_number()
    elif choice == "4":
        check_average()

    elif choice == "5":
        count_even_odd()

    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid input, try again.")
