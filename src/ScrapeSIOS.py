from ChromeInstance import ChromeInstance
from Scraper import Scraper
from selenium.webdriver.common.by import By 
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class ScrapeSIOS:

    def __init__(self):
        self.__PAGE_DWELL = 0.1
        self.__TIMEOUT = 10.0
        self.__DELAY = 0.1
        self.__BROWSER = Chrome(ChromeDriverManager().install())
        self.__SCRAPER = Scraper(self.__BROWSER)
        self.part_numbers = []
        return


    def more_pages_available(self)-> bool:
        more_pages = '#content > div > div > div.s-left-wide > div.globalsearch > div:nth-child(2) > div > div.pager > div.next'
        last_page = '#content > div > div > div.s-left-wide > div.globalsearch > div:nth-child(2) > div > div.pager > div.next.disabled'
        try:
            self.__BROWSER.find_element(by=By.CSS_SELECTOR, value=selector)
        except:
            self.__BROWSER.find_element(By.CSS_SELECTOR, last_page)

    def search(self, search_parameter: str):
        url = f'https://support.industry.siemens.com/cs/search?t=all&search={search_parameter}'
        self.__BROWSER.get(url)
        self.__accept_cookies()
        self.__click_more()
        self.click_view_100_items()
        self.part_numbers = self.get_part_numbers_on_all_pages()
        return

    def __accept_cookies(self)-> None:
        sleep(5.0)
        button = self.__BROWSER.execute_script('return document.querySelector("#usercentrics-root").shadowRoot.querySelector("#uc-center-container > div.sc-bYoBSM.dxGEzT > div > div > div > button:nth-child(2)");')
        button.click()
        return

    def __click_more(self)-> None:
        x_path = '/html/body/div[1]/div/div/div[4]/div/div/div[3]/div[2]/div/ul[1]/li[2]/div[2]'
        self.__SCRAPER.click_button_x_path(x_path, self.__TIMEOUT, self.__DELAY)
        return
    
    def __get_product_count(self)-> str:
        x_path = '/html/body/div[1]/div/div/div[4]/div/div/div[3]/div[2]/div[1]/div[1]'
        self.__SCRAPER.wait_for_target(x_path, self.__TIMEOUT)
        return self.__BROWSER.find_element(By.XPATH, x_path).text
        
    def click_view_100_items(self)-> None:
        x_path = '/html/body/div[1]/div/div/div[4]/div/div/div[3]/div[2]/div[2]/div/div[2]/span[4]'
        self.__SCRAPER.click_button_x_path(x_path, self.__TIMEOUT, self.__DELAY)
        return

    def get_part_numbers_on_all_pages(self):
        part_numbers = []
        count = int(self.__get_product_count())
        remaining = count
        while remaining > 0:
            self.__wait_for_page_to_load(remaining)
            sleep(self.__PAGE_DWELL)
            count_on_page = self.__calculate_part_number_count_for_this_page(remaining)
            part_numbers_on_page = self.__get_part_numbers_on_page(count_on_page)
            part_numbers = self.__add_to_list(part_numbers_on_page, part_numbers)
            remaining -= count_on_page
            self.__click_next_page_button()
        return part_numbers

    def __wait_for_page_to_load(self, remaining: int)-> None:
        x_path = self.__wait_for_this_x_path(remaining)
        self.__SCRAPER.wait_for_target(x_path, self.__TIMEOUT)
        return

    def __add_to_list(self, add_this: list, to_this:list)-> list:
        for element in add_this:
            to_this.append(element)
        return to_this

    def __calculate_part_number_count_for_this_page(self, remaining: int)-> int:
        if remaining >= 100: return 100
        return remaining

    def __wait_for_this_x_path(self, remaining: int)-> str:
        if remaining >= 100: 
            # x_path of 100th part number on page
            return '/html/body/div[1]/div/div/div[4]/div/div/div[3]/div[2]/div[4]/div[100]/div/div/div/div[2]/div[1]/div[1]/a'
        # x_path of "contact & partners" link on right side of page
        return '/html/body/div[1]/div/div/div[4]/div/div/div[4]/div[2]/div/div[3]/div[7]/div/div[1]/div/div[2]/div'

    def __get_part_numbers_on_page(self, count: int)-> list:
        class_ = 'product-value'
        elements = []
        while len(elements) < count:
            elements = self.__BROWSER.find_elements(by=By.CLASS_NAME, value=class_)
        try:
            return [element.text for element in elements]
        except Exception as e:
            return self.__get_part_numbers_on_page(count)

    def __click_next_page_button(self)-> None:
        selector = '#content > div > div > div.s-left-wide > div.globalsearch > div:nth-child(2) > div > div.pager > div.next'
        self.__SCRAPER.click_button_selector(selector, self.__TIMEOUT, self.__DELAY)
        return