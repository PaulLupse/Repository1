import os
from pathlib import Path
import random

test_files_folder_path = (Path(__file__).parent/"TestFiles").resolve()
resource_files_folder_path = (Path(__file__).parent.parent/"Resources").resolve()

# obiect generator de fisiere test
class TestGenerator:
    def __init__(self):

        self.english_words = [] # retinem cuvintele englezesti intr-o lista
        with(open(resource_files_folder_path/"EnglishWords.txt","r") as words_file):
            for line in words_file:
                self.english_words.append(line.strip())

        self.romanian_words = []
        with(open(resource_files_folder_path / "RomanianWords.txt", "r") as words_file):
            for line in words_file:
                self.romanian_words.append(line.strip())

        #print("Word of the day: " + random.choice(self.english_words).lower())

    # genereaza un fisier cu <word_count> de cuvinte pentru ghicit
    def generate_test(self, word_count):

        # numara cate fisiere de test sunt in folder
        file_cnt = 0
        for file in test_files_folder_path.iterdir():
            file_cnt += 1

        # genereaza al <test_file>-ulea fisier de test
        test_file = open(test_files_folder_path/str("Test#" + str(file_cnt) + ".test"),"w")

        for i in range(0, word_count):

            # alege un cuvant la nimereala
            random_word = random.choice(self.english_words).lower()

            # alege o litera din acel cuvant
            letter1 = random.choice(random_word)
            letter2 = letter1

            # alege o alta litera
            while letter1 == letter2:
                letter2 = random.choice(random_word)

            censored_word = ''
            for letter in random_word:
                if letter == letter1 or letter == letter2: # literele nu sunt 'taiate' din cuvant
                    censored_word += letter
                else:
                    censored_word += '#'

            test_file.write(random_word + ' ' + censored_word + '\n')

    @staticmethod
    def delete_test():

        last_file = ''
        for file in test_files_folder_path.iterdir(): # alege ultimul fisier test
            last_file = file

        # si il sterge
        if last_file == '':
            print("No test file was found.")
        else:
            os.remove(last_file)

        print("Deleted file " + str(last_file))


