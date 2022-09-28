from ChromeInstance import ChromeInstance
from selenium.webdriver.common.by import By 
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions
from selenium.webdriver.common.by import By 
from time import sleep


class Scraper:

    def __init__(self, browser):
        self.browser = browser

    def click_button(self, x_path, timeout, delay):
        wait = WebDriverWait(self.browser, timeout)
        button = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, x_path)))
        sleep(delay)
        button.click()
        return

    def wait_for_target(self, x_path, timeout):
        wait = WebDriverWait(self.browser, timeout)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, x_path)))
        return

    def wait_for_link(self, x_path, timeout):
        wait = WebDriverWait(self.browser, timeout)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, x_path)))
        return

    def enter_text(self, x_path, timeout, delay, text):
        wait = WebDriverWait(self.browser, timeout)
        text_box = wait.until(expected_conditions.presence_of_element_located((By.XPATH, x_path)))
        time.sleep(delay)
        text_box.send_keys(text)
        return

    def search_for_text(self, text):
        return text in self.browser.page_source


class ScrapeSIOS:

    def __init__(self):
        self.BROWSER = Chrome(ChromeDriverManager().install())
        self.SCRAPER = Scraper(self.BROWSER)
        return

    def search(self, search_parameter: str):
        url = f'https://support.industry.siemens.com/cs/search?t=all&search={search_parameter}'
        self.BROWSER.get(url)
        self.accept_cookies()
        self.click_more()
        return

    def accept_cookies(self):
        x_path = '/html/body/div[3]//div/div/div/div/div[2]/div/div[2]/div/div/div/div/button[2]'
        self.SCRAPER.click_button(x_path, 10.0, 0.5)
        button.click()
        return

    def click_more(self):
        x_path = '/html/body/div[1]/div/div/div[4]/div/div/div[3]/div[2]/div/ul[1]/li[2]/div[2]'
        self.SCRAPER.click_button(x_path, 6.0, 0.1)
        return
