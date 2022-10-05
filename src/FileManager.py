from os.path import getsize


class FileManager:

    def read_file(file_name:str)->str:
        with open(file_name, 'r') as file_:
            text = file_.read()
        return text

    def create_file(file_name:str, data:str)-> None:
        with open(file_name, 'w') as file_:
            file_.write(data)
        return

    def append_to_file(file_name:str, data:str)->None:
        _data = data
        if FileManager.__is_blank(file_name):
            FileManager.__append_action(file_name, _data)
            return
        if FileManager.__last_character_in_file(file_name) != '\n':
            _data = '\n' + _data
            FileManager.__append_action(file_name, _data)
            return
        FileManager.__append_action(file_name, _data)
        return

    def __append_action(file_name:str, data:str)->None:
        with open(file_name, 'a') as file_:
            file_.write(data)
        return

    def __is_blank(file_name:str)->bool:
        return getsize(file_name) == 0
    
    def __last_character_in_file(file_name:str)->str:
        with open(file_name, 'r') as file_:
            data = file_.read()
        return data[-1]