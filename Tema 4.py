import random

cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in range(0, len(cuvant_de_ghicit))]

nr_incercari_ramase = 6
litere_incercate = set()

nr_litere_ramase = len(cuvant_de_ghicit)

while nr_litere_ramase and nr_incercari_ramase:
    print(''.join(progres))
    print(f"Numarul de incercari ramase este: {nr_incercari_ramase}")

    valid = 0
    print("Introdu litera: ")
    while not valid:
        litera = input().lower()
        if not(litera.isalpha() and len(litera) == 1):
            print("EROARE! Introdu o litera valida: ")
        elif litera in litere_incercate:
            print("EROARE! Ai introdus deja aceasta litera. Introdu alta litera: ")
        else: valid = 1
    else:
        litere_incercate.add(litera)

    pozitie_litera = cuvant_de_ghicit.find(litera)

    if(pozitie_litera == -1):
        nr_incercari_ramase -= 1
        print(f"Litera {litera} nu se afla in cuvant.")
    else:
        nr_litere_asemenea = 0
        print("Ai ghicit o litera!")
        while(pozitie_litera != -1):
            progres[pozitie_litera] = litera
            pozitie_litera = cuvant_de_ghicit.find(litera, pozitie_litera + 1)
            nr_litere_asemenea += 1

        nr_litere_ramase -= nr_litere_asemenea

if(nr_incercari_ramase == 0):
    print(f"Ai pierdut! Cuvântul era: {cuvant_de_ghicit}")
else:
    print(f"Felicitări! Ai ghicit cuvântul! ({cuvant_de_ghicit})")
