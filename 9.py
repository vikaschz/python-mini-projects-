votes = {}

def add_vote_for_candidates(name):
    if name in votes:
        votes[name] += 1
    else:
        votes[name] = 1
    print(f"Vote added for {name}.")

def show_results():
    if not votes:
        print("No votes yet.")
        return
    print("\nResults (sorted by votes):")
    for candidate, count in sorted(votes.items(), key=lambda x: x[1], reverse=True):
        print(f"{candidate}: {count} votes")

def check_winner():
    if not votes:
        print("No votes yet.")
        return
    winner = max(votes.items(), key=lambda x: x[1])
    print(f"\nWinner: {winner[0]} with {winner[1]} votes")

def main():
    while True:
        print('\n1. Add vote for candidate')
        print('2. Show results')
        print('3. Declare winner')
        print('4. Exit')

        choice = input('Enter your choice: ')

        if choice == "1":
            candidate = input("Enter candidate name: ")
            add_vote_for_candidates(candidate)

        elif choice == "2":
            show_results()

        elif choice == "3":
            check_winner()

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print('Invalid input, try again.')

if __name__ == "__main__":
    main()


