import json
from pathlib import Path
from flask import request, jsonify
import numpy as np

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

def get_books():
    print(data['books'])
    return jsonify(data['books'])

def get_book_by_id(book_id):

    book_id = int(book_id)
    book_index = _get_book_index(book_id)

    if book_index is not None:
        return jsonify(data['books'][book_index]), 200
    else:
        return {"error":"Book not found"}, 404

def _validate_input(user_input):

    if type(user_input) is not dict:
        return False

    for key, value in user_input.items():
        if key not in defined_fields:
            return False

    return True

def _fetch_new_id():

    book_id = data['books'][-1]['id'] + 1
    return book_id

def add_book():

    book_data = {'id':_fetch_new_id()}
    book_data.update(request.json)

    if not _validate_input(book_data):
        return {'error': 'Bad request'}, 400

    data['books'].append(book_data)
    _write_to_json(data)

    return "created", 201

def update_book(book_id):

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
