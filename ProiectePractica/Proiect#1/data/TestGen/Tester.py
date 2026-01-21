from src.AdvancedWordGuesser import AdvancedWordGuesser
from data.TestGen.TestGenerator import TestGenerator as TestGen
from pathlib import Path
import os


class Tester:


    def __init__(self, test_files_folder, default_dict_file, default_output_file):

        self.default_output_file = default_output_file
        self.default_dict_file = default_dict_file
        self.test_files_folder = test_files_folder

        self.test_files_folder_path = Path(test_files_folder).resolve()

        self.clear_console = lambda: os.system('cls')
        self.clear_console()

        self.test_generator = TestGen(test_files_folder, default_dict_file)

    def gui_loop(self):

        while True:
            print("Aplicație de testare pentru algoritmul de ghicit.\nSelectați o actiune:")
            print("1. Generare fișier test")
            print("2. Rulare algoritm pentru un fișier test.")
            print("3. Ștergere fișier test.")
            print("0. Ieșire.")
            action = input()
            match action:
                case "0":
                    print("La revedere.")
                    input("Apăsați tasta 'enter' pentru a continua...")
                    self.clear_console()
                    break
                case "1":
                    self.clear_console()
                    self.test_generator.generate_test(100)
                    print("Genreare efectuată cu succes.")

                case "2":
                    self.clear_console()
                    file_to_test = self.iterate_folder(self.test_files_folder_path)
                    if file_to_test != '':
                        guesser = AdvancedWordGuesser(file_to_test, self.default_output_file, self.default_dict_file)
                        guesser.run_file()
                        print(f"Testare efectuată cu succes. Rezultatele au fost memorate în fișierul: {self.default_output_file}")

                case "3":
                    self.clear_console()

                    file_to_delete = self.iterate_folder(self.test_files_folder_path)
                    if file_to_delete != '':
                        os.remove(file_to_delete)
                        print("Fișier șters cu succes.")

                case _:
                    print("Introducere invalidă.")


            input("Apăsați tasta 'enter' pentru a continua...")
            self.clear_console()

    @staticmethod
    def iterate_folder(folder_path):

        if folder_path.iterdir():

            print("Selectați un fișier:")
            file_list = []
            for file in folder_path.iterdir():
                file_list.append(file)

            for index, file in enumerate(file_list):
                print(str(index + 1) + '. ' + str(file))
            print("0. Anulare")

            try:
                file_number = int(input())
                if file_number == 0:
                    return ''
                return file_list[file_number-1]
            except:
                print("Index de fișier invalid.")

        else:
            raise FileNotFoundError()
