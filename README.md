# Task Manager

## Project Description
Task Manager is a program designed for a small business to efficiently manage tasks assigned to each team member. It provides two different menus: one for administrators and another for regular users. Administrators have special privileges, such as registering new users and adding tasks. Users can view tasks assigned to them, add new tasks, and more.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Credits](#credits)

## Installation
To install the project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/task-manager.git`
2. Navigate to the project directory: `cd task-manager`
3. Run the program: `python task_manager.py`

## Usage
After installing the project, you can use it by running the `task_manager.py` file. The program will prompt you to enter your username and password. Depending on whether you are an administrator or a user, you will have access to different menu options.

### Administrator Menu
- **r - Register a user**: Add new users to the system.
- **a - Add a task**: Assign tasks to users.
- **va - View all tasks**: Display all tasks in the system.
- **vm - View my tasks**: Display tasks assigned to the administrator.
- **gr - Generate Reports**: Generate task and user overview reports.
- **ds - Display Statistics**: Display statistics based on generated reports.
- **e - Exit**: Exit the program.

### User Menu
- **a - Add a task**: Add new tasks.
- **va - View all tasks**: Display all tasks in the system.
- **vm - View my tasks**: Display tasks assigned to the user.
- **e - Exit**: Exit the program.

## Screenshots
![Login](/screenshots/login.png)

*Initial login screen where users are prompted to enter their username and password.*

![Admin Menu 2](/screenshots/admin_menu.png)

*The available options for admin registering a user, adding a task, viewing all tasks, generating reports, displaying statistics, and exiting.*

![User Menu](/screenshots/user_menu.png)

*The user menu, showcasing options such as adding a task, viewing all tasks, viewing user-specific tasks, and exiting.*

![Registration process](/screenshots/registration.png)

*Process of registering a new user. Images of the user registration interface.*

![Task Addition](/screenshots/addition.png)

*The process of adding a new task, including entering details such as task title, description, due date, etc.*

![View All Tasks](/screenshots/view_all.png)

*The output when selecting the option to view all tasks, displaying a list of tasks in the system.*

![View User-Specific Tasks](/screenshots/view_mine.png)

*The output when a user views their specific tasks, including information like task title, description, due date, and completion status.*


![Generate Reports](/screenshots/generate.png)

*The process of generating reports, and display the generated reports or overviews.*

![Display Statictics](/screenshots/display.png)

*The output when selecting the option to display statistics, showing information about the total number of users, tasks, completion percentages, etc.*

![Exit Confirmation](/screenshots/exit.png)

*The exit confirmation message when choosing to exit the program.*


## Credits
- Author: Marcelle Meintjes
- [Reference 1](https://www.simplilearn.com/tutorials/python-tutorial/python-check-if-file-exists)
- [Reference 2](https://builtin.com/data-science/python-list).
- [Reference 3](https://www.w3schools.com/python/gloss_python_function_arguments.asp)

