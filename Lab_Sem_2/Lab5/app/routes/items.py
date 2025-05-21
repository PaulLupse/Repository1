import json
from pathlib import Path
from flask import request, jsonify
import numpy as np
from ..utilities import ListUtilities

defined_fields = None
def _read_json():

    db = open(Path(__file__).parent.parent/"data"/"books.json", "r")
    new_data = json.load(db)
    db.close()
    
    if new_data["books"]:
        global defined_fields
        defined_fields = np.array([field for field in new_data["books"][0].keys()], dtype = object)

    return new_data

def _write_to_json(new_data):

    json_file = open(Path(__file__).parent.parent / "data" / "books.json", "w")
    # noinspection PyTypeChecker
    json.dump(new_data, json_file, indent=4)
    json_file.close()

def _get_book_index(book_id, books_data):

    book_id = int(book_id)
    book_index = None
    for index, book in enumerate(books_data):
        if book["id"] == book_id:
            book_index = index

    return book_index

order = {"order": ["id", "title", "author", "year_published", "stock", "price"]}
def get_books():

    books_data = _read_json()["books"]
    ordered_data = ListUtilities.list_carbon_copy(books_data)
    ordered_data.insert(0, order)
    return ordered_data, 200

def get_book_by_id(book_id):

    try:
        book_id = int(book_id)
    except ValueError:
        return jsonify({"error": "Id must be integer"}), 400

    books_data = _read_json()["books"]
    book_index = _get_book_index(book_id, books_data)

    if book_index is not None:
        ordered_data = ListUtilities.list_carbon_copy([books_data[book_index]])
        ordered_data.insert(0, order)
        return ordered_data, 200
    else:
        return jsonify({"error":"Book not found"}), 404

def _validate_input(user_input):

    if type(user_input) is not dict:
        return False
    
    if defined_fields is not None:
        for key, value in user_input.items():
            if key not in defined_fields:
                return False

    return True

def _fetch_new_id(books_data):

    book_id = 0
    if books_data:
        book_id = books_data[-1]["id"] + 1
    return book_id

def add_book():

    books_data = _read_json()["books"]

    book_data = {"id":_fetch_new_id(books_data)}
    book_data.update(request.json)

    if not _validate_input(book_data):
        return jsonify({"error": "Bad request"}), 400

    books_data.append(book_data)
    _write_to_json({"books":books_data})

    return {"info":"Created succesfully"}, 201

def update_book(book_id):

    try:
        int(book_id)
    except ValueError:
        return jsonify({"error": "Id must be integer"}), 400

    books_data = _read_json()["books"]
    new_data = request.json
    if not _validate_input(new_data):
        return jsonify({"error": "Bad request"}), 400

    book_index = _get_book_index(book_id, books_data)

    if book_index is not None:
        for field in new_data.keys():
            books_data[book_index][field] = new_data[field]
    else:
        return jsonify({"error": "Book not found"}), 404

    _write_to_json({"books":books_data})
    return {"info":"Updated succesfully"}, 200

def delete_book(book_id):

    try:
        book_id = int(book_id)
    except ValueError:
        return jsonify({"error": "Id must be integer"}), 400

    books_data = _read_json()["books"]
    _read_json()
    book_index = _get_book_index(book_id, books_data)

    if book_index is not None:
        del books_data[book_index]
        _write_to_json({"books":books_data})
        return {"info":"Deleted succesfully"}, 200
    else:
        return jsonify({"error": "Book not found"}), 404
