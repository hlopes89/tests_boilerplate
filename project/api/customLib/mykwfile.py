from robot.api.deco import keyword
from lib.core import Core, Browser


class TestLib:
    ROBOT_LIBRARY_SCOPE = 'TEST CASE'
    # TEST SUITE | GLOBAL

    def __init__(self) -> None:
        self.core = Core()
        self.browser = Browser()

    @keyword("call core")
    def call_core(self):
        pass

    @keyword('open google "${url}"')
    def open_google(self, url):
        self.core.log(url)
        self.browser.open_driver(url)
        self.browser.go_to("https://www.google.com")
