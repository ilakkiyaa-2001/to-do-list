def add_items(n):
    with open("to-do.txt", "a") as f:        
        for i in range(n):
            e = input("Enter the task: ")
            f.write(e + '\n')
    print("Task has been added successfully")


def show_task():
    try:
        with open("to-do.txt", 'r') as f:
            for i in f.readlines():
                print(i.strip('\n'))
    except FileNotFoundError:
        print("File Not Found")


def remove_task():
    try:
        with open('to-do.txt', 'r') as f:
            lines = f.readlines()

        show_task()
        tasks_to_remove = input("Enter tasks to be removed (separate multiple tasks with commas): ").split(',')
        tasks_to_remove = [task.strip() for task in tasks_to_remove]

        with open('to-do.txt', 'w') as f:
            for line in lines:
                if line.strip() not in tasks_to_remove:
                    f.write(line)

        print("Task(s) removed successfully")
    except FileNotFoundError:
        print("The file is not found")
    except ValueError:
        print("Please enter valid input")


while True:
    print("Welcome to the To-Do list")
    print("Please select from the menu:")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Remove task")
    print("4. Exit")
    print()

    try:
        number = int(input("Enter your choice: "))
        
        if number == 1:
            no = int(input("Enter number of tasks to be added: "))
            add_items(no)
        elif number == 2:
            show_task()
        elif number == 3:
            remove_task()
        elif number == 4:
            print("Exiting the To-Do list.")
            break
        else:
            print("Invalid option, please choose again.")
    except ValueError:
        print("Please enter a valid number.")
