from FileManager import FileManager
from StringExtension import StringExtension


class CleanCSV:

    self.__text: str

    def __init__(self, input_file_name:str, output_file_name:str):
        self.__text = FileManager.read_file(file_name)
        data = self.__just_alpha_numeric_and_new_line()
        FileManager.create_file(output_file_name, data)
        return

    def __just_alpha_numeric_and_new_line()->str:
        text_list = self.__text.split('\n')
        text = ''
        for line in text:
            text += f'{StringExtension().just_alpha_numeric(line)}\n'
        while text[-1] == '\n':
            text = text[:-1]
        return text
