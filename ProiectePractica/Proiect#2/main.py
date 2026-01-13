import argparse # pentru prelucrarea argumentelor
import numpy # pentru tablourile performante
import datetime # pentru afisarea runtime-ului jocurilor
from colorama import init # pentru text colorat in consola

from src.game import Game

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--games", type=int, default=100)
arg_parser.add_argument("--rows", type=int, default=11)
arg_parser.add_argument("--columns", type=int, default=11)
arg_parser.add_argument("--target", type=int, default=10000)
arg_parser.add_argument("--input_predefined", type=bool, default=False)
arg_parser.add_argument("--input", type=str, default="test/DefaultTest.txt")
arg_parser.add_argument("--output", type=str, default="results/DefaultResult.csv")

# functie ce citeste un fisier input, formatat astfel:
# fiecare linie reprezinta linia matricei de joc initiale,
# elementele liniilor sunt despartite prin spatii, si fac parte din multimea {0,1,2,3,4}
def read_input(input_file):

    try:
        with open(input_file, 'r') as file:

            input_matrix = []
            m = 10000
            # deoarece in matrice avem doar valori de la 0 la 4, e destul ca elementele sa fie valori intregi pe 8 biti
            for i, file_line in enumerate(file):

                line = file_line.strip(' ').strip('\n').split(' ')

                m = min(m, len(line))

                if line == ['']: # daca linia este goala, atunci se opreste citirea fisierului
                    break

                for j, element in enumerate(line):
                    try:
                        element = int(element)
                    except ValueError:
                        raise ValueError(f"Elementul '{line[j]}' de pe linia {i} și coloana {j} nu este o valoare întreagă." )
                    if element not in (0,1,2,3,4):
                        raise ValueError(f"Elementul '{element}' de pe linia {i} și coloana {j} nu face parte din mulțimea {0, 1, 2, 3, 4}.")

                input_matrix.append(line)

            n = len(input_matrix)
            # se considera dimensiunea m a matricii ca fiind dimensiunea celei mai scurte linii

            matrix = numpy.ndarray((n, m), dtype=numpy.int8)
            for i in range(0, n):
                for j in range(0, m):
                    matrix[i][j] = input_matrix[i][j]

            return n, m, matrix

    except FileNotFoundError:
        print("\033[91m{}\033[00m".format(f"Eroare: Fișierul de intrare {input_file} nu a fost gasit."))
        raise
    except ValueError as error:
        print("\033[91m{}\033[00m".format(f"Eroare la citirea fisierului {input_file}. Motiv: {error}"))
        raise
    except PermissionError:
        print("\033[91m{}\033[00m".format(f"Eroare: Nu este prermis accesul la fișierul {input_file}. Cel mai probabil o altă aplicație îl folosesște la acest moment."))
        raise

# functia care ruleaza toate jocurile dupa parametrii introdusi de utilizator
def run_games(game_number, matrix, rows, cols, target, output_file):

    print("Se rulează aplicația având configurația:")
    print(f"Linii: {rows}. Coloane: {cols}. Număr de jocuri: {game_number}. Țintă: {target}p.")
    try:
        with open(output_file, 'w', encoding="UTF-8") as out:

            # fisierul de iesire e golit
            out.truncate()
            out.writelines("game_id,points,reached_target,stopping_reason,moves_to_target\n")

            start_time = datetime.datetime.now()

            print(f"Executia jocurilor începută la: {start_time}.")

            # pentru fiecare joc se creeaza un nou obiect de tip joc, iar jocul propriu-zis trebuie sa fie rulat prin
            # metoda 'play'
            total_swaps = 0 # se retine numarul total de pasi pentru datele cu caracter statistic
            ok_status = 0
            for i in range(0, game_number):

                game = Game(i, matrix, (rows, cols))
                point_cnt, swap_cnt = game.play(target)

                total_swaps += swap_cnt

                status = "REACHED_TARGET"
                ok_status += 1
                if point_cnt < target:
                    status = "NO_MOVES"
                    ok_status -= 1

                out.writelines(f"{i},{point_cnt},{"YES" if status == "REACHED_TARGET" else "NO"},{status},{swap_cnt}\n")

            end_time = datetime.datetime.now()
            print(f"Executia jocurilor terminată la: {end_time}.")
            print(f"Runtime total: {end_time - start_time}")
            print(f"Media interschimbărilor: {total_swaps/game_number}")
            print(f"Rata de succes: {ok_status/game_number*100} %")

    except PermissionError:
        print("\033[91m{}\033[00m".format(f"Eroare: Nu este prermis accesul la fișierul {output_file}. Cel mai probabil o altă aplicație îl folosesște la acest moment."))
        raise

def main():

    init() # initializeaza consola pt coduri de culoare ansi
    try:
        arguments = arg_parser.parse_args()
        target = arguments.target
        game_number = arguments.games
        output_file = arguments.output

        # daca input-ul este predefinit, atunci sunt ignorate argumentele 'rows' si 'columns'
        if arguments.input_predefined is True:
            print(f"Fișier de intrare: {arguments.input}.")
            rows, cols, matrix = read_input(arguments.input)
            run_games(game_number, matrix, rows, cols, target, output_file)
        # altfel, este ignorat fisierul de intrare
        else:

            rows, cols = arguments.rows, arguments.columns
            run_games(game_number, None, rows, cols, target, output_file)

        print("\033[92m{}\033[00m".format(f"Aplicația a fost rulată cu succes. Rezultatele au fost memorate în fișierul: {output_file}."))
    except:
        print("\033[91m{}\033[00m".format("A apărut o eroare în timpul programului, iar rularea a fost suspendată."))
        raise

    input("Apăsați tasta 'enter' pentru a continua...")

if __name__ == "__main__":
    main()