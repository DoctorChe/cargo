from PyQt5.QtWidgets import QListWidget


class TasksListView(QListWidget):
    def __init__(self, parent):
        QListWidget.__init__(self, parent)
