import sys
from PySide6.QtWidgets import QApplication
from src.model import TaskModel
from src.view import TaskView
from src.controller import TaskController

def main():
    app = QApplication(sys.argv)

    # Inicialización del patrón MVC
    model = TaskModel()
    view = TaskView()
    controller = TaskController(model, view)

    view.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()