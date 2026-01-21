# Automatizare joc Candy Crush

<p align="justify">
Acest proiect are ca scop automatizarea jocului arhicunoscut sub numele de "Candy Crush" (c), publicat de compania King,
inițial pentru browser în Aprilie 2012, urmând apoi să fie publicat pentru iOS, Android și FireOS mai târziu în același
an, iar apoi pentru Windows în Iulie 2015, sub numele de "Candy Crush Saga" (c). Aplicația este scrisă în limbajul de
programare Python în versiunea 3.12, deși poate rula cu orice versiune de Python, mai nouă sau egală cu versiunea 3.4.
</p>

## Descriere
___

<p align="justify">
Jocul Candy Crush face parte din categoria jocurilor puzzle, mai precis, subcategoria de
jocuri "potrivire trei" ("match three" pe engleză). În aceste tipuri de jocuri este implicat un jucător și un tabel de elemente, de 
regulă bogat colorate cu scopul de a evidenția distincția dintre acestea, care, aranjate în modele specifice, determină 
distrugerea acestora și câștigul a unui număr specific de puncte. Jucătorul are opțiunea de a interschimba elemente 
adiacente ortogonal pentru crearea acestor modele, modelul de bază fiind mai mereu o linie de 3 elemente, de unde vine 
și numele subcategoriei de jocuri, "potrivește trei". La distrugerea unor elemente locul acestora este ocupat de elementele
de deasupra lor, întrucât toată coloana de elemente gravitează în jos. Locurile de deasupra, astfel ramase libere, sunt 
umplute de alte elemente, alese aleator. Jocul se termină la atingerea unui numar specific de puncte, sau în situațiile 
în care nu se mai poate efectua nici o interschimbare pentru generarea unui model.
</p>

## Cuprins
___

1. Dependențe
2. Structură
3. Utilizare 
4. Algoritm
5. Limitări


## 1. Dependențe

- python 3.4 - ...: https://www.python.org/
- numpy 2.3.4: https://numpy.org/
- colorama 0.4.6: https://pypi.org/project/colorama/

## 2. Structură
___

    Proiect_CandyCrush
    ├── src
    │    ├── game.py
    │    └── game_matrix.py
    ├── test
    │    └── DefaultTest.txt
    ├── results
    │    └── DefaultResults.csv
    ├── docs
    │    └── Presentation.pptx
    └── main.py

<p align="justify">
Dosarul principal conține modului "main.py" utilizat pentru rularea aplicației, și este locul de unde începe căutarea
fișierelor input/output. Dosarul "src" conține codul sursă al aplicației, format din modulele "game.py" și "game_matrix.py".
Dosarele "test" și "results" rețin fișiere test, respectiv fișiere rezultat ale rulării aplicației. În dosarul "docs" 
este inclusă o prezentare a proiectului.
</p>

## 3. Utilizare
___

### Fișierele de intrare

<p align="justify">
Aplicația poate să ruleze folosind fișiere de intrare de tip .txt, formatate într-un mod specific, dacă este aleasă 
această opțiune de către utilizator. Dosarul test conține un astfel fișier de intrare predefinit, "DefaultTest.txt",
asupra căruia este rulată aplicația în cazul în care nu este specificat un fișier test de către utilizator.

Fișierele de intrare trebuie să prezinte următorul format:

- Fiecare linie din fișier reprezintă o linie a matricei de joc predefinite
- Rlementele fiecărei linii sunt despărțite prin spații
- Rlementele matricei fac parte din mulțimea {0, 1, 2, 3, 4}, reprezenând culorile bomboanelor

Nerespectarea acestui format duce la generarea de erori.
</p>

### Fișierele de ieșire

<p align="justify">
Rezultatele rulării aplicației, cu sau fără un fișier de intrare sunt memoreate în fișiere de ieșire de tip .csv, 
formatate într-un mod specific. Dosarul results conține un astfel de fișier de ieșire, "DefaultResults.csv", unde vor 
fii memorate rezultatele rulării aplicației ori de câte ori utilizatorul nu precizează un fișier de ieșire la rulare.

