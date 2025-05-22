import csv
import random
import time
from datetime import datetime

class persoana():
    def __init__(self, cnp, nume):
        self.cnp = cnp
        self.nume = nume

# modificat populatia din index #22 pt a rezulta exact 1000000 de cnp-uri in urma calculelor
repartitie = {40: 1716961,
                  22: 761250,
                  29: 695117,
                  12: 679141,
                  13: 655997,
                  35: 650533,
                  33: 642551,
                  4: 601387,
                  16: 599442,
                  3: 569932,
                  5: 551297,
                  8: 546615,
                  23: 542686,
                  26: 518193,
                  17: 496892,
                  15: 479404,
                  27: 454203,
                  24: 452475,
                  2: 410143,
                  10: 404979,
                  7: 392821,
                  32: 388325,
                  28: 383280,
                  37: 374700,
                  20: 361657,
                  39: 341861,
                  38: 335312,
                  30: 330668,
                  1: 325941,
                  34: 323544,
                  18: 314684,
                  6: 295988,
                  19: 291950,
                  51: 283458,
                  9: 281452,
                  52: 262066,
                  21: 250816,
                  11: 246588,
                  25: 234339,
                  31: 212224,
                  14: 200042,
                  36: 193355,
                  }
#folosind date de la recenzamantul din 2022

