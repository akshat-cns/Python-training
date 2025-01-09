def display_menu():
    print("\nVoting System")
    print("1. Cast a vote")
    print("2. View results")
    print("3. Exit")


def cast_vote(voters, votes):
    voter_id = input("Enter your voter ID: ")

    if voter_id in voters:
        print("You have already voted.")
        return

    print("\nCandidates:")
    for candidate in votes:
        print(f"- {candidate}")

    choice = input("Enter the name of the candidate you want to vote for: ").strip()
    if choice in votes:
        votes[choice] += 1
        voters.add(voter_id)
        print(f"Your vote for {choice} has been recorded!")
    else:
        print("Invalid candidate! Vote not recorded.")


def view_results(votes):
    for candidate, vote_count in votes.items():
        print(f"{candidate}: {vote_count} votes")


def main():
    voters = set()  
    votes = {"Akshat": 0, "Dev": 0, "Daksh": 0}  

    while True:
        print(''' \nVoting system:
    1. Caste a vote
    2. View results
    3. Exit ''')
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                cast_vote(voters, votes)
            elif choice == 2:
                view_results(votes)
            elif choice == 3:
                print("Exit.")
                break
            else:
                print("Invalid choice! Please select a valid option.")
        except ValueError:
            print("Please enter a number!")

if __name__ == "__main__":
    main()