meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []

while(studenti):
    print(studenti[0], "a comandat", comenzi[0])
    meniu.remove(comenzi[0])
    studenti.pop(0)
    tavi.pop(-1)
    istoric_comenzi.append(comenzi[0])
    comenzi.pop(0)

print("S-au comandat", istoric_comenzi.count("guias"), "guias,", istoric_comenzi.count("ceafa"), "ceafa,",
      istoric_comenzi.count("papanasi"), "papanasi.")

print("Mai sunt", tavi.count("tava"), "tavi")
print("Mai este ceafa:", "ceafa" in meniu)
print("Mai este papanas:", "papanasi" in meniu)
print("Mai este guias:", "guias" in meniu)

suma = 0

suma += preturi[0][1] * istoric_comenzi.count("papanasi")
suma += preturi[1][1] * istoric_comenzi.count("ceafa")
suma += preturi[2][1] * istoric_comenzi.count("guias")

print("Cantina a încasat:", suma, "lei.")
print("Produse care costă cel mult 7 lei:", [produs for produs in preturi if produs[1] <=7])
