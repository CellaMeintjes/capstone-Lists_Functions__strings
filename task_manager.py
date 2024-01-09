# =====importing libraries===========
import datetime


# ====LOGIN SECTION====

# Read data from users.txt append to dict and validate username and password
def read_users():
    users = {}
    with open("users.txt", "r") as file:
        for line in file:
            username, password = line.strip().split(", ")
            users[username] = password
    return users


# Validate user credentials for login section
def validate_credentials(users):
    while True:
        username = input("Enter your username:\n")
        password = input("Enter your password: \n")

        # Check if username and password in users
        if username in users and users[username] == password:
            return username
        else:
            print("Invalid username or password. Please try again.")


# Function to allow admin special menu
def is_admin(username):
    return username == 'admin'


# Register new user and write to users.txt
def reg_user():
    users = read_users()

    while True:
        new_username = input("Enter a new username: \n")
        # Check if username is already registered in users.txt
        if new_username in users:
            print("Username already exists. Please choose a different username.")
            return

        new_password = input(f"Enter a password for {new_username}:\n")
        confirm_password = input("Confirm password:\n")

        # Validate new-password
        if new_password == confirm_password:
            users[new_username] = new_password

            # Open users.txt and write new details of user to the file
            with open("users.txt", "a") as file:
                file.write(f"{new_username}, {new_password}\n")
                print("New user registered successfully.")
                break
        else:
            print("Passwords do not match. Please try again.")


# Fuction to add new_task to tasks.txt
def add_task(username):
    task_username = input("Enter the username of the person the task is assigned to:\n")
    task_title = input("Enter the title of the task: \n")
    task_description = input("Enter the task description: \n")
    due_date = input("Enter the due date (YYYY-MM-DD):")

    # return string representing date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Wite new task data to tasks.txt file
    with open("tasks.txt", "a") as file:
        file.write(f"{task_username}, {task_title}, {task_description}, {current_date}, {due_date}, No\n")
    print("Task added successfully.")


# Funtion to view all tasks registered on taskManager.py
def view_all():

    # Open and read lines from tasks.txt file
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    for task in tasks:
        task_details = task.strip().split(", ")

        # Print information for each task in an easy to read format
        print("-"*50)
        print("Task: ", task_details[1])
        print("Assigned to: ", task_details[0])
        print("Date Assigned: ", task_details[3])
        print("Due Date: ", task_details[4])
        print("Task Complete?: ", task_details[5])
        print("Task Description: ", task_details[2])
        print("-"*50)
        print("\n")


# Function to view tasks for current user
def view_mine(username):
    # Open tasks.txt and readlines from file
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    my_tasks = []
    for task in tasks:
        task_details = task.strip().split(", ")
        if task_details[0] == username:
            my_tasks.append(task)

    # If no task assigned to the current user
    if not my_tasks:
        print("You currently have no tasks assigned.")
        return

    print("-" * 50)
    print("Your tasks: ")
    print("-" * 50)

    # Display each task with a corresponding number
    for i, task in enumerate(my_tasks, start=1):
        task_details = task.strip().split(", ")
        print(f"{i}. Assigned to: {task_details[0]}")
        print(f"   Task: {task_details[1]}")
        print(f"   Description: {task_details[2]}")
        print(f"   Date Created: {task_details[3]}")
        print(f"   Due Date: {task_details[4]}")
        print(f"   Completed: {task_details[5]}\n")

    while True:
        choice = input("Enter the number of the task you want to work on (-1 to go back to the main menu): ")
        if choice == '-1':
            break
        try:
            task_number = int(choice)
            if 1 <= task_number <= len(my_tasks):
                task_details = my_tasks[task_number - 1].strip().split(", ")
                if task_details[5] == "No":
                    print("Options: 'complete' or 'edit'")
                    mark_complete = input("Do you want to mark this task as complete (enter 'complete') or edit it (enter 'edit'): ")
                    if mark_complete == 'complete':
                        task_details[5] = "Yes"
                        my_tasks[task_number - 1] = ", ".join(task_details)

                        # Update tasks list with task details
                        task_index = tasks.index(task)  # Find the index of the task in tasks list
                        tasks[task_index] = my_tasks[task_number - 1]
                        with open("tasks.txt", "w") as file:
                            file.writelines(tasks)
                        print("Task marked as complete.")

                    elif mark_complete == 'edit':
                        field = input("What would you like to edit (username or due date): ").lower()
                        if field == 'username':
                            new_username = input("Enter the new username: ")
                            task_details[0] = new_username
                        elif field == 'due date':
                            new_due_date = input("Enter the new due date (YYYY-MM-DD): ")
                            task_details[4] = new_due_date
                        else:
                            print("Invalid field to edit.")
                        my_tasks[task_number - 1] = ", ".join(task_details)

                        # Update tasks list with task details
                        task_index = tasks.index(task)  # Find the index of the task in tasks list
                        tasks[task_index] = my_tasks[task_number - 1]
                        with open("tasks.txt", "w") as file:
                            file.writelines(tasks)
                        print("Task edited successfully.")

                    else:
                        print("Invalid action. Please enter 'complete' or 'edit'.")
                else:
                    print("You can only work on incomplete tasks.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# Function to display total number of tasks and the total number of users registered with taskManager.py
def display_statistics():
    # Read data from user_overview and task_overview user has to generate reports first
    try:
        with open("task_overview.txt", "r", encoding="utf-8") as task_file:
            task_overview = task_file.read()
            print("-" * 50)
            print("Task Overview:")
            print("-" * 50)
            print(task_overview)

        with open("user_overview.txt", "r", encoding="utf-8") as user_file:
            user_overview = user_file.read()
            print("-" * 50)
            print("User Overview:")
            print("-" * 50)
            print(user_overview)
    except FileNotFoundError:
        print("Reports have not been generated. Please generate reports before trying to display the overviews.")


# Function to generate task overview
def generate_task_overview():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task.strip().split(", ")[5] == "Yes")
    uncompleted_tasks = total_tasks - completed_tasks
    today = datetime.date.today()
    overdue_tasks = sum(1 for task in tasks if task.strip().split(", ")[5] == "No" and today > datetime.date.fromisoformat(task.strip().split(", ")[4]))

    incomplete_percentage = (uncompleted_tasks / total_tasks) * 100
    overdue_percentage = (overdue_tasks / total_tasks) * 100

    with open("task_overview.txt", "w", encoding="utf-8") as task_file:
        task_file.write(f"Total number of tasks: {total_tasks}\n")
        task_file.write(f"Total number of completed tasks: {completed_tasks}\n")
        task_file.write(f"Total number of uncompleted tasks: {uncompleted_tasks}\n")
        task_file.write(f"Total number of tasks that haven’t been completed and are overdue: {overdue_tasks}\n")
        task_file.write(f"Percentage of tasks that are incomplete: {incomplete_percentage:.2f}%\n")
        task_file.write(f"Percentage of tasks that are overdue: {overdue_percentage:.2f}%\n")


