import json
import csv
from pathlib import Path
import os
try:
    from ..Functionality import rest
except:
    print(__name__)

def main():
    for item in os.walk(Path(__file__).parent):
        if item[0][-5:-1:] == "test":
            print(f"\nIn {item[0][-5::]}... ")

            stock = json.load(open(Path(__file__).parent/f'{item[0][-5::]}'/'stock.json', 'r'))
            reader = csv.reader(open(Path(__file__).parent/f'{item[0][-5::]}'/'orders.csv'))

            banknote_stock = {}
            products = {}

            for item in stock['bancnote']:
                banknote_stock[item['valoare']] = int(item['stoc'])
            for item in stock['produse']:
                products[item['nume'].lower()] = int(item['pret'])

            for index, order in enumerate(reader):

                print(f'Comanda {index}:')

                sum_client = int(order[0])
                sum_order = 0
                for product in order[1::]:
                    sum_order += products[product.lower()]

                print('Stoc bancnote:', banknote_stock)
                nr_banknotes, banknotes = rest.rest(banknote_stock, sum_client - sum_order)

                print(f'Suma platita: {sum_client}, suma comanda: {sum_order}.')

                if nr_banknotes is not None:
                    print(f'Rest: {sum_client - sum_order}', end = ' ')
                    if nr_banknotes: print(f'numar de bancnote: {nr_banknotes}', banknotes)
                    else: print()
                else:
                    print(f'Nu se poate da rest petru comanda cu suma {sum_order} si restul {sum_client - sum_order}')
                    break