def carbon_copy(Dict):
    dict_copy = {}
    for key, value in Dict.items():
        dict_copy[key] = value
    return dict_copy

def remove_empty_values(Dict):
    dict_copy = {}
    for key, value in Dict.items():
        if value:
            dict_copy[key] = value
    return dict_copy