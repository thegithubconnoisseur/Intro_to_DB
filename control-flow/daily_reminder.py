task_variable = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

word = ''
match priority:

    case _ if priority.lower() == "high":
        word = f" {task_variable} is a high priority task"
          
    case _ if priority.lower() == "medium":
        word = f" {task_variable} is a medium priority task"

    case _ if priority.lower() == "low":
        word = f" {task_variable} is a low priority task"
    
    case _ :
        print("You have to choose from one fo the priorities given in the question.")

    
if time_bound.lower() == "yes":
    print("Reminder:" + word + " that requires immediate attention today!")

elif time_bound.lower() == "no":
    word += ". Consider completing it when you have free time."
    print("Note:" + word)