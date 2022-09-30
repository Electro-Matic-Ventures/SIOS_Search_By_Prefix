from Timestamp import Timestamp

class Log:

    def __init__(self, path):
        if path == '': path = '.'
        self.__path = f'{path}/process_log.csv'
        return

    def create(self):
        with open(self.__path, 'w') as f:
            f.write(f'{Timestamp().one_true_format()}; log created\n')
        return

    def add_event(self, text):
        with open(self.__path, 'a') as f:
            f.write(f'{Timestamp().one_true_format()}; {text}\n')
        return