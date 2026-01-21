from pathlib import Path
import random



class TestGenerator:
    def __init__(self, test_files_folder, default_dict_file):

        self.test_files_folder_path = Path(test_files_folder).resolve()

        # lista ce retine cuvintele din dictionarul romanesc
        self.romanian_words = []
        with(open(default_dict_file, "r",encoding="utf-8") as words_file):
            for line in words_file:
                self.romanian_words.append(line.strip().upper())


    # genereaza un fisier cu 100 de cuvinte pentru ghicit
    def generate_test(self, word_count):

        words = self.romanian_words

        # numara cate fisiere de test sunt in folder
        file_cnt = 0
        for file in self.test_files_folder_path.iterdir():
            file_cnt += 1

        # genereaza un fisier nou
        test_file = open(self.test_files_folder_path/str("Test#" + str(file_cnt) + ".csv"),"w",encoding="utf-8")

        # genereaza cuvintele
        for i in range(0, word_count):

            random_word = random.choice(words).upper()
            letter1 = random.choice(random_word)
            letter2 = letter1
            while letter1 == letter2:
                letter2 = random.choice(random_word)

            censored_word = ''
            for letter in random_word:
                if letter == letter1 or letter == letter2 or letter == '-':
                    censored_word += letter
                else:
                    censored_word += '*'

            test_file.write(str(i)+','+censored_word + ',' + random_word + '\n')





