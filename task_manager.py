"""Student Task Manager - console application."""


class TaskManager:
    def __init__(self):
        self.tasks = []
        self._next_id = 1

    def add_task(self, title):
        """Add a task. Raises ValueError if the title is empty."""
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty.")
        task = {"id": self._next_id, "title": title.strip(), "done": False}
        self.tasks.append(task)
        self._next_id += 1
        return task

    def get_tasks(self):
        return list(self.tasks)

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["done"] = True
                return True
        return False

    def delete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                return True
        return False


def show_tasks(manager):
    tasks = manager.get_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for t in tasks:
        mark = "x" if t["done"] else " "
        print(f"[{mark}] {t['id']}. {t['title']}")


def main():
    manager = TaskManager()
    while True:
        print("\n1) Add  2) Show  3) Complete  4) Delete  5) Exit")
        choice = input("Choose: ").strip()
        try:
            if choice == "1":
                manager.add_task(input("Title: "))
            elif choice == "2":
                show_tasks(manager)
            elif choice == "3":
                ok = manager.complete_task(int(input("Task ID: ")))
                print("Task completed." if ok else "Task not found.")
            elif choice == "4":
                ok = manager.delete_task(int(input("Task ID: ")))
                print("Task deleted." if ok else "Task not found.")
            elif choice == "5":
                break
            else:
                print("Invalid choice.")
        except ValueError as err:
            print(f"Error: {err}")


if __name__ == "__main__":
    main()