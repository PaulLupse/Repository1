import json
from pathlib import Path
from flask import request
import numpy as np
from ..utilities import ListUtilities


def _read_json():

    db = open(Path(__file__).parent.parent/'data'/'books.json', 'r')
    new_data = json.load(db)
    db.close()

    return new_data, np.array([field for field in new_data['books'][0].keys()], dtype = object)

def _write_to_json(new_data):

    json_file = open(Path(__file__).parent.parent / 'data' / 'books.json', 'w')
    # noinspection PyTypeChecker
    json.dump(new_data, json_file, indent=4)
    json_file.close()

data, defined_fields = _read_json()

def _get_book_index(book_id):

    book_id = int(book_id)
    global book_index
    book_index = None
    for index, book in enumerate(data['books']):
        if book['id'] == book_id:
            book_index = index

    return book_index

order = {'order': ['id', 'title', 'author', 'year_published', 'stock', 'price']}
def get_books():

    _read_json()
    ordered_data = ListUtilities.list_carbon_copy(data['books'])
    ordered_data.insert(0, order)
    print(data['books'])
    return ordered_data, 200

def get_book_by_id(book_id):

    _read_json()
    book_id = int(book_id)
    book_index = _get_book_index(book_id)

    if book_index is not None:
        ordered_data = ListUtilities.list_carbon_copy([data['books'][book_index]])
        ordered_data.insert(0, order)
        print(data['books'][book_index])
        return ordered_data, 200
    else:
        return {"error":"Book not found"}, 404

def _validate_input(user_input):

    if type(user_input) is not dict:
        return False

    for key, value in user_input.items():
        if key not in defined_fields:
            print(key)
            return False

    return True

def _fetch_new_id():

    book_id = data['books'][-1]['id'] + 1
    return book_id

def add_book():

    print(request.json)

    book_data = {'id':_fetch_new_id()}
    book_data.update(request.json)

    if not _validate_input(book_data):
        return {'error': 'Bad request'}, 400

    data['books'].append(book_data)
    _write_to_json(data)

    return "created", 201

def update_book(book_id):

    print(book_id)
    print(request.json)

    _read_json()
    new_data = request.json
    if not _validate_input(new_data):
        return {'error': 'Bad request'}, 400

    book_id = int(book_id)
    book_index = _get_book_index(book_id)

    if book_index is not None:
        for field in new_data.keys():
            data['books'][book_index][field] = new_data[field]
    else:
        return {'error': 'Book not found'}, 404

    _write_to_json(data)
    return "updated", 200

def delete_book(book_id):

    _read_json()
    book_id = int(book_id)
    book_index = _get_book_index(book_id)

    if book_index is not None:
        del data['books'][book_index]
        _write_to_json(data)
        return 'deleted', 200
    else:
        return {'error': 'Book not found'}, 404

if __name__ == "__main__":
    print(update_book(2))
