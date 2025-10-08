from pathlib import Path
from ..WordGuesser import WordGuesser

test_files_folder_path = (Path(__file__).parent/"TestFiles").resolve()

# obiect pentru testat algoritmul
class Tester:
    def __init__(self):
        self.word_guesser = WordGuesser()

    # itereaza prin toate fisierele de testare
    def run_tests(self):
        test_files_exist = False
        for file_path in test_files_folder_path.iterdir():
            test_files_exist = True
            if str(file_path.name).endswith(".test"):
                print("\nRunning test in test file: " + file_path.name + '\n')
                self.run_test(file_path)

        if not test_files_exist:
            print("No test file was found.")
        else:
            print("Test run complete.")

    # ruleaza teste pentru cuvintele din inauntrul fisierului de testare care are locatia file_path
    def run_test(self, file_path):
        test_file = open(file_path, 'r')
        for line in test_file:
            word_pair = line.split(' ')
            self.word_guesser.guess_word(word_pair[0], word_pair[1], "english")