nume_f = ('Ada','Adela','Adelaida','Adelina','Adina','Adriana','Adnana','Agata','Agafia','Aglaia',
'Agripina','Aida','Ala','Alberta','Albertina','Alexandra','Alexandrina','Alexia','Alice','Alida',
'Alina','Alis','Alma','Amalia','Amanda','Amelia','Ana','Anabela','Anaida','Anamaria',
'Anastasia','Anca','Ancuța','Anda','Andra','Andrada','Andreea','Anemona','Aneta','Angela',
'Angelica','Anghelina','Anica','Anișoara','Antoaneta','Antonela','Antonia','Antonina','Anuța','Ariadna',
'Ariana','Arina','Aristița','Arghira','Arlette','Artemisa','Artemiza','Astrid','Atena','Augusta',
'Augustina','Aura','Aurelia','Aureliana','Aurica','Aurora','Axenia','Beatrice','Betina','Bianca',
'Blanduzia','Bogdana','Brândușa','Brigitta','Camelia','Carina','Carla','Carmen','Carmina','Carol',
'Carolina','Casandra','Casiana','Caterina','Catinca','Catrina','Catrinel','Cătălina','Cecilia','Cella',
'Celia','Cerasela','Cezara','Chira','Chirița','Cipriana','Clara','Clarisa','Claudia','Clementina',
'Cleopatra','Clotilda','Codrina','Codruța','Constanța','Constantina','Consuela','Coralia','Corina','Cornelia',
'Cosmina','Crenguța','Crina','Cristina','Daciana','Dafina','Daiana','Dalia','Dana','Daniela',
'Daria','Dariana','Delia','Demetra','Denisa','Despina','Diana','Dida','Didina','Dimitrina',
'Dina','Dochia','Doina','Domnica','Dora','Doriana','Dorina','Dorli','Draga','Dumbrăvița',
'Dumitra','Dumitrana','Dumitrița','Ecaterina','Eftimia','Elena','Eleonora','Eliana','Elisabeta','Elisaveta',
'Elisa','Eliza','Elodia','Elpis','Elvira','Emanuela','Emilia','Erica','Estera','Eufrosina',
'Eugenia','Eusebia','Eva','Evanghelina','Evdochia','Evelina','Fabia','Fabiana','Fausta','Felicia',
'Fenareta','Filofteia','Filomela','Fiona','Fivi','Flavia','Floare','Floarea','Flora','Florența',
'Florentina','Floriana','Florica','Florina','Francesca','Frusina','Gabriela','Geanina','Gențiana','Georgeta',
'Georgia','Georgiana','Geta','Gherghina','Gianina','Gina','Giorgiana','Gizela','Gloria','Glorița',
'Grațiana','Grațiela','Haricleea','Harieta','Henrieta','Heracleea','Hermiona','Hortensia','Iasmina','Ica',
'Ilaria','Ileana','Ilinca','Ilona','Ina','Ioana','Ioanina','Iolanda','Ionela','Ionelia',
'Ionuța','Iosefina','Iridenta','Irina','Iris','Irma','Isabela','Isaura','Iudita','Iulia',
'Iuliana','Iustina','Ivana','Ivona','Izabela','Izaura','Jana','Janeta','Janina',
'Jasmina','Jeana','Jeny','Joița','Josefina','Julia','Julieta','Laurita','Laura','Laurenția',
'Lavinia','Lăcrămioara','Leana','Lelia','Leny','Leontina','Leopoldina','Letiția','Lenuța','Lia',
'Liana','Lidia','Ligia','Lili','Liliana','Lioara','Liuba','Livia','Loredana','Lorelei',
'Lorena','Luana','Lucia','Luciana','Lucreția','Ludmila','Ludovica','Luiza','Luminița','Magdalena',
'Maia','Malvina','Manuela','Mara','Marcela','Marcheta','Marga','Margareta','Maria','Mariana',
'Maricica','Marieta','Marilena','Marina','Marinela','Marioara','Marta','Martina','Marusia','Matilda',
'Mădălina','Mălina','Mărioara','Măriuca','Melania','Melina','Melinda','Melisa','Mia','Mihaela',
'Mila','Milena','Milița','Minodora','Mioara','Mirabela','Miranda','Mirela','Mirona','Miuța',
'Miruna','Mona','Monalisa','Monica','Nadia','Naomi','Nadejda','Narcisa','Natalia','Natașa',
'Nectaria','Nelly','Nicoleta','Niculina','Nidia','Nina','Noemi','Nora','Norica',
'Oana','Octavia','Octaviana','Ofelia','Olga','Olimpia','Olivia','Ortansa','Otilia','Ozana',
'Pamela','Paraschiva','Patricia','Paula','Paulica','Paulina','Pelaghia','Petria','Petrina',
'Petronela','Petruța','Pompilia','Profira','Pulcheria','Rada','Rafila','Raluca','Ramona',
'Rebeca','Reghina','Renata','Rica','Rita','Roberta','Robertina','Rodica','Romana','Romanița',
'Romina','Roxana','Roxelana','Roza','Rozalia','Ruxanda','Ruxandra','Sabina','Sabrina','Safina',
'Safta','Salomea','Sanda','Sandra','Sarmisa','Sarmiza','Saveta','Savina','Săndica', 'Sânziana',
'Selina','Semenica','Smeralda','Serafina','Severina','Sidonia','Silvana','Silvia','Silviana','Simina',
'Simona','Smaranda','Sodica','Sofia','Sofica','Sonia','Sorana','Sorina','Speranța','Stana',
'Stanca','Stela','Steliana','Steluța','Susana','Suzana','Svetlana','Ștefana','Ștefania','Tamara',
'Tania','Tatiana','Teea','Teodora','Teodosia','Teona','Teresa','Tereza','Tiberia','Timea',
'Tinca','Tincuța','Tudora','Tudorica','Tudorița','Tudosia','Valentina','Valeria','Vanesa','Vanda',
'Varvara','Vasilica','Vasilichia','Venera','Venețiana','Vera','Veronica','Veta','Vicenția','Victoria',
'Violeta','Viorela','Viorica','Virginia','Viviana','Vlădelina','Voichița','Xenia','Zamfira','Zaraza',
'Zenaida','Zenobia','Zenovia','Zina','Zita','Zoe')

