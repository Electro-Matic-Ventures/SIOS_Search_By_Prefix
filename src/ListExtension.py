class ListExtension:

    def to_string_one_element_per_line(self, data:list)-> str:
        string_ = ''
        for element in data:
            string_ += f'{element}\n'
        return string_[:-1]