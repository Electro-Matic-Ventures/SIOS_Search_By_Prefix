from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout


class QtExecuteButton(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.button = QPushButton('Begin Scraping')
        self.button.setFixedHeight(30)
        self.__layout = QVBoxLayout()
        self.__layout.setContentsMargins(0, 10, 0, 10)
        self.__layout.addWidget(self.button)
        self.setLayout(self.__layout)
        return