# Simple Command-Line To-Do List
# Author: Your Name

def show_menu():
    print("\n=== To-Do List ===")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet!")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("\nEnter new task: ")
    tasks.append(task)
    print(f"Added: {task}")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter task number to remove: "))
            removed = tasks.pop(task_num - 1)
            print(f"Removed: {removed}")
        except (ValueError, IndexError):
            print("Invalid task number!")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("\nChoose an option: ")
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
