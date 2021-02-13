from robot.api.deco import keyword
from lib.core.core import Core


class TestLib:
    ROBOT_LIBRARY_SCOPE = 'TEST CASE'
    # TEST SUITE | GLOBAL

    def __init__(self) -> None:
        self.core = Core()

    @keyword("call core")
    def call_core(self):
        pass

    @keyword('open google "${url}"')
    def open_google(self, url):
        self.core.log(url)
        self.core.open_driver(url)