nume_b = ('Abel','Achim','Adam','Adelin','Adi','Adonis','Adrian','Agnos','Albert','Aleodor',
'Alex','Alexandru','Alexe','Alin','Alistar','Amedeu','Amza','Anatol','Anatolie','Andrei',
'Andrian','Angel','Anghel','Antim','Anton','Antonie','Antoniu','Arcadian','Arian','Aristide',
'Aristotel','Arsenie','Atanasio','Augustin','Aurel','Aurelian','Aurică','Avram','Axinte','Barbu',
'Bartolomeu','Basarab','Bănel','Bebe','Beniamin','Benone','Bernard','Bogdan','Bonifaciu','Brăduț',
'Bucur','Caius','Calistrat','Camil','Cantemir','Carol','Casian','Cazimir','Călin','Cătălin',
'Cecil','Cedrin','Cezar','Chiril','Ciprian','Claudiu','Codin','Codrin','Codruț','Conrad',
'Constantin','Cornel','Corneliu','Corvin','Cosmin','Costache','Costică','Costel','Costin','Crin',
'Cristea','Cristian','Christian','Cristinel','Cristobal','Cristofor','Dacian','Damian','Dan','Daniel',
'Darius','David','Decebal','Dimitrie','Denis','Dinu','Dionisie','Dominic','Dorel','Dorian',
'Dorin','Dorinel','Doru','Dragomir','Dragoș','Ducu','Dumitru','Edgar','Edmond','Eduard',
'Eftimie','Emanoil','Emanuel','Emanuil','Emil','Emilian','Eracle','Eremia','Eric','Ernest',
'Eudoxiu','Eufrațiu','Eugen','Eusebiu','Eustațiu','Fabian','Faust','Felix','Filip','Fiodor',
'Flaviu','Florea','Florentin','Florian','Florin','Francisc','Gabriel','Gelu','George','Georgel',
'Georgian','Ghenadie','Gheorghe','Gheorghiță','Gherasim','Ghiță','Gică','Gicu','Giorgian','Grațian',
'Gregorian','Grigoraș','Grigore','Gruia','Haralamb','Haralambie','Horațiu','Horea','Horia','Horică',
'Huberțiu','Iacob','Iacov','Iancu','Ianis','Ieremia','Igor','Ilarie','Ilarion','Ilie',
'Iliuță','Inocențiu','Inochentie','Ioan','Ion','Ionel','Ionică','Ioniță','Ionuț','Iorgu',
'Iosif','Irinel','Isidor','Iulian','Iuliu','Iurie','Iustin','Iustinian','Ivan','Jan',
'Jean','Jenel','Ladislau','Lascăr','Laurențiu','Laurian','Lazăr','Leon','Leonard','Leonid',
'Leonidas','Leontin','Leordean','Lică','Liviu','Lorin','Luca','Lucențiu','Lucian','Lucrețiu',
'Ludovic','Manole','Marcel','Marcu','Marian','Marin','Marinel','Marius','Martin','Matei',
'Mauriciu','Maxim','Maximilian','Mădălin','Mărin','Metodiu','Mihai','Mihail','Mihăiță','Mihnea',
'Mina','Mircea','Miron','Mitică','Mitrofan','Mitruț','Modest','Moise','Mugur','Mugurel',
'Nae','Narcis','Nechifor','Nectarie','Nelu','Nestor','Nichifor','Nicoară','Nicodim','Nicolae',
'Nicolaie','Nicu','Niculiță','Nicușor','Nicuță','Norbert','Noris','Norman','Octav','Octavian',
'Octaviu','Olimpian','Olimpiu','Oliver','Oliviu','Osvald','Ovidiu','Pamfil','Panagachie','Panait',
'Pantelimon','Paul','Pavel','Pătru','Petre','Petrică','Petrișor','Petru','Petruț','Pintiliu',
'Pleșu','Pompiliu','Profiriu','Radu','Rafael','Rareș','Raul','Răducu','Răzvan','Relu',
'Remus','Robert','Romeo','Romi','Romică','Romulus','Sabin','Sandu','Sava','Sebastian',
'Septimiu','Sergiu','Sever','Severin','Silvian','Silviu','Simi','Simion','Sinică','Sorin',
'Stan','Stancu','Stanislav','Stelian','Șerban','Ștefan','Tadeu','Teodor','Teofil','Teohari',
'Theodor','Tiberiu','Timotei','Titus','Todor','Toma','Traian','Trandafir','Tudor','Valentin',
'Valer','Valeriu','Valter','Vasile','Vasilică','Veaceslav','Veniamin','Vicențiu','Victor','Vincențiu',
'Viorel','Visarion','Virgil','Vitalie','Vitold','Vlad','Vladimir','Vlaicu','Voicu','Zamfir',
'Zeno','Zenobie','Zaharia')

