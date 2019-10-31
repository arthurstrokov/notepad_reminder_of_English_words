import requests
import json
from service import load_data_from_json, save_data_to_json
import concurrent.futures

# https://developers.lingvolive.com/ru-ru
URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = 'MjYyZTFiNzktYTJkYS00MmRlLWJiOTMtNjc2NDJiY2I2ZDc4OjJjOTUwM2FhNGQxNjQ5MjI5NWJjMmI3MzM4OTg1OTcw'


def get_a_word_translation(key: str) -> str:
    headers_auth = {'Authorization': 'Basic ' + KEY}
    auth = requests.post(URL_AUTH, headers=headers_auth)
    if auth.status_code == 200:
        token = auth.text
        headers_translate = {
            'Authorization': 'Bearer ' + token
        }
        params = {
            'text': key,
            'srcLang': 1033,
            'dstLang': 1049
        }
        req = requests.get(
            URL_TRANSLATE, headers=headers_translate, params=params)
        res = req.json()
        try:
            value = res['Translation']['Translation']
            return value
        except TypeError:
            if res == 'Incoming request rate exceeded for 50000 chars per day pricing tier':
                return res
            else:
                return None
    else:
        print('Error!' + str(auth.status_code))


def get_duplicates(check_these, check_here) -> list:
    not_translated_words = []
    for key in check_these:
        if key in check_here:
            continue
        else:
            not_translated_words.append(key)
    return not_translated_words


if __name__ == "__main__":
    google_10000_english_keys = load_data_from_json(
        'data/google_10k_english.json')
    google_10000_english_russian_keys = load_data_from_json(
        'data/google_10k_english_russian.json')

    not_translated_words = get_duplicates(
        google_10000_english_keys, google_10000_english_russian_keys)
    print(str(len(not_translated_words)) + ' words not translated yet')

    with concurrent.futures.ProcessPoolExecutor() as executor:
        for en, ru in zip(not_translated_words, executor.map(get_a_word_translation, not_translated_words)):
            print(en, ru)
            if ru == 'Incoming request rate exceeded for 50000 chars per day pricing tier':
                break
            google_10000_english_russian_keys[en] = ru
            save_data_to_json('data/google_10k_english_russian.json',
                              google_10000_english_russian_keys)
    # https://docs.python.org/3/library/concurrent.futures.html#module-concurrent.futures

    # not_translated_words_test = ['victim']
    # translated_words_test = {}
    # for en in not_translated_words_test:
    #     ru = get_a_word_translation(en)
    #     if ru == 'Incoming request rate exceeded for 50000 chars per day pricing tier':
    #         break
    #     translated_words_test[en] = ru
    #     save_data_to_json('data/translated_words_test.json',
    #                       translated_words_test)
