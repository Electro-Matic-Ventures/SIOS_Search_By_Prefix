from PySide6.QtWidgets import QGroupBox, QLabel, QLineEdit, QHBoxLayout


class QtLabeledInputGroup(QGroupBox):

    def __init__(self, label):
        QGroupBox.__init__(self, label)
        self.input = QLineEdit()
        self.__layout = QHBoxLayout()
        self.__layout.addWidget(self.input)
        self.setLayout(self.__layout)
        return