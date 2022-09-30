from datetime import datetime


class Timestamp:

    def __inti__(self):
        return 

    def one_true_format(self)-> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def one_true_filesave(self)-> str:
        return datetime.now().strftime("%Y_%m_%d_%H_%M_%S")