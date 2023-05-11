import sys
import ui

class Menu():

    def __init__(self, ui):
        self.ui = ui

    def exitProgramm(self) -> None:
        
        self.ui.close()