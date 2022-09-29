from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions
from selenium.webdriver.common.by import By 
from time import sleep


class Scraper:

    def __init__(self, browser):
        self.browser = browser

    def click_button_x_path(self, x_path, timeout, delay):
        wait = WebDriverWait(self.browser, timeout)
        button = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, x_path)))
        sleep(delay)
        button.click()
        return

    def click_button_selector(self, selector:str, timeout:float, delay:float)-> None:
        wait = WebDriverWait(self.browser, timeout)
        button = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, selector)))
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