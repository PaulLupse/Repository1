import json

def add_product(json_file, product_name, product_cost):
    file = json.load(json_file)
    ...

def remove_product(json_file, product_name):
    ...

def increment_banknote(json_file, banknote_value, banknote_amount):
    ...

def decrement_banknote(json_file, banknote_value, decrement_amount):
    ...