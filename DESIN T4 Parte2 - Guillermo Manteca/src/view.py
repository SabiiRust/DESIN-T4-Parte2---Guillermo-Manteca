from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget

class TaskView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor de Tareas - MVC")
        self.resize(400, 300)

        # Widget central y Layout principal
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        # Entrada de texto y botón añadir
        self.input_layout = QHBoxLayout()
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Escribe una nueva tarea...")
        self.add_button = QPushButton("Añadir")
        self.input_layout.addWidget(self.task_input)
        self.input_layout.addWidget(self.add_button)

        # Lista de tareas y botón eliminar
        self.task_list = QListWidget()
        self.delete_button = QPushButton("Eliminar Tarea Seleccionada")

        # Integrar al layout principal
        self.main_layout.addLayout(self.input_layout)
        self.main_layout.addWidget(self.task_list)
        self.main_layout.addWidget(self.delete_button)