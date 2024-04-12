import os
import unittest
import sys
sys.path.append("..")

import main


class test_main(unittest.TestCase):

    def StartMenu_StartMenuRuns_StartMenuDisplays(self):
        # Arrange

        # Act
        main.start_menu()
        os.system("exit")

        # Assert
        self.assertTrue()

if __name__ == '__main__':
    unittest.main()