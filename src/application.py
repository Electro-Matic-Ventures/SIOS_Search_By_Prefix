from ScrapeSIOS import ScrapeSIOS
from time import sleep

scraper = ScrapeSIOS()
scraper.search('6es75')
print(scraper.part_numbers)

stop_here = True
