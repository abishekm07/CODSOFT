# todo_list.py

from typing import List, Dict

class ToDoList:
    def __init__(self):
        self.tasks: List[Dict[str, str]] = []

    def add_task(self, title: str) -> None:
        self.tasks.append({"title": title, "status": "Pending"})
        print(f"Task added: '{title}'")

    def view_tasks(self) -> None:
        if not self.tasks:
            print("No tasks in your to-do list.")
            return

        print("\nYour Tasks:")
        for idx, task in enumerate(self.tasks, 1):
            print(f"{idx}. {task['title']} - {task['status']}")

    def mark_done(self, task_number: int) -> None:
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]["status"] = "Completed"
            print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number: int) -> None:
        if 1 <= task_number <= len(self.tasks):
            removed = self.tasks.pop(task_number - 1)
            print(f"Deleted task: '{removed['title']}'")
        else:
            print("Invalid task number.")

def main() -> None:
    todo = ToDoList()
    
    while True:
        print("\n=== To-Do List Menu ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            title = input("Enter the task title: ").strip()
            todo.add_task(title)
        elif choice == '2':
            todo.view_tasks()
        elif choice == '3':
            try:
                num = int(input("Enter task number to mark as completed: "))
                todo.mark_done(num)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            try:
                num = int(input("Enter task number to delete: "))
                todo.delete_task(num)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