Fișierele de ieșire au următorul format:

- Pe prima linie sunt specificate numele coloanelor. Avem, astfel, următoarele 
  coloane:
  - "game_id": Identificatorul jocului.
  - "points": Numărul de puncte acumulat de joc.
  - "reached_target": Starea de atingere a țintei.
  - "stopping_reason": Motivul opririi jocului.
  - "moves_to_target": Câte interschimbări au fost făcute până la atingerea țintei.
- Restul liniilor reprezintă datele despre jocurile rulate în cadrul aplicației.

### Rularea aplicației

Cel mai rapid mod de rulare al aplicației este rularea fișierului main.py direct din exploratorul de fișiere.

Modul avansat de rulare implică utilizarea unui emulator de terminal (de ex. Windows Powershell). Cea mai simplă astfel de rulare
o reprezintă următoarea:

    python main.py

Aceasta va avea același efect cu rularea direct din exploratorul de fișiere.

Când este folosită rularea prin terminal, utilizatorul are posibilitatea de a specifica anumiți parametrii de intrare,
prin care acesta poate manipula rularea aplicației. Următoarele argumente de rulare sunt valide:

- "--games": Numărul de jocuri pe care să le execute aplicația. Implicit 100.
- "--rows": Numărul de linii a matricelor generate de aplicație, asupra cărora vor fii rulați algoritmii. Implicit 11.
- "--columns": Numărul de coloane a matricelor. Implicit 11.
- "--target": Ținta de puncte. Implicit 10000.
- "--input_predefined": Dacă se folosește un fișier de intrare predefinit.  Implicit False.
- "--input": Calea către acel fișier de intrare predefinit.  Implicit "test/DefaultTest.txt".
- "--output": Fișierul de ieșire. Implicit "results/DefaultResult.csv".

Toate aceste argumente sunt opționale și pot fii omise individual unele față de altele. Dacă argumentul "input_predefined"
este setat la valoarea True, atunci sunt ignorate argumentele rows și columns, întrucât se folosesc dimensiunile matricei
din fișierul de intrare predefinit. Când nu se folosește un fișier de intrare predefinit, matricile de jos sunt generate
aleator de către aplicație.

Ca exemplu, dacă am dori să rulăm aplicația pentru 50 de jocuri, pe matrici de dimensiune 9x9 și până la o țintă de 
9500 de puncte, am folosi următoarea linie de comandă:

    python main.py --games 50 --rows 9 --columns 9 --target 9500

Dacă utilizatorul ar dori să ruleze aplicația pe un fișier de intrare predefinit, sub un nume ipotetic de "input_file",
și să memoreze rezultatele într-un fișier de ieșire cu un nume ipotetic de "output_file", acesta ar trebui să folosească
următoarea linie de comandă:

    python main.py --input_predefined True --input input_file.txt --output output_file.csv

</p>

## 4. Algoritm
___

<p align="justify">
Algoritmul de automatizare a jocului Candy Crush se bazează pe o strategie deterministică și de tip "greedy", deși, 
datorită reumplerii tabelului de joc cu elemente generate aleator, algoritmul devine euristic, cu 
rezultate de rulare diferite pentru aceleași tabele de intrare predefinite. O metodă de păstrare a caracterului determinist
ar fii utilizarea unui algoritm de generare a numerelor pseudo-aleatoare, dar acesta nu este cazul soluției prezentate 
în cele ce urmează.
</p>

Algoritmul recunoaște un număr mai restrâns de modele, în comparație cu jocul original:

- Linie de 3: 3 elemente (bomboane) de aceeași culoare, aranjate într-o linie verticală sau orizontală.
- Linie de 4: 4 elemente (bomboane) de aceeași culoare, aranjate într-o linie verticală sau orizontală.
- Linie de 5: 5 elemente (bomboane) de aceeași culoare, aranjate într-o linie verticală sau orizontală.
- L: Două modele de tip linie de 3 care se intersectează într-un singur capăt și sunt perpendiculare, cu toate rotațiile posibile.
- T: Un model de tip linie de 3, care se intersectează, în capăt, cu un model de tip linie de 5 în mijlocul acestuia, cu toate rotațiile posibile.

