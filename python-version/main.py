# Display menu
#Ask for user choice
#Store the choice - variable
#Show the choice

def menu(name):
    print(f"Hello {name}")
    print("\n=== Student Success Tracker ===")
    print("\n1. Add Goal")
    print("\n2. View Goals")
    print("\n3. Update Goal Status")
    print("\n4. Delete Goal")
    print("\n5. Exit")

def get_integer(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Please enter a valid number.")

def main():
    name = input("Name: ")
    while True:
        menu(name)
        choice = get_integer("Enter your choice: ")
        if choice == 1:
            add_goal()
        elif choice == 2:
            view_goals()
        elif choice == 3:
            update_goal_status()
        elif choice == 4:
            delete_goal()
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

goals = [] #This will store all the goals and their respective information.

def add_goal(): #This function will add a goal to the goal list.
    goal = {}
    goal["Name"] = input("What is your goal?: ")
    goal["Deadline"] = input("When would you like to finish it?: ")
    goal["Status"] = "Started"
    goals.append(goal)
    print("\nGoal added successfully!")

#We are going to add a view goals function. This function should help with 
# viewing the goals that have been added to the goal list. It should display the name, 
# deadline, and status of each goal.    

def view_goals():
    if len(goals) == 0:
        print("No goals added yet.")
    else:
        for num in range(len(goals)):
            print(f"Goal {num + 1}:")
            print(f"\tName: {goals[num]['Name']}")
            print(f"\tDeadline: {goals[num]['Deadline']}")
            print(f"\tStatus: {goals[num]['Status']}")
            print("\n")

#This function will allow the user to update the status of a goal. 
# The user will be able to choose which goal they want to update and then 
# select the new status for that goal. The status options will be 
# "Started", "In Progress", and "Completed". After the user selects the new status, 
# the goal's status will be updated in the goal list.

def display_goals():
    for num in range(len(goals)):
            print(f"\n{num + 1}. {goals[num]['Name']}")

def update_goal_status():
    if len(goals) == 0:
        print("No goals added yet.")
    else:
        display_goals()
        choice = get_integer("\nWhich goal would you like to update?: ")
        while choice < 1 or choice > len(goals):
            print("Invalid choice. Please try again.")
            choice = get_integer("\nWhich goal would you like to update?: ")
        print("\nChoose new status")
        print("\n1. Started")
        print("2. In Progress")
        print("3. Completed")
        status_choice = get_integer("\nEnter your choice: ")
        while status_choice not in [1, 2, 3]:
            print("Invalid choice. Please try again.")
            status_choice = get_integer("\nEnter your choice: ")
        status = ["Started", "In Progress", "Completed"]
        new_status = status[status_choice - 1]
        goals[choice - 1]["Status"] = new_status
        print("\nGoal status updated successfully!")


"""This function will allow the user to delete a goal from the goal list.
    If there are no goals:
        Display message
    Otherwise:
        Display numbered goals
        Ask which goal to delete
Validate choice
Remove goal using pop()
Display confirmation 
"""

def delete_goal():
    if len(goals) == 0:
        print("No goals added yet.")
    else:
        display_goals()
        choice = get_integer("\nWhich goal would you like to delete?: ")
        while choice < 1 or choice > len(goals):
            print("Invalid choice. Please try again.")
            choice = get_integer("\nWhich goal would you like to delete?: ")
        deleted_goal = goals.pop(choice - 1)
        print(f"Deleted goal: {deleted_goal['Name']}")
        
main()

