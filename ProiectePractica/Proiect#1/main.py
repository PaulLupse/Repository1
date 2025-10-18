from data.TestGen.Tester import Tester
import argparse
from src.AdvancedWordGuesser import AdvancedWordGuesser
import os

default_input_file = "data/TestFiles/DefaultTest.csv"
default_output_file = "results/DefaultResults.csv"
default_dict_file = "data/RomanianWords.txt"
test_files_folder = "data/TestFiles"

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--mode", type=str,default="test") # precizeaza modul de rulare
arg_parser.add_argument("--input", type=str,default=default_input_file) # precizeaza fisierul de input
arg_parser.add_argument("--output", type=str,default=default_output_file) # precizeaza fisierul de output
arg_parser.add_argument("--dict", type=str, default=default_dict_file) # precizeaza fisierul folosit pe post de dictionar/lista de cuvinte

def main():

    args = arg_parser.parse_args()
    try:
        if args.mode == "test":

            application = Tester(test_files_folder, default_dict_file, default_output_file)
            application.gui_loop()

        else:

            input_file = args.input
            output_file = args.output
            word_list_file = args.dict

            guesser = AdvancedWordGuesser(input_file, output_file, word_list_file)
            guesser.run_file()

            print("Aplicația a fost rulată cu succes.")
    except:
        print("Aplicația a întâlnit o eroare și rularea a fost suspendată.")

    return 0

if __name__ == "__main__":
    main()