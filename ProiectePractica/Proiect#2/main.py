import argparse

from src.game import game

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--games", type=int, default=1)
arg_parser.add_argument("--rows", type=int, default=11)
arg_parser.add_argument("--columns", type=int, default=11)
arg_parser.add_argument("--target", type=int, default=10000)
arg_parser.add_argument("--input_predefined", type=bool, default=False)
arg_parser.add_argument("--input", type=str, default="test/DefaultTest.txt")
arg_parser.add_argument("--output", type=str, default="results/DefaultResult.csv")

def main():
    game('aaaa')

if __name__ == "__main__":
    main()