<p align="justify">
Automatizarea jocurilor individuale este implementată în clasa "Game" care se află în script-ul game.py. În script-ul main.py
este creat un nou obiect de tip Game pentru fiecare joc în parte. Algoritmii de căutare a modelelor sunt implementați
în clasa "GameMatrix" aflată în modului game_matrix.py.

În cele ce urmează vom folosii următorii termeni pentru scurtarea explicației:
</p>

### Definiții
___

- **Model**: O grupare de elemente de aceeași culoare, așezate într-un anumit fel astfel încât să formeze unul dintre cele 
  5 modele precizate mai sus.
- **Model Potențial**: O grupare de n-1 elemente de aceeași culoare, unde n este numărul de elemente necesare pentru formarea
  unui model, în așa fel încât, în urma unei posibile interschimbări, să se formeze un model. Un model potențial devine model (simplu)
  în urma găsirii unei interschimbări ce determină formarea unui model, cu elemente facând parte din modelul potențial.

- **Gravitare**: Procesul de relocare a elementelor din tabela de joc, astfel încât coloanele să pot fii împărțite în segmente
  de poziții vacante (cu valoarea 0) și poziții ocupate de elemente (cu valoarea non 0).

- **Reumplere**: Înlocuirea tuturor pozițiilor vacante cu noi elemente, generate aleator și folosind o distribuție uniformă.

- **Căutare cascadă**: Repetarea procesului de căutare a modelelor, de distrugere a elementelor din care sunt formate, de 
  de gravitare a elementelor tabelului și de reumplere a tabelei de joc, până când nu mai sunt găsite modele.
- **Swap neoficial**: Swap realizat doar pentru testarea existenței unor modele. Acestea nu se numără și pot fii revocate.
- **Swap oficial**: Swap neoficial care a produs un model dorit. Acestea se numără și nu se pot revoca, și se poate numi și
  un swap propriu-zis.

___


<p align="justify">
Algoritmul începe cu o căutare cascadă pentru a elimina modelele încă din înaintea începerii jocului. Se repetă, apoi, 
următorul proces, până ce nu se mai găsesc noi interschimbări sau este atinsă ținta de puncte:
</p>

- Se realizează o căutare a modelelor potențiale de tip linie de 5.
- Dacă nu a fost găsit un model, se realizează o căutare a modelelor potențiale de tip L.
- Dacă nu a fost găsit un model, se realizează o căutare a modelelor potențiale de tip linie de 4.
- Dacă nu a fost găsit un model, se realizează o căutare a modelelor potențiale de tip linie de 3.

<p align="justify">
Toate aceste căutări se realizează de la baza matricei și până la prima linie a matricei, folosind ca punct de ancorare
fiecare poziție de pe fiecare linie a matricei. Fiecare tip de model potențial are o modalitate de căutare diferită, 
dar căutarea modelelor de tip linie sunt similare în implementare. Căutările se opresc atunci când se găsește un model,
și se reiau de la început.
</p>

<p align="justify">
Căutările modelelor potențiale se deosebesc de căutările modelelor simple prin faptul că, în cazul căutărilor modelelor
simple, doar se distrug elemntele ce formează acele modele. La găsirea unui model potențial, se distrug elementele ce 
formează acel model, devenit model simplu, este performată o căutare cascadă și algoritmul se oprește în totalitate.

Tratarea coliziunilor modelelor și a modelelor potențiale este inclusă în caracterul de strategie greedy a algoritmului.
Sunt căutate modelele și modelele potențiale în ordinea punctelor pe care le generează (în urma eliminării acestora).
Dacă, la un moment dat, un swap crează două modele în același timp, care au elemente comune, se alege modelul
căutat la acel moment, iar datorită faptului că algoritmul se oprește în întregime când găsește un anumit model, nu există
posibilitatea ca, la un moment dat, pentru un model căutat, swap-ul să genereze atât modelul căutat cât și unul mai valoros.

</p>

## Licență
___

MIT License











    