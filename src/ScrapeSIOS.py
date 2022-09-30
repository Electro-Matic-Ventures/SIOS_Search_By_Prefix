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
        self.__more_pages_available = True
        self.part_numbers = []
        return

    def search(self, search_parameter: str):
        url = f'https://support.industry.siemens.com/cs/search?t=all&search={search_parameter}'
        self.__BROWSER.get(url)
        self.__accept_cookies()
        self.__click_more()
        self.__click_view_100_items()
        self.part_numbers = self.__get_part_numbers_on_all_pages()
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
        
    def __click_view_100_items(self)-> None:
        x_path = '/html/body/div[1]/div/div/div[4]/div/div/div[3]/div[2]/div[2]/div/div[2]/span[4]'
        self.__SCRAPER.click_button_x_path(x_path, self.__TIMEOUT, self.__DELAY)
        return

    def __get_part_numbers_on_all_pages(self):
        part_numbers = []
        while self.__more_pages_available:
            self.__more_pages_available = self.__check_for_more_pages()
            count_on_page = self.__calculate_part_number_count_for_this_page()
            part_numbers_on_page = self.__get_part_numbers_on_page(count_on_page)
            part_numbers = self.__add_to_list(part_numbers_on_page, part_numbers)
            if self.__more_pages_available:
                self.__click_next_page_button()
        return part_numbers

    def __get_product_count(self)-> str:
        x_path = '/html/body/div[1]/div/div/div[4]/div/div/div[3]/div[2]/div[1]/div[1]'
        self.__SCRAPER.wait_for_target(x_path, self.__TIMEOUT)
        return self.__BROWSER.find_element(By.XPATH, x_path).text

    def __add_to_list(self, add_this: list, to_this:list)-> list:
        for element in add_this:
            to_this.append(element)
        return to_this

    def __calculate_part_number_count_for_this_page(self)-> int:
        if self.__more_pages_available: return 100
        return int(self.__get_product_count()) % 100

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

    def __check_for_more_pages(self)-> bool:
        # more_pages = '#content > div > div > div.s-left-wide > div.globalsearch > div:nth-child(2) > div > div.pager > div.next'
        last_page = '#content > div > div > div.s-left-wide > div.globalsearch > div:nth-child(2) > div > div.pager > div.next.disabled'
        try:
            self.__BROWSER.find_element(by=By.CSS_SELECTOR, value=last_page)
            return False
        except Exception as e:
            return True