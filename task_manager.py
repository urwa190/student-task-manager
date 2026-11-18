"""Student Task Manager - console application."""


class TaskManager:
    def __init__(self):
        self.tasks = []
        self._next_id = 1

    def add_task(self, title):
        task = {"id": self._next_id, "title": title, "done": False}
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