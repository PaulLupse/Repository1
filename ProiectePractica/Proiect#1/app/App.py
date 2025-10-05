from .WordGuesser import WordGuesser
from .Tests.TestGenerator import TestGenerator as TestGen
from .Tests.Tester import Tester
import os

class App:
    def __init__(self, app_name):
        self.clear_console = lambda: os.system('cls')
        self.app_name = app_name
        self.tester = Tester()
        self.test_generator = TestGen()
        self.word_guesser = WordGuesser()
        print("Application \"" + app_name + "\" started.")

    def gui_loop(self):

        while True:
            print("Select an action:")
            print("0. Exit")
            print("1. Generate a test")
            print("2. Run tests")
            action = input()
            match action:
                case "0":
                    print("Bye")
                    input("Press enter to continue...")
                    break
                case "1":
                    self.test_generator.generate_test(10)
                    print("Test generation complete.")
                case "2":
                    self.tester.run_tests()
                    print("Test run complete.")
                case _:
                    print("Invalid input.")


            input("Press enter to continue...")
            self.clear_console()
