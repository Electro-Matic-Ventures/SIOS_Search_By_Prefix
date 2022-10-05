from re import sub


class StringExtension:

    def __init__(self):
        return
        
    def replace_all(self, haystacks, needles, new_needle):
        new_haystacks = []
        if new_needle in needles:
            return haystacks
        for haystack in haystacks:
            for needle in needles:
                while haystack.find(needle) >= 0:
                    haystack = haystack.replace(needle, new_needle)
            new_haystacks.append(haystack)
        return new_haystacks

    def capitalize_first_letter_of_each_word(self, value):
        strings = value.split(' ')
        _return = ''
        for _string in strings:
            _string = _string.lower()
            _return += _string[:1].upper() + _string[1:] + ' '
        return _return[:-1]

    def just_alpha_numeric(self, string):
        return sub('[^a-zA-Z0-9]','', string).strip()

    def split_multiple_delimeters(self, value, delimeters):
        if len(delimeters) == 0:
            return value
        delimeter = delimeters.pop()
        out = []
        for x in value:
            out.extend(x.split(delimeter))
        return self.split_multiple_delimeters(out, delimeters)

    def string_number_to_float(self, value):
        value = value.replace(',','.')
        count = value.count('.')
        value = value.replace('.', '', count - 1)
        return float(value)

    def interrior(self, text: str, delimeter: str):
        '''
        interior is intended to be used to get the text between quotes, parentheses, or brackets.
        presently, it cannot handle nested cases.
        this functionlity is planned for a future version.
        '''
        position = text.find(delimeter)
        text = text[1 + position :]
        position = text.find(delimeter)
        text = text[: position]
        return text