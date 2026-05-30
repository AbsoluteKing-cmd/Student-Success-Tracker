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

    if choice == "1":
        add_goal()


def main():
    name = input("Name: ")
    menu(name)
    print(goals)

goals = [] #This will store all the goals and their respective information.

def add_goal(): #This function will add a goal to the goal list.
    goal = {}
    goal["Name"] = input("What is your goal?: ")
    goal["Deadline"] = input("When would you like to finish it?: ")
    goal["Status"] = "Started"
    goals.append(goal)
    print("\nGoal added successfully!")

    

main()


