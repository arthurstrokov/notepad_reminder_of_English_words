import requests
import json
from typing import Dict
import asyncio
import aiohttp


URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = 'YjlkMjk0YTgtZGI3NS00NGE0LWJlNDUtYjkzMDU5Mzc5YTNkOjE2ODE3ZGM4OTI3OTQ4YWE5ZTBlYmJmYTZmMmY5YjZh'


async def get_a_word_translation_from_abbyy_api(key: str, session) -> str:
    headers_auth = {'Authorization': 'Basic ' + KEY}
    auth = requests.post(URL_AUTH, headers=headers_auth)    
    token = auth.text
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
        value = res['Translation']['Translation']
        print(value)
        return value     

async def get_a_word_translation(not_translated_words):
    async with aiohttp.ClientSession() as session:        
        tasks = [asyncio.ensure_future(get_a_word_translation_from_abbyy_api(word, session)) for word in not_translated_words]
        await asyncio.wait(tasks)


if __name__ == "__main__":

    not_translated_words = ['one', 'two', 'three']

    # asyncio.run(get_a_word_translation(not_translated_words)) 

    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(get_a_word_translation(not_translated_words))
    loop.run_until_complete(future)    