# Function to generater user over view reports
def generate_user_overview():
    with open("users.txt", "r") as file:
        users = file.readlines()

    total_users = len(users)

    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    task_count_by_user = {}
    completed_task_count_by_user = {}

    for task in tasks:
        task_details = task.strip().split(", ")
        assigned_to = task_details[0]
        if assigned_to in task_count_by_user:
            task_count_by_user[assigned_to] += 1
        else:
            task_count_by_user[assigned_to] = 1

        if task_details[5] == "Yes":
            if assigned_to in completed_task_count_by_user:
                completed_task_count_by_user[assigned_to] += 1
            else:
                completed_task_count_by_user[assigned_to] = 1

    with open("user_overview.txt", "w") as user_file:
        user_file.write(f"Total number of users registered with taskmanager.py: {total_users}\n")
        user_file.write(f"Total number of tasks that have been generated and tracked using task_manager.py: {len(tasks)}\n")

        for user, task_count in task_count_by_user.items():
            percentage_assigned = (task_count / len(tasks)) * 100
            percentage_completed = 0
            if user in completed_task_count_by_user:
                percentage_completed = (completed_task_count_by_user[user] / task_count) * 100

            user_file.write(f"\nUser: {user}\n")
            user_file.write(f"Total number of tasks assigned to that user: {task_count}\n")
            user_file.write(f"Percentage of the total number of tasks assigned to that user: {percentage_assigned:.2f}%\n")
            user_file.write(f"Percentage of tasks assigned to that user that have been completed: {percentage_completed:.2f}%\n")
            user_file.write(f"Percentage of tasks that must still be completed: {100 - percentage_completed:.2f}%\n")


# Display menu for admin
def admin_menu():
    print('''Select one of the following Options below:
    r - Register a user
    a - Add a task
    va - View all tasks
    vm - View my tasks
    gr - Generate Reports
    ds - Display Statistics
    e - Exit
    ''')


# Display menu for user
def user_menu():
    print('''Select one of the following Options below:
    a - Add a task
    va - View all tasks
    vm - View my tasks
    e - Exit
    ''')


# Main program
users = read_users()
print("Welcome to Task Manager!")

# Validate user credentials for login section
username = validate_credentials(users)
print(f"Welcome {username}!")

# Continue to display the menu until the user chooses to exit
while True:
    if is_admin(username):
        # admin menu displayed if username is admin
        admin_menu()
        menu = input("Enter your choice: ").lower()
        if menu == 'r':
            reg_user()
        elif menu == 'a':
            add_task(username)
        if menu == 'va':
            view_all()
        elif menu == 'vm':
            view_mine(username)
        elif menu == 'gr':
            print("Reports are being generated...")
            generate_task_overview()
            generate_user_overview()
            print("Reports generated.")
        elif menu == 'ds':
            display_statistics()
        elif menu == 'e':
            print("Goodbye!!!")
            break
        else:
            print("You have made a wrong choice. Please try again.")

    else:
        # Menu for username if not admin
        user_menu()
        menu = input("Enter your choice: ").lower()
        if menu == 'va':
            view_all()
            continue
        elif menu == 'vm':
            view_mine(username)
            continue
        elif menu == 'e':
            print("Goodbye!!!")
            break
        else:
            print("You have made a wrong choice. Please try again.")
            
# sources used
# https://www.simplilearn.com/tutorials/python-tutorial/python-check-if-file-exists
# https://builtin.com/data-science/python-list
# https://www.w3schools.com/python/gloss_python_function_arguments.asp
