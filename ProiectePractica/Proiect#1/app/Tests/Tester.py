from pathlib import Path
from ..WordGuesser import WordGuesser

test_files_folder_path = (Path(__file__).parent/"TestFiles").resolve()

class Tester:
    def __init__(self):
        self.word_guesser = WordGuesser()

    def run_tests(self):
        for file_path in test_files_folder_path.iterdir():
            if str(file_path.name).endswith(".test"):
                print("\nRunning test in test file: " + file_path.name + '\n')
                self.run_test(file_path)

    def run_test(self, file_path):
        test_file = open(file_path, 'r')
        for line in test_file:
            word_pair = line.split(' ')
            self.word_guesser.guess_word(word_pair[0], word_pair[1], "english")
