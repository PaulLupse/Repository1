
english_letters = ['e', 't', 'a', 'o', 'i', 'n', 's', 'r', 'h', 'd',
                   'l', 'u', 'c', 'm' ,'f' ,'y', 'w', 'g', 'p', 'b', 'v',
                   'k', 'x', 'q', 'j', 'z']

romanian_letters = ['a', 'i' ,'e' ,'r' ,'t' ,'n' ,'u' ,'o' ,'c' ,'ă' ,'s' ,'l' ,'p',
                    'd' ,'m' ,'ș' ,'ț' ,'f' ,'v' ,'b' ,'g' ,'z' ,'h' ,'â' ,'î' ,'j',
                    'x' ,'k' ,'y' ,'w' ,'q']

class WordGuesser:

    def __init__(self):
        for i in range(0, len(english_letters)):
            english_letters[i] = english_letters[i].upper()

        for i in range(0, len(romanian_letters)):
            romanian_letters[i] = romanian_letters[i].upper()

    @staticmethod
    def try_letter(letter, word):
        cnt = 0
        if letter in word:
            for index, let in enumerate(word): # cautam pozitiile in care se afla litera incercata
                if let == letter:
                    cnt += 1
        return cnt

    def guess_word(self, censored_word, word, language):

        # formatul cuvantului cenzurat: caracter == "#" => caracter ascuns
        #                               caracter == [a-z] or [A-Z] => caracter present

        word_len = len(word)

        letters=[]
        if language == 'english':
            letters = english_letters

        elif language == 'romanian':
            letters = romanian_letters
        else:
            raise ValueError('Language must be english or romanian')

        # initial, numarul de litere ce trebuiesc ghicite este egal cu numarul total de litere
        letters_to_guess = word_len
        step_cnt = 0

        unused_letters = [letter for letter in letters] # memoram toate literele nefolosite din alfabet

        for letter in censored_word: # eliminam din lista toate literele deja expuse in cuvantul cenzurat
            if letter != '*':
                if letter in unused_letters:
                    unused_letters.remove(letter)
                letters_to_guess -= 1

        print("\nGuessing word: " + word)
        unused_letters_index = 0
        while letters_to_guess> 0: # cat timp nu am ghicit toate literele din cuvant

            print("Letters remaining: " + str(letters_to_guess))
            print("Letter chosen: " + unused_letters[unused_letters_index])

            count = self.try_letter(unused_letters[unused_letters_index], word) #incercam o litera din alfabet si memoram numarul de aparitii
            if count: # daca litera incercata apare cel putin o data
                unused_letters.remove(unused_letters[unused_letters_index]) # o eliminam din lista
                letters_to_guess -= count # si reducem numarul de litere ce trebuiesc ghicite
            else: unused_letters_index += 1 # altfel, mergem mai departe
            step_cnt += 1 # fiecare incercare reprezinta un pas

        print("Word guessed in: " + str(step_cnt) + " steps.\n")
        return step_cnt

