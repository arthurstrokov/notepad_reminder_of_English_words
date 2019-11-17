import json
import random


def show_random_word(file_name):
    with open(file_name, 'r', encoding='utf-8') as data_file:
        dict_data_loaded = json.load(data_file)
        en, ru = random.choice(list(dict_data_loaded.items()))
        return(en + ' ' + ru)


def load_data(file_name):
    with open(file_name, 'r', encoding='utf-8') as json_file:
        data_loaded = json.load(json_file)
    return data_loaded


def save_data(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4,
                  sort_keys=True)


if __name__ == "__main__":
    pass
