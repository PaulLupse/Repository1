from .WordGuesser import WordGuesser
from .AdvancedWordGuesser import AdvancedWordGuesser
from .Tests.TestGenerator import TestGenerator as TestGen
from .Tests.Tester import Tester
import os

class App:
    def __init__(self, app_name):
        self.clear_console = lambda: os.system('cls')
        self.app_name = app_name
        self.tester = Tester()
        self.test_generator = TestGen()
        self.word_guesser = AdvancedWordGuesser()
        print("Application \"" + app_name + "\" started.")

    def gui_loop(self):

        while True:
            print("Select an action:")
            print("1. Generate a test")
            print("2. Run tests")
            print("3. Delete test")
            print("0. Exit")
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
                            self.test_generator.generate_test(100, "english")
                            print("Test generation complete.")
                        case "1":
                            self.test_generator.generate_test(100, "romanian")
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
                        case "1":
                            self.tester.run_tests("romanian")
                        case _:
                            print("Invalid language selected.")
                case "3":
                    self.clear_console()
                    print("Select language:")
                    print("0. English")
                    print("1. Romanian")

                    language = input()
                    match language:
                        case "0":
                            self.test_generator.delete_test("english")
                        case "1":
                            self.test_generator.delete_test("romanian")
                        case _:
                            print("Invalid language selected.")
                case _:
                    print("Invalid input.")


            input("Press enter to continue...")
            self.clear_console()
