import random
import json
from pathlib import Path

try:
    from ..Functionality import rest
except:
    print(__name__)

def generare_comanda(produse): # stoc este un dictionar

    nr_produse = random.randrange(1, 4)
    suma_totala = 0
    while nr_produse:

        produs, pret = random.choice(list(produse.items()))
        suma_totala += pret
        nr_produse -= 1

    suma_platita = suma_totala + random.randrange(0, 101)

    return suma_platita, suma_totala


def testare(stoc):

    produse = {}
    stoc_bancnote = {}
    for produs in stoc['produse']:
        produse[produs['nume']] = produs['pret']
    for item in stoc['bancnote']:
        stoc_bancnote[item['valoare']] = int(item['stoc'])

    while True:


        print('Stoc bancnote:', stoc_bancnote)

        suma_platita, suma_comanda = generare_comanda(produse)
        nr_bancnote, bancnote = rest.rest(stoc_bancnote, suma_platita - suma_comanda)

        print(f'Suma platita: {suma_platita}, suma comanda: {suma_comanda}.')

        if nr_bancnote is not None:
            print(f'Rest: {suma_platita - suma_comanda}', end=' ')
            if nr_bancnote:
                print(f'numar de bancnote: {nr_bancnote}', bancnote)
            else:
                print()
        else:
            print(f'Nu se poate da rest petru comanda cu suma {suma_platita} si restul {suma_platita - suma_comanda}')
            break
        print("#####")


def main():

    stoc = json.load(open(Path(__file__).parent/'stock.json', 'r'))
    testare(stoc)