nume_familie = ('Popa','Popescu','Pop','Radu','Ionescu','Dumitru','Stoica','Stan','Gheorghe','Rusu',
'Munteanu','Matei','Constantin','Șerban','Marin','Mihai','Ștefan','Lazăr','Moldovan','Vasile',
'Toma','Ciobanu','Florea','Ilie','Stanciu','Oprea','Tudor','Dumitrescu','Dinu','Cristea',
'Andrei','Ionița','Anghel','Mureșan','Neagu','Barbu','Sandu','Ion','Ungureanu','Dragomir',
'Vlad','Georgescu','Constantinescu','Nagy','Crăciun','Cojocaru','Mocanu','Tănase','Iordache','Enache',
'Grigore','Petre','Voicu','Lupu','Balan','Dobre','Nicolae','Badea','Coman','Ivan',
'Roman','Szabo','Rădulescu','Lungu','Iancu','Ene','Manea','Preda','David','Bucur',
'Mărinescu','Stoian','Nistor','Iacob','Pavel','Filip','Avram','Drăgan','Suciu','Olteanu',
'Petrescu','Rus','Simion','Costea','Marcu','Crișan','Luca','Roșu','Nita','Kovacs',
'Diaconu','Rotaru','Bogdan','Muntean','Nedelcu','Dan','Crețu','Călin','Zaharia','Stănescu',
'Costache','Popovici','Stancu','Baciu','Alexandru','Ștefănescu','Ghița','Albu','Teodorescu','Neacșu',
'Moraru','Păun','Anton','Roșca','Paraschiv','Toader','Nica','Drăghici','Nitu','Pascu',
'Ardelean','Olaru','Dima','Zamfir','Năstase','Varga','Damian','Mihalache','Dinca','Dumitrache',
'Sava','Moise','Chiriac','Mihăilă','Miron','Apostol','Petcu','Niculescu','Sîrbu','Bratu',
'Istrate','Iliescu','Micu','Vasilescu','Oancea','Fărcaș','Chirilă','Kiss','Croitoru','Florescu',
'Găvrilă','Gheorghiu','Soare','Manole','Savu','Vișan','Dumitrașcu','Stroe','Ursu','Tămaș',
'Musat','Marian','Balint','Simon','Molnar','Niculae','Patrașcu','Pană','Ignat','Toth',
'Cosma','Tudorache','Grecu','Dascălu','Grosu','Chiriță','Cozma','Oltean','Mihailescu','Morar',
'Moldoveanu','Sima','Panait','Voinea','Ciocan','Irimia','Manolache','Necula','Pîrvu','Adam',
'Burlacu','Danciu','Szekely','Turcu','Dănilă','Grigoraș','Sabău','Tudose','Marginean','Nicolescu',
'Cazacu','Alexe','Szasz','Aldea','Maxim','Negru','Gabor','Diaconescu','Mihalcea','Trandafir',
'Duta','Costin','Cucu','Militaru','Dogaru','Mircea','Vasiliu','Macovei','Chis','Dobrescu',
'Gherman','Tomescu','Negrea','Negoiță','Păduraru','Bota','Groza','Gal','Alexandrescu','Catană',
'Grigorescu','Ișpaș','Nicoară','Blaga','Bejan','Fodor','Neagoe','Drăgoi','Banu','Pintilie',
'Pintea','Văduva','Mateescu','Cristescu','Mirea','Trif','Sârbu','Pașca','Puiu','Iorga',
'Tătaru','Moga','Nechita','Bodea','Solomon','Barbulescu','Trifan','Olariu','Prodan','Man',
'Șandor','Vintilă','Antal','Cornea','Frătilaă','Martin','Ichim','Gheorghița','Giurgiu','Iosif',
'Neamțu','Peter','Vereș','Banica','Nemeș','Bunea','Achim','Staicu','Dumitriu','Boboc',
'Botezatu','Maftei','Petrea','Ganea','Rădoi','Parvu','Simionescu','Opriș','Covaci','Ivașcu',
'Mazilu','Milea','Chivu','Biro','Horvath','Miu','Alexa','Ardeleanu','Buda','Szilagyi','Matei',
'Batin','Podariu','Hotea','Lupșe','Zaha','Berindan')

