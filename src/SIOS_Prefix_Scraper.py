from QtBrowseGroup import QtBrowseGroup
from QtLabeledInputGroup import QtLabeledInputGroup
from QtExecuteButton import QtExecuteButton
from QtStatusMessage import QtStatusMessage
from ScrapeSIOS import ScrapeSIOS
from ListExtension import ListExtension
from FileManager import FileManager
from Timestamp import Timestamp
from Log import Log
from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QVBoxLayout, QFileDialog, QSizePolicy
from sys import exit, argv


class GUI(QMainWindow):

    def __init__(self):
        # SIZE CONSTANTS
        self.__WINDOW_HEIGHT = 300
        self.__WINDOW_WIDTH = 400
        self.__INTERSTITIAL_SPACING = 15
        # MAIN WINDOW SETUP
        QMainWindow.__init__(self)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        # MAIN WINDOW SIZE
        self.__set_main_window_size()
        # TITLE
        self.setWindowTitle("Siemens SIOS Prefix Scraper")
        # WIDGETS
        self.enter_prefix_group = QtLabeledInputGroup('Enter Prefix')
        self.output_path_group = QtBrowseGroup('Select Path for Output Files')
        self.execute_button = QtExecuteButton()    
        self.status_message = QtStatusMessage()
        # LAYOUT
        self.__layout = QVBoxLayout()
        self.__configure_layout()
        self.__add_widgets_to_layout()
        self.__set_widget_sizes()
        self.central_widget.setLayout(self.__layout)
        # CONNECTIONS
        self.__make_connections()
        return

    def __set_main_window_size(self)-> None:
        self.setFixedHeight(self.__WINDOW_HEIGHT)
        self.setFixedWidth(self.__WINDOW_WIDTH)
        return

    def __configure_layout(self)-> None:
        self.__layout.setContentsMargins(
            self.__INTERSTITIAL_SPACING, 
            self.__INTERSTITIAL_SPACING, 
            self.__INTERSTITIAL_SPACING, 
            self.__INTERSTITIAL_SPACING)
        self.__layout.setSpacing(self.__INTERSTITIAL_SPACING)
        return

    def __add_widgets_to_layout(self)-> None:
        self.__layout.addWidget(self.enter_prefix_group, 1, Qt.AlignLeft)
        self.__layout.addWidget(self.output_path_group, 1, Qt.AlignLeft)
        self.__layout.addWidget(self.execute_button, 1, Qt.AlignLeft)
        self.__layout.addWidget(self.status_message, 1, Qt.AlignLeft)
        return

    def __set_widget_sizes(self)-> None:
        self.__set_enter_prefix_group_size()
        self.__set_output_path_group_size()
        self.__set_execute_button_size()
        self.__set_status_message_size()
        return

    def __set_enter_prefix_group_size(self)-> None:
        width = self.__WINDOW_WIDTH - 2 * self.__INTERSTITIAL_SPACING
        self.enter_prefix_group.setFixedWidth(width)
        return

    def __set_output_path_group_size(self)-> None:
        width = self.__WINDOW_WIDTH - 2 * self.__INTERSTITIAL_SPACING
        self.output_path_group.setFixedWidth(width)
        return

    def __set_execute_button_size(self)-> None:
        width = self.__WINDOW_WIDTH - 2 * self.__INTERSTITIAL_SPACING
        self.execute_button.setFixedWidth(width)
        return

    def __set_status_message_size(self)-> None:
        width = self.__WINDOW_WIDTH - 2 * self.__INTERSTITIAL_SPACING
        self.status_message.setFixedWidth(width)
        return

    def __make_connections(self)-> None:
        # OUTPUT PATH SELECTION
        self.output_path_group.browse_button.clicked.connect(self.__output_path_selection_button_action)
        # EXECUTE BUTTON
        self.execute_button.button.clicked.connect(self.__execute_button_action)
        return

    def __output_path_valid(self)-> bool:
        return len(self.output_path_group.path_display.text()) > 0

    def __prefix_valid(self)-> bool:
        return len(self.enter_prefix_group.input.text()) > 0

    def __form_inputs_valid(self)-> bool:
        return  self.__output_path_valid() and self.__prefix_valid()

    def __notifiy_invalid_form_data(self)-> None:
        if not self.__output_path_valid():
            self.__invalid_output_path_notification()
        if not self.__prefix_valid():
            self.__invalid_prefix_notification()
        return

    def __invalid_output_path_notification(self)-> None:
        timestamp_ = Timestamp().one_true_format()
        Log('./').add_event(f'Invalid output path specified. Process terminated at {timestamp_}')
        self.status_message.message.setText(f'Invalid output path specified. Process terminated at {timestamp_}')
        return

    def __invalid_prefix_notification(self)-> None:
        timestamp_ = Timestamp().one_true_format()
        Log('./').add_event(f'No prefix provided. Process terminated at {timestamp_}')
        self.status_message.message.setText(f'No prefix provided. Process terminated at {timestamp_}.')
        return

    def __return_data_invalid(self, data:list)-> bool:
        return len(data) == 0

    def __notify_no_data_found(self)-> None:
        Log(output_path).add_event(f'Scraping complete. No data found.')
        self.status_message.message.setText(f'Scraping complete, no data found at {Timestamp().one_true_format()}')
        return

    def __notify_successful_run(self, output_path:str='./')-> None:
        Log(output_path).add_event(f'Scraping complete.')
        self.status_message.message.setText(f'Scraping Completed at {Timestamp().one_true_format()}')
        return

    def __notify_exception(self, exception_text:Exception, output_path:str='./')-> None:
        Log(output_path).add_event(f'{exception_text}')
        self.status_message.message.setText(f'{exception_text}')

    @Slot()
    def __output_path_selection_button_action(self)-> None:
        path_name = QFileDialog.getExistingDirectory(self, 'Browse For Output Path', '')
        self.output_path_group.path_display.setText(path_name)
        return

    @Slot()
    def __execute_button_action(self):
        try:
            # FORM VALIDATION
            if not self.__form_inputs_valid():
                self.__notifiy_invalid_form_data()
                return
            # GET FORM VARIABLES
            prefix = self.enter_prefix_group.input.text()
            output_path = self.output_path_group.path_display.text()
            timestamp_ = Timestamp().one_true_filesave()
            save_file_name = f'{output_path}/sios_prefix_{prefix}_scraped_{timestamp_}.csv'
            # INSTATIATE SCRAPING APPLICATION
            scraper = ScrapeSIOS()
            # SCRAPE SIOS
            scraper.search(prefix)
            # TRANSFORM DATA
            output = ListExtension().to_string_one_element_per_line(scraper.part_numbers)
            # NO DATA FOUND
            if self.__return_data_invalid(output):
                self.__notifiy_invalid_form_data()
                return
            # SAVE TO FILE
            FileManager().save_to_file(save_file_name, output)
            # SUCCESSFUL RUN
            self.__notify_successful_run(output_path)
            return
        except Exception as e:
            self.__notify_exception(e, './')
            return


if __name__ == "__main__":
    app = QApplication(argv)
    widget = GUI()
    widget.show()
    exit(app.exec())