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
                    self.clear_console()
                    print("Select language:")
                    print("0. English")
                    print("1. Romanian")

                    language = input()
                    match language:
                        case "0":
                            self.test_generator.generate_test(10, "english")
                            print("Test generation complete.")
                        case "1":
                            self.test_generator.generate_test(10, "romanian")
                            print("Test generation complete.")
                        case _:
                            print("Invalid language selected.")
                case "2":
                    self.clear_console()
                    print("Select language:")
                    print("0. English")
                    print("1. Romanian")

                    language = input()
                    match language:
                        case "0":
                            self.tester.run_tests("english")
                            print("Test run complete.")
                        case "1":
                            self.tester.run_tests("romanian")
                            print("Test run complete.")
                        case _:
                            print("Invalid language selected.")
                case _:
                    print("Invalid input.")


            input("Press enter to continue...")
            self.clear_console()
