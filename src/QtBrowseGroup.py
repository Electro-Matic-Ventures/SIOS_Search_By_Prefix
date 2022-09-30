from PySide6.QtWidgets import QGroupBox , QLineEdit, QPushButton, QHBoxLayout


class QtBrowseGroup(QGroupBox):

    def __init__(self, label):
        QGroupBox.__init__(self, label)
        self.path_display = QLineEdit()
        self.browse_button = QPushButton('Browse')
        self.__layout = QHBoxLayout()
        self.__layout.addWidget(self.path_display)
        self.__layout.addWidget(self.browse_button)
        self.setLayout(self.__layout)
        return