from pathlib import Path
import json

defined_fields = []
# functie pentru citirea din fisierul json
# si stabilirea campurilor definite
def _read_json():

    json_file = open(Path(__file__).parent.parent / 'Data' / 'books.json', 'r')
    data = json.load(json_file)

    if data['books']:
        for key in data['books'][0].keys():
            defined_fields.append(key)

    json_file.close()

    return data

# data == list
# functie pt scrierea in fisierul json
# de la inceputul fisierului (practic o suprascriere)
def _write_json(data):

    json_file = open(Path(__file__).parent.parent / 'Data' / 'books.json', 'w')
    json.dump({"books":data}, json_file, indent = 4)
    json_file.close()

# genereaza un id nou
def _fetch_new_id():

    books_data = _read_json()['books']
    if books_data:
        new_id = int(books_data[-1]['id']) + 1
        return new_id
    return 0

# valideaza datele unei carti
def _validate_data(book_data):

    if defined_fields:
        for key in book_data.keys():
            if key not in defined_fields: # daca cartea are campuri de date ce nu sunt prezente in campurile definite...
                return False # ...datele sunt invalide
    return True

# returneaza cartea dupa id
def get_book_by_id(book_id):

    books_data = _read_json()['books']

    for book in books_data:
        if int(book['id']) == book_id:
            return book, 200
    return 'error', 404

# returneaza toate cartile
def get_all_books():

    books_data = _read_json()['books']
    return books_data, 200

# sterge o carte, dupa id
def delete_book(book_id):

    books_data = _read_json()['books']

    for book in books_data:
        if int(book['id']) == book_id: # daca cartea e gasita
            books_data.remove(book) # o sterge din lista de carti
            _write_json(books_data) # si rescrie fisierul json
            return 'deleted', 201

    return 'error', 404

def add_book(book_data):

    print(book_data)

    books_data = _read_json()['books']

    if not _validate_data(book_data):
        print(defined_fields)
        print('error 400')
        return 'error', 400

    new_book = {"id":str(_fetch_new_id())}
    for field, value in book_data.items():
        if value == '':
            value = '-'
        new_book[field] = value
    books_data.append(new_book)

    _write_json(books_data)

    return 'created', 200

def update_book(book_data):

    books_data = _read_json()['books']
    try:
        book_id = int(book_data['id'])
    except ValueError:
        return 'ID-ul cartii trebuie sa fie valoare intreaga!', 400

    if not _validate_data(book_data):
        print(defined_fields)
        return 'Internal server error', 400

    books_data = _read_json()['books']

    book_index = None
    for index, book in enumerate(books_data):
        if int(book['id']) == book_id:
            book_index = index

    if book_index is None:
        return 'Cartea nu a fost gasita!', 404

    for field, value in book_data.items():
        books_data[book_index][field] = value

    _write_json(books_data)

    return 'updated', 200

if __name__ == '__main__':
    book_data = {"id":"3","title": "b", "author": "b", "year_published": "1010"}
    print(update_book(book_data))
