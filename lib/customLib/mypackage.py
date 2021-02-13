from robot.api.deco import keyword
from lib.core.core import Core


class TestLib:
    ROBOT_LIBRARY_SCOPE = 'TEST CASE'
    # TEST SUITE | GLOBAL

    def __init__(self) -> None:
        pass

    @keyword("hello")
    def hello(self):
        print("hello")

    @keyword("bye")
    def bye(self):
        print("bye")

    @keyword("call core")
    def call_core(self):
        Core().run_kw("hello")
        Core().run_kw("bye")