cnpuri = []
hash_table = []

def calc_nr_persoane(populatie):
    return (1000000 * populatie) // 19053815

def repartizeaza_pe_varste(populatie):
    c1 = (17 * populatie)//100 #persoane intre 0-14 ani
    c2 = (64 * populatie)//100 #persoane intre 15-64 ani
    c3 = (19 * populatie)//100 #persoane peste 64 ani
    c2 = c2 + populatie - (c1 + c2 + c3)
    return c1, c2, c3

def generare_data(an1, an2): # an2 > an1
    ultima_zi = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    an_curent = time.localtime().tm_year
    an = random.randint(an_curent - an2, an_curent - an1)
    global data
    if an == an_curent:
        luna_curenta = time.localtime().tm_mon
        zi_curenta = time.localtime().tm_mday

        luna = random.randint(1, luna_curenta)
        zi = random.randint(1, zi_curenta)
    else:
        luna = random.randint(1, 12)
        zi = random.randint(1, ultima_zi[luna - 1] + ((luna == 2) and ( (an % 4 == 0 and an % 100 != 0) or an % 400 == 0 ) ) ) #daca anul este bisect si luna este februarie, ziua nasterii poate fii 29
    data = an * 10000 + luna * 100 + zi
    return data

def cifra_de_control(cnp):
    constanta = 279146358279
    cp_constanta = constanta
    cp_cnp = cnp
    s = 0
    while cp_cnp:
        s += (cp_cnp % 10) * (cp_constanta % 10)
        cp_cnp //= 10
        cp_constanta //= 10

    if s % 11 < 10:
        return s % 11
    else: return 1

def generare_cnp(an1, an2, index, sex):
    data = generare_data(an1, an2)
    global s
    if sex == 'm':
        if data // 10000 > 2000:
            s = 5
        else: s = 1
    else:
        if data // 10000 > 2000:
            s = 6
        else:
            s = 2

    data = data % 1000000
    cnp = s * 100000000000 + data * 100000 + index * 1000 + random.randint(0, 999)
    c = cifra_de_control(cnp)
    cnp = cnp * 10 + c

    cnpuri.append(cnp)
    return cnp

