class FileManager:

    def save_to_file(self, file_name:str, data:str)-> None:
        with open(file_name, 'w') as file_:
            file_.write(data)
        return