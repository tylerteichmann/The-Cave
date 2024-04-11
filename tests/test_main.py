import os
import unittest
from .context import main

class test_main(unittest.TestCase):

    def StartMenu_StartMenuRuns_StartMenuDisplays(self):
        # Arrange

        # Act
        main.start_menu()
        os.system("exit")

        # Assert
        self.assertTrue()