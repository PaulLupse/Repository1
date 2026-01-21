from linecache import getline
from pathlib import Path
from plistlib import InvalidFileException

romanian_letters = ['a', 'i' ,'e' ,'r' ,'t' ,'n' ,'u' ,'o' ,'c' ,'ă' ,'s' ,'l' ,'p',
                    'd' ,'m' ,'ș' ,'ț' ,'f' ,'v' ,'b' ,'g' ,'z' ,'h' ,'â' ,'î' ,'j',
                    'x' ,'k' ,'y' ,'w' ,'q']

class AdvancedWordGuesser:
    def __init__(self, input_file_name, output_file_name, dict_file_name):

        self.input_file_name = input_file_name
        self.output_file_name = output_file_name

        self.step_cnt = 0
        self.tried_letters = []

        # lista ce retine cuvintele din dictionarul romanesc
        self.romanian_words = []
        self.set_words(dict_file_name)

        for i in range(0, len(romanian_letters)):
            romanian_letters[i] = romanian_letters[i].upper()

    # creeaza lista de cuvinte
    def set_words(self, dict_file_name):

        try:
            with(open(dict_file_name, "r", encoding="utf-8") as words_file):
                for line in words_file:
                    self.romanian_words.append(line.strip().upper())
        except FileNotFoundError:
            print(f"Eroare: Fișierul dicționar \"{dict_file_name}\" nu a fost găsit.")
            raise FileNotFoundError

    # verifica daca cuvantul candidat are posibilitatea de a fii cuvantul cenzurat
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

    # selecteaza toate cuvintele care a posibilitatea de a fii cuvantul cenzurat
    def select_matching_words(self, censored_word, words):

        matching_words = []
        for candidate_word in words:
            if self.match(censored_word, candidate_word):
                matching_words.append(candidate_word)
        return matching_words

    # modifica lista de cuvinte candidate
    def cull_matching_words(self, censored_word, matching_words):

        for candidate_word in matching_words:
            if not self.match(censored_word, candidate_word):
                matching_words.remove(candidate_word)
        return matching_words

    # incearca o litera, contorul de incercari este incrementat
    # aceasta functie este singurul loc in care este incrementat contorul de incercari
    # returneaza numarul de aparitii a literei incercate si cuvantul cenzurat
    def try_letter(self, letter, word, censored_word):

        self.tried_letters.append(letter) # adauga litera la lista literelor incercate
        self.step_cnt += 1
        letter_cnt = 0
        for index, let in enumerate(word):
            if word[index] == letter: # daca este gasita litera pe o pozitie
                letter_cnt+=1 # controul de aparitii e incrementat
                censored_word = censored_word[:index] + letter + censored_word[index+1::] # este dezvaluita litera in cuvantul cenzurat

        return letter_cnt, censored_word

    # functie ce ghiceste cuvantul cenzurat
    def guess_word(self, censored_word, word):

        words = self.romanian_words
        letters = romanian_letters

        matching_words = self.select_matching_words(censored_word, words)

        word_len = len(censored_word)

        # initial, numarul de litere ce trebuiesc ghicite este egal cu numarul total de litere
        letters_to_guess = word_len

        unused_letters = [letter for letter in letters]  # memoram toate literele nefolosite din alfabet

        for letter in censored_word: # eliminam din lista toate literele deja expuse in cuvantul cenzurat
            if letter != '*':
                if letter in unused_letters:
                    unused_letters.remove(letter)
                letters_to_guess -= 1

        while letters_to_guess> 0 and len(matching_words): # cat timp nu am ghicit toate literele din cuvant

            for matching_word in matching_words: # pracurgem toate cuvintele candidate

                trial_letters = [letter for letter in matching_word]

                for letter in trial_letters: # punem spre incercare literele din cuvantul candidat

                    if letter in unused_letters: # daca litera nu a fost folosita


                        count, censored_word = self.try_letter(letter, word, censored_word)  # incercam o litera

                        unused_letters.remove(letter)  # si o eliminam din lista

                        if count:  # daca litera incercata apare cel putin o data
                            matching_words = self.cull_matching_words(censored_word, matching_words) # reducem lista de candidati
                            letters_to_guess -= count  # si reducem numarul de litere ce trebuiesc ghicite
                        else:
                            break # daca cel putin o litera din cuvantul candidat nu se afla in cuvantul cenzurat,
                                  # atunci candidatul nu are posibilitatea de a fii cuvantul final

                    if letters_to_guess == 0:
                        break

                if letters_to_guess == 0:
                    break

                if matching_word in matching_words: # in cazul in care candidatul inca se afla in lista (in urma reducerii listei)
                    matching_words.remove(matching_word) # acesta este eliminat

            if letters_to_guess == 0:
                break

        # daca nu a fost ghicit cuvantul prin metoda avansata, incercam forta bruta (incercam literele in functie de frecventa acestora in limba romana)

        unused_letters_index = 0
        while letters_to_guess> 0: # cat timp nu am ghicit toate literele din cuvant

            count, censored_word = self.try_letter(unused_letters[unused_letters_index], word, censored_word) #incercam o litera din alfabet si memoram numarul de aparitii

            if count: # daca litera incercata apare cel putin o data
                unused_letters.remove(unused_letters[unused_letters_index]) # o eliminam din lista
                letters_to_guess -= count # si reducem numarul de litere ce trebuiesc ghicite
            else: unused_letters_index += 1 # altfel, mergem mai departe

        cpy_step_cnt = self.step_cnt
        cpy_tried_letters = [letter for letter in self.tried_letters]

        # resetam literele incercate si numarul de pasi
        self.tried_letters = []
        self.step_cnt = 0

        return cpy_step_cnt,censored_word,cpy_tried_letters

    # ghiceste fiecare litera din fisierul memorat
    def run_file(self):

        total_steps_cnt = 0

        try:
            input_file = open(self.input_file_name, 'r', encoding='utf-8')
        except FileNotFoundError:
            print(f"Eroare: Fișierul de intrare \"{self.input_file_name}\" nu a fost găsit.")
            raise FileNotFoundError

        # daca fisierul de iesire nu este gasit, acesta este creat
        # daca este gasit, acesta este suprascris cu noul rezultat
        output_file = open(self.output_file_name, 'w', encoding='utf-8')
        output_file.truncate()

        if not input_file.name.endswith(".csv"):
            print("Eroare: Tipul fișierului de intrare este invalid.")
            raise InvalidFileException

        index = 0
        for line in input_file:
            word_pair = line.split(',')
            if not len(word_pair) == 3:
                print("Eroare: Formatul fișierului de intrare este invalid.")
                raise InvalidFileException

            steps,found_word,tried_letters = self.guess_word(word_pair[1], word_pair[2].strip('\n'))
            total_steps_cnt += steps
            output_file.write(f"{index},{steps},{found_word},OK,{' '.join(tried_letters)}\n")
            index +=1

        output_file.write(f"Total pași efectuați: {total_steps_cnt}\n")
        output_file.write(f"Media pașilor efecțuati: {total_steps_cnt/index}")


