import random
import logging
import json
logger = logging.getLogger(__name__)


def show_random_word_from_file_json(file_name):
    with open(file_name, 'r', encoding='utf-8') as data_file:
        dict_data_loaded = json.load(data_file)
        en, ru = random.choice(list(dict_data_loaded.items()))
        return(en + ' ' + ru)


def load_data_from_json(json_file_name):
    with open(json_file_name, 'r', encoding='utf-8') as json_file:
        data_loaded = json.load(json_file)
    return data_loaded


def save_data_to_json(json_file_name, data):
    with open(json_file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4,
                  sort_keys=False)


# Understand what lies within. Понять, что находится внутри.
if __name__ == "__main__":
    # will print a message to the console
    # logger.warning(show_random_word_from_file_dict())
    # logger.info('I told you so')  # will not print anything
    pass
