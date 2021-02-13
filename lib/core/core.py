from robot.libraries.BuiltIn import BuiltIn


class Core:

    def __init__(self) -> None:
        self.bi = BuiltIn()

    def run_kw(self, kw):
        self.bi.run_keyword(kw)

    def from_core(self):
        print("from core")
