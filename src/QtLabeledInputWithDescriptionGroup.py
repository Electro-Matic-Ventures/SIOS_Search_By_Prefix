from PySide6.QtWidgets import QGroupBox, QLabel, QLineEdit, QHBoxLayout


class QtLabeledInputWithDescriptionGroup(QGroupBox):

    def __init__(self, group_label:str, description_label:str):
        QGroupBox.__init__(self, group_label)
        self.description = QLabel(description_label)
        self.input = QLineEdit()
        self.__layout = QHBoxLayout()
        self.__layout.addWidget(self.description)
        self.__layout.addWidget(self.input)
        self.setLayout(self.__layout)
        return