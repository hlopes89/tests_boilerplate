import sys
import os
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from robot.api import logger


class Core:
    def __init__(self) -> None:
        self.bi = BuiltIn()

    def log(self, msg):
        logger.console(msg)

    def run_kw(self, kw):
        self.bi.run_keyword(kw)


class Browser:
    CROMEDRIVER_PATH = "lib/chromedriver/chromedriver"

    def open_driver(self, url):
        self.driver = Chrome(executable_path=self.CROMEDRIVER_PATH)
        self.driver.get(url)

    def go_to(self, url):
        self.driver.get(url)