def creare_persoane():
    print("Creearea persoanelor inceputa la: ", datetime.now().time())

    registru = open('registru.csv', 'w', encoding='utf-8', newline='')

    writer = csv.writer(registru)

    global cnpuri

    for index, populatie in repartitie.items(): # pentru fiecare judeti generam cnp-uri in kimita populatiei
        nr_cnp_judet = calc_nr_persoane(populatie)
        c1, c2, c3 = repartizeaza_pe_varste(nr_cnp_judet)

        #persoane intre 0-14 ani
        for i in range(0, c1//2): #persoane de sex masculin
            writer.writerow([str(generare_cnp(0, 14, index, 'm')) , generare_nume('m')])

        for i in range(c1//2, c1): #persoane de sex feminin
            writer.writerow([str(generare_cnp(0, 14, index, 'f')) , generare_nume('f')])

        #persoane intre 15-64 ani

        for i in range(0, c2//2): #persoane de sex masculin
            writer.writerow([str(generare_cnp(15, 64, index, 'm')) , generare_nume('m')])

        for i in range(c2//2, c2): #persoane de sex feminin
            writer.writerow([str(generare_cnp(15, 64, index, 'f')) , generare_nume('f')])

        #persoane peste 64 ani

        for i in range(0, c3//2): #persoane de sex masculin
            writer.writerow([str(generare_cnp(64, 99, index, 'm')) , generare_nume('m')])

        for i in range(c3//2, c3): #persoane de sex feminin
            writer.writerow([str(generare_cnp(64, 99, index, 'f')) , generare_nume('f')])

    registru.close()
    print("Creearea persoanelor terminata la: ", datetime.now().time())
    return cnpuri

def generare_nume(sex):
    if sex == 'm':
        return random.choice(nume_b) + ' ' + random.choice(nume_familie)
    else: return random.choice(nume_f) + ' ' + random.choice(nume_familie)

def sum_dig(nr):
    rez = 0
    cpnr = nr
    while(cpnr > 0):
        rez += cpnr % 10
        cpnr //= 10
    return rez

def hash(cnp):
    cnp = int(cnp)
    s3 = sum_dig(cnp % 10000)
    s2 = sum_dig((cnp // 10000)) % 10000
    s1 = sum_dig(cnp // 100000000)

    index = (s1 + s2*97 + s3*9409) % 997

    return index

def hash2(cnp):
    cnp = int(cnp)
    s4 = sum_dig(cnp % 1000)
    s3 = sum_dig((cnp // 1000)) % 1000
    s2 = sum_dig(cnp // 1000000) % 1000
    s1 = sum_dig(cnp // 1000000000)

    index = (s1 + s2 * 41 + s3 * 1681 + s4 * 68921) % 997

    return index

def hash3(cnp):
    cnp = int(cnp)

    index = 0
    p = 0
    cpcnp = cnp
    while cpcnp > 10:
        index = (index + ((cpcnp % 10) * (111111 ** p)) % (1e9 + 7)) % (1e9 + 7)
        cpcnp //= 10
        p += 1

    return int((index + cpcnp) % 1000)

def disperseaza():
    print('Hashing inceput la: ', datetime.now().time())
    hash_table.clear()  # initializam un hash table cu 997 linii
    for i in range(0, 1000):
        linie = []
        hash_table.append(linie)

    registru = open('registru.csv', 'r', encoding='utf-8')

    for linie in registru:
        Persoana = persoana(int(linie[0:13:]), linie[14:len(linie)])
        Hash = hash3(Persoana.cnp)
        hash_table[Hash].append(Persoana)

    registru.close()
    print('Hashing terminat la: ', datetime.now().time())

def cauta_persoana(cnp):
    Hash = hash3(cnp)
    nr_pasi = 0

    for i in range(0, len(hash_table[Hash])):
        nr_pasi += 1
        if hash_table[Hash][i].cnp == cnp:
            return hash_table[Hash][i].nume, nr_pasi

    return "Persoana nu a fost gasita!", nr_pasi

def selecteaza_aleator(nr_persoane):
    lista = []
    cnp = random.sample(cnpuri, nr_persoane)
    for cnp_aleator in cnp:
        print(cnp_aleator)
        nume, nr_pasi = cauta_persoana(cnp_aleator)
        lista.append([nume.strip(), cnp_aleator, nr_pasi])
        print(f"Persoana căutată: {nume.strip()}. Pași efectuați: {nr_pasi}")
    return lista


if __name__ == '__main__':
    creare_persoane()

    disperseaza()

    print(hash3(1234567890123))

    maxim = 0
    for list in hash_table:
        maxim = max(maxim, len(list))

    print(maxim)