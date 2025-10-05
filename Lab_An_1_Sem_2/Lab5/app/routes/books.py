import json
from pathlib import Path
from flask import request, jsonify
import numpy as np
from ..utilities import ListUtilities

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

# new_data == list
# functie pt scrierea in fisierul json
# de la inceputul fisierului (practic o suprascriere)
def _write_to_json(new_data):

    json_file = open(Path(__file__).parent.parent / "data" / "books.json", "w")
    # noinspection PyTypeChecker
    new_data["field_types"] = defined_fields
    print(new_data)
    json.dump(new_data, json_file, indent=4)
    json_file.close()

# retuneaza index-ul cartii dupa id-ul acesteia
def _get_book_index(book_id, books_data):

    book_id = int(book_id)
    book_index = None
    for index, book in enumerate(books_data):
        if book["id"] == book_id:
            book_index = index

    return book_index

order = {"order": ["id", "title", "author", "year_published", "stock", "price"]}

# functie care returneaza toate cartile din baza de date
def get_books():

    books_data = _read_json()["books"]
    ordered_data = ListUtilities.list_carbon_copy(books_data)
    ordered_data.insert(0, order)
    return ordered_data, 200

# functie care returneaza o carte dupa id
def get_book_by_id(book_id):

    try:
        book_id = int(book_id)
    except ValueError:
        return {"error": "Id must be integer"}, 400

    books_data = _read_json()["books"]
    book_index = _get_book_index(book_id, books_data)

    if book_index is not None:
        ordered_data = ListUtilities.list_carbon_copy([books_data[book_index]])
        ordered_data.insert(0, order)
        return ordered_data, 200
    else:
        return {"error":"Book not found"}, 404

# valideaza datele unei carti
def _validate_data(book_data):

    for key, value in book_data.items():
        if key not in defined_fields.keys(): # daca cartea are campuri de date ce nu sunt prezente in campurile definite...
            return False, "Bad request" # ...datele sunt invalide
        else:
                try:
                    value = int(value)
                except ValueError:
                    return False, {"error":f"{key.replace('_', ' ').capitalize()} must pe number!"}

    return True, None

# returneaza un id nou
def _fetch_new_id(books_data):

    book_id = 0
    if books_data:
        book_id = books_data[-1]["id"] + 1
    return book_id

# functie care adauga o carte
def add_book():

    books_data = _read_json()["books"]

    # se genereaza un id nou pt carte
    book_data = {"id":_fetch_new_id(books_data)}
    book_data.update(request.json) # si se adauga datele acesteia

    response, msg = _validate_data(book_data)
    if not response: # daca raspunsul este fals (datele nu sunt valide) returneaza mesaju de eroare
        return jsonify({"error":msg}), 400

    # adaugam cartea la lista de carti
    books_data.append(book_data)
    _write_to_json({"books":books_data}) # si rescriem fisierul json cu noile date

    return {"info":"Created succesfully"}, 201

# functie care modifica datele unei carti cu id-ul specificat
def update_book(book_id):

    try:
        int(book_id)
    except ValueError:
        return {"error": "Id must be integer"}, 400

    new_data = request.json

    response, msg = _validate_data(new_data)
    if not response:
        print(msg)
        return jsonify({"error":msg}), 400

    books_data = _read_json()["books"]
    book_index = _get_book_index(book_id, books_data)

    if book_index is not None: # daca a fost gasita cartea
        for field in new_data.keys():
            books_data[book_index][field] = new_data[field] # ii modificam datele
    else:
        return {"error": "Book not found"}, 404

    _write_to_json({"books":books_data}) # rescriem fisierul json cu datele modificate
    return {"info":"Updated succesfully"}, 200

# functie care sterge o carte cu id-ul specificat
def delete_book(book_id):

    try:
        book_id = int(book_id)
    except ValueError:
        return {"error": "Id must be integer"}, 400

    books_data = _read_json()["books"]
    _read_json()
    book_index = _get_book_index(book_id, books_data)

    if book_index is not None: # daca a fost gasita cartea
        del books_data[book_index] # o stergem din lista
        _write_to_json({"books":books_data}) # si rescriem fisierul json
        return {"info":"Deleted succesfully"}, 200
    else: # altfel, afisam mesajul de eroare
        return {"error": "Book not found"}, 404
