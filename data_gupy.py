from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from helpers.utilities import Utilities
from time import sleep
import pandas as pd

from selenium.webdriver.support.ui import Select


class Gupy:
    __slots__ = "robot"
    def __init__(self) -> None:
        self.robot = Utilities()


    def start_browser(self):
        try:
            self.robot.open_chrome()
        except Exception as e:
            raise

    def select_url(self, url):
        try:
            self.robot.browser.get(url)
            self.robot.browser.delete_all_cookies()
            sleep(30)
        except Exception as e:
            raise
        
    