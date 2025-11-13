# Simple To-Do List with Priorities

tasks = []

def add_task(description, priority):
    if priority not in ['high', 'medium', 'low']:
        print("Invalid priority. Use: high, medium, or low.")
        return
    tasks.append({'description': description, 'priority': priority})
    print(f"Task added: '{description}' with priority '{priority}'.")

def show_tasks():
    priority_order = {'high': 1, 'medium': 2, 'low': 3}
    sorted_tasks = sorted(tasks, key=lambda x: priority_order[x['priority']])
    if not sorted_tasks:
        print("No tasks to show.")
        return
    print("\nTasks (sorted by priority):")
    for idx, task in enumerate(sorted_tasks, 1):
        print(f"{idx}. [{task['priority'].capitalize()}] {task['description']}")

def remove_task(index):
    if index < 1 or index > len(tasks):
        print("Invalid task number.")
        return
    removed = tasks.pop(index - 1)
    print(f"Removed task: '{removed['description']}'.")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            desc = input("Enter task description: ")
            prio = input("Enter priority (high/medium/low): ").lower()
            add_task(desc, prio)
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            show_tasks()
            if tasks:
                try:
                    idx = int(input("Enter task number to remove: "))
                    remove_task(idx)
                except ValueError:
                    print("Please enter a valid number.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()