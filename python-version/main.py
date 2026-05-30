# Display menu
#Ask for user choice
#Store the choice - variable
#Show the choice

def menu(name):
    print(f"Hello {name}")
    print("\n=== Student Success Tracker ===")
    print("\n1. Add Goal")
    print("\n2. View Goal")
    print("\n3. Exit")

    choice = input("\nEnter your choice: ")

    print(f"\nYou selected option {choice}")


def main():
    name = input("Name: ")
    menu(name)


main()


