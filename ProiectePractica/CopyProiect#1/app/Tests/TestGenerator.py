from pathlib import Path
import random

english_test_files_folder_path = (Path(__file__).parent/"TestFiles/English").resolve()
romanian_test_files_folder_path = (Path(__file__).parent/"TestFiles/Romanian").resolve()
resource_files_folder_path = (Path(__file__).parent.parent/"Resources").resolve()

class TestGenerator:
    def __init__(self):

        # lista ce retine cuvintele din dictionarul englez
        self.english_words = []
        with(open(resource_files_folder_path/"EnglishWords.txt","r",encoding="utf-8") as words_file):
            for line in words_file:
                self.english_words.append(line.strip())

        # lista ce retine cuvintele din dictionarul romanesc
        self.romanian_words = []
        with(open(resource_files_folder_path / "RomanianWords.txt", "r",encoding="utf-8") as words_file):
            for line in words_file:
                self.romanian_words.append(line.strip())

        print("Word of the day: " + random.choice(self.english_words+self.romanian_words).lower())

    # genereaza un fisier cu 100 de cuvinte pentru ghicit
    def generate_test(self, word_count, language):

        #default-ul este limba engleza
        if language == "english":
            words = self.english_words
            test_files_folder_path = english_test_files_folder_path
        else:
            test_files_folder_path = romanian_test_files_folder_path
            words = self.romanian_words

        #print(self.romanian_words)

        # numara cate fisiere de test sunt in folder
        file_cnt = 0
        for file in test_files_folder_path.iterdir():
            file_cnt += 1

        # genereaza un fisier nou
        test_file = open(test_files_folder_path/str("Test#" + str(file_cnt) + ".test"),"w",encoding="utf-8")

        # genereaza cuvintele
        for i in range(0, word_count):

            random_word = random.choice(words).lower()
            letter1 = random.choice(random_word)
            letter2 = letter1
            while letter1 == letter2:
                letter2 = random.choice(random_word)

            censored_word = ''
            for letter in random_word:
                if letter == letter1 or letter == letter2 or letter == '-':
                    censored_word += letter
                else:
                    censored_word += '#'

            test_file.write(random_word + ' ' + censored_word + '\n')



