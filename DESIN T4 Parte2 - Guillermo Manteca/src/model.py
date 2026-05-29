class TaskModel:
    def __init__(self):
        self._tasks = []

    def get_tasks(self):
        return self._tasks

    def add_task(self, task_text):
        if task_text.strip():
            self._tasks.append(task_text)
            return True
        return False

    def remove_task(self, index):
        if 0 <= index < len(self._tasks):
            self._tasks.pop(index)
            return True
        return False