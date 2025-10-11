from pathlib import Path
from ..WordGuesser import WordGuesser

english_test_files_folder_path = (Path(__file__).parent/"TestFiles/English").resolve()
romanian_test_files_folder_path = (Path(__file__).parent/"TestFiles/Romanian").resolve()

class Tester:
    def __init__(self):
        self.word_guesser = WordGuesser()

    def run_tests(self, language):

        test_files_folder_path = english_test_files_folder_path
        if language == "romanian":
            test_files_folder_path = romanian_test_files_folder_path
        print(test_files_folder_path)

        for file_path in test_files_folder_path.iterdir():
            if str(file_path.name).endswith(".test"):
                print("\nRunning test in test file: " + file_path.name + '\n')
                self.run_test(file_path, language)

    def run_test(self, file_path, language):

        total_steps_cnt = 0
        test_file = open(file_path, 'r', encoding="utf-8")
        for line in test_file:
            word_pair = line.split(' ')
            total_steps_cnt += self.word_guesser.guess_word(word_pair[0], word_pair[1], language)

        print("\nTotal steps: " + str(total_steps_cnt))
