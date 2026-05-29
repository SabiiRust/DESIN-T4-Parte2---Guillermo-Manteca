from src.model import TaskModel
from src.view import TaskView

class TaskController:
    def __init__(self, model: TaskModel, view: TaskView):
        self.model = model
        self.view = view

        # Conectar señales (eventos de la vista) a los métodos del controlador
        self.view.add_button.clicked.connect(self.add_task)
        self.view.task_input.returnPressed.connect(self.add_task)
        self.view.delete_button.clicked.connect(self.delete_task)

    def add_task(self):
        text = self.view.task_input.text()
        if self.model.add_task(text):
            self.view.task_input.clear()
            self.update_view()

    def delete_task(self):
        selected_row = self.view.task_list.currentRow()
        if selected_row >= 0:
            self.model.remove_task(selected_row)
            self.update_view()

    def update_view(self):
        self.view.task_list.clear()
        for task in self.model.get_tasks():
            self.view.task_list.addItem(task)