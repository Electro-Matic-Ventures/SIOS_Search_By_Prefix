from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class QtStatusMessage(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.message = QLabel()
        self.message.setWordWrap(True)
        self.__layout = QVBoxLayout()
        self.__layout.setContentsMargins(10, 10, 10, 10)
        self.__layout.addWidget(self.message)
        self.setLayout(self.__layout)
        return
