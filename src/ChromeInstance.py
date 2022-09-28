from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

class ChromeInstance:

    def __init__(self):
        self.CHROME = Chrome(ChromeDriverManager().install())
        return