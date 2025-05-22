from pathlib import Path
import json

defined_fields = {}
# functie pentru citirea din fisierul json
# si stabilirea campurilor definite
def _read_json():

    json_file = open(Path(__file__).parent.parent / 'Data' / 'books.json', 'r')
    data = json.load(json_file)

    for key, value in data['field_types'].items():
        defined_fields[key] = value

    json_file.close()

    return data

# data == list
# functie pt scrierea in fisierul json
# de la inceputul fisierului (practic o suprascriere)
def _write_json(data):

    json_file = open(Path(__file__).parent.parent / 'Data' / 'books.json', 'w')
    json.dump({"books":data}, json_file, indent = 4)
    json_file.close()

# genereaza un id nou, dupa ultimul id gasit in tabela
def _fetch_new_id():

    # citeste fisierul json
    books_data = _read_json()['books']
    if books_data:
        new_id = int(books_data[-1]['id']) + 1
        return new_id
    return 0

# valideaza datele unei carti
def _validate_data(book_data):

    if defined_fields:
        for key, value in book_data.items():
            if key not in defined_fields.keys(): # daca cartea are campuri de date ce nu sunt prezente in campurile definite...
                return False, "Bad request" # ...datele sunt invalide
            else:
                if defined_fields[key] == 'int':
                    try:
                        value = int(value)
                    except ValueError:
                        return False, f"{key.replace('_', ' ').capitalize()} must pe number!"

    return True, None

# returneaza cartea dupa id, daca este gasita, altfel returneaza eroare
'''def get_book_by_id(book_id):

    # citeste fisierul json
    books_data = _read_json()['books']

    for book in books_data:
        if int(book['id']) == book_id:
            return book, 200
    return 'error', 404'''

# returneaza toate cartile
def get_all_books():

    # citeste fisierul json
    books_data = _read_json()['books']

    return books_data, defined_fields, 200

# sterge o carte dupa id, daca este gasita, altfel returneaza eroare
def delete_book(book_id):

    # daca id-ul nu este valoare intreaga
    try:
        book_id = int(book_id)
    except ValueError: # returneaza eroare
        return 'Book id must be a number!', 400

    # citeste fisierul json
    books_data = _read_json()['books']

    for book in books_data:
        if int(book['id']) == book_id: # daca cartea e gasita
            books_data.remove(book) # o sterge din lista de carti
            _write_json(books_data) # si rescrie fisierul json
            return 'deleted', 201

    return 'error', 404

# adauga o carte
def add_book(book_data):

    print(book_data)

    # citeste fisierul json
    books_data = _read_json()['books']

    response, msg = _validate_data(book_data)
    if not response:
        return msg, 400

    # se atribuie un nou id la cartea noua
    new_book = {"id":str(_fetch_new_id())}

    for field, value in book_data.items():
        if value == '': # fiecare camp nul este inlocuit cu caracterul -
            value = '-'
        new_book[field] = value
    books_data.append(new_book)

    # rescrie fisierul json cu datele modificate
    _write_json(books_data)

    return 'created', 200

def update_book(book_data):

    try: # daca id-ul nu este valoare intreaga
        book_id = int(book_data['id'])
    except ValueError:
        return 'ID-ul cartii trebuie sa fie valoare intreaga!', 400

    response, msg = _validate_data(book_data)
    if not response:
        return msg, 400

    books_data = _read_json()['books']

    # cauta locul din lista de carti unde se afla cartea cu id-ul specificat
    book_index = None
    for index, book in enumerate(books_data):
        if int(book['id']) == book_id:
            book_index = index

    # daca nu e gasita, returneaza eroare
    if book_index is None:
        return 'Cartea nu a fost gasita!', 404

    # fiecare camp din book_data, care nu este nul, inlocuieste campul curent al cartii
    for field, value in book_data.items():
        if value != '':
            books_data[book_index][field] = value

    # rescrie fisierul json cu datele modificate
    _write_json(books_data)

    return 'updated', 200

if __name__ == '__main__':
    book_data = {"id":"3","title": "b", "author": "b", "year_published": "1010"}
    print(update_book(book_data))
