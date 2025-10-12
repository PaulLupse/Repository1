from pathlib import Path

english_letters = ['e', 't', 'a', 'o', 'i', 'n', 's', 'r', 'h', 'd',
                   'l', 'u', 'c', 'm' ,'f' ,'y', 'w', 'g', 'p', 'b', 'v',
                   'k', 'x', 'q', 'j', 'z']

romanian_letters = ['a', 'i' ,'e' ,'r' ,'t' ,'n' ,'u' ,'o' ,'c' ,'ă' ,'s' ,'l' ,'p',
                    'd' ,'m' ,'ș' ,'ț' ,'f' ,'v' ,'b' ,'g' ,'z' ,'h' ,'â' ,'î' ,'j',
                    'x' ,'k' ,'y' ,'w' ,'q']


resource_files_folder_path = (Path(__file__).parent/"Resources").resolve()

class AdvancedWordGuesser:
    def __init__(self):

        self.step_cnt = 0
        # lista ce retine cuvintele din dictionarul englez
        self.english_words = []
        with(open(resource_files_folder_path / "EnglishWords.txt", "r", encoding="utf-8") as words_file):
            for line in words_file:
                self.english_words.append(line.strip())

        # lista ce retine cuvintele din dictionarul romanesc
        self.romanian_words = []
        with(open(resource_files_folder_path / "RomanianWords.txt", "r", encoding="utf-8") as words_file):
            for line in words_file:
                self.romanian_words.append(line.strip().upper())

        for i in range(0, len(english_letters)):
            english_letters[i] = english_letters[i].upper()

        for i in range(0, len(romanian_letters)):
            romanian_letters[i] = romanian_letters[i].upper()

    @staticmethod
    def match(censored_word, candidate_word):

        # daca candidatul are lungime diferita, nu poate fii cuvantul cenzurat
        if len(censored_word) != len(candidate_word):
            return False

        for index, letter in enumerate(censored_word):
            # daca literele necenzurate nu sunt asemenea, nu poate fii cuvantul cenzurat
            if letter != '*' and letter != candidate_word[index]:
                return False

        return True

    def try_letter(self, letter, word):

        self.step_cnt += 1
        return word.count(letter)

    def guess_word(self, censored_word, word, language):

        if language == "romanian":
            words = self.romanian_words
            letters = romanian_letters
        elif language == "english":
            words = self.english_words
            letters = english_letters
        else: raise ValueError("Language must be romanian or english")

        matching_words = []
        for candidate_word in words:
            if self.match(censored_word, candidate_word):
                matching_words.append(candidate_word)

        word_len = len(censored_word)
        # initial, numarul de litere ce trebuiesc ghicite este egal cu numarul total de litere
        letters_to_guess = word_len

        unused_letters = [letter for letter in letters]  # memoram toate literele nefolosite din alfabet

        for letter in censored_word: # eliminam din lista toate literele deja expuse in cuvantul cenzurat
            if letter != '*':
                if letter in unused_letters:
                    unused_letters.remove(letter)
                letters_to_guess -= 1

        print("\nGuessing word: " + word)
        while letters_to_guess> 0 and len(matching_words): # cat timp nu am ghicit toate literele din cuvant
            for matching_word in matching_words:

                trial_letters = [letter for letter in matching_word]

                for letter in trial_letters:

                    print("Letters remaining: " + str(letters_to_guess))
                    if letter in unused_letters:

                        print("Letter chosen: " + letter)

                        count = self.try_letter(letter, word)  # incercam o litera din alfabet si memoram numarul de aparitii

                        unused_letters.remove(letter)  # o eliminam din lista
                        if count:  # daca litera incercata apare cel putin o data
                            letters_to_guess -= count  # si reducem numarul de litere ce trebuiesc ghicite
                        else:
                            break # daca cel putin o litera din cuvantul candidat nu se afla in cuvantul cenzurat, atunci nu are

                    if letters_to_guess == 0:
                        break

                if letters_to_guess == 0:
                    break

                matching_words.remove(matching_word)

            if letters_to_guess == 0:
                break

        # daca nu a fost ghicit cuvantul, incercam forta bruta
        unused_letters_index = 0
        while letters_to_guess> 0: # cat timp nu am ghicit toate literele din cuvant

            print("Letters remaining: " + str(letters_to_guess))
            print("Letter chosen: " + unused_letters[unused_letters_index])

            count = self.try_letter(unused_letters[unused_letters_index], word) #incercam o litera din alfabet si memoram numarul de aparitii
            if count: # daca litera incercata apare cel putin o data
                unused_letters.remove(unused_letters[unused_letters_index]) # o eliminam din lista
                letters_to_guess -= count # si reducem numarul de litere ce trebuiesc ghicite
            else: unused_letters_index += 1 # altfel, mergem mai departe

        print("Word guessed in " + str(self.step_cnt) + " steps")
        cpy_step_cnt = self.step_cnt
        self.step_cnt = 0
        return cpy_step_cnt
