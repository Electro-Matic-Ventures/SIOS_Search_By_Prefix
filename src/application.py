from ScrapeSIOS import ScrapeSIOS
from ListExtension import ListExtension
from FileManager import FileManager


scraper = ScrapeSIOS()
scraper.search('6av2')
part_numbers = ListExtension().to_string_one_element_per_line(scraper.part_numbers)
FileManager().save_to_file('./part_numbers.csv', part_numbers)