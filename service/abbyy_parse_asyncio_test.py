import requests
import json
from typing import Dict
import asyncio
import aiohttp
import time
from service.file_handling import load_data_from_json


URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = 'YjlkMjk0YTgtZGI3NS00NGE0LWJlNDUtYjkzMDU5Mzc5YTNkOjE2ODE3ZGM4OTI3OTQ4YWE5ZTBlYmJmYTZmMmY5YjZh'


def get_token():
    headers_auth = {'Authorization': 'Basic ' + KEY}
    auth = requests.post(URL_AUTH, headers=headers_auth)
    token = auth.text
    return token


async def get_a_word_translation_from_abbyy_api(key: str, session, token) -> str:
    headers_translate = {
        'Authorization': 'Bearer ' + token
    }
    params: Dict[str, str] = {
        'text': key,
        'srcLang': '1033',
        'dstLang': '1049'
    }
    async with session.get(URL_TRANSLATE, headers=headers_translate, params=params) as req:
        res = await req.json()
        try:
            value = res['Translation']['Translation']
            print(key + ' ' + value)
            return value
        except TypeError:
            if res == 'Incoming request rate exceeded for 50000 chars per day pricing tier':
                return res
            else:
                return None
    return value


async def get_a_word_translation(not_translated_words):
    token = get_token()
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.ensure_future(get_a_word_translation_from_abbyy_api(
            word, session, token)) for word in not_translated_words]
        await asyncio.wait(tasks)


if __name__ == "__main__":

    start_time = time.time()

    not_translated_words = load_data_from_json(
        'data/not_translated_words.json')

    # asyncio.run(get_a_word_translation(not_translated_words))

    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(
        get_a_word_translation(not_translated_words))
    loop.run_until_complete(future)

    end_time = time.time()
    print(end_time - start_time)
