from config import RASP_YANDEX_TOKEN
from urllib.parse import quote
import requests


def get_suggests(city: str) -> list:
    encoded_city = quote(city.encode('utf-8'))
    url = f'https://suggests.rasp.yandex.net/all_suggests?format=old&part={encoded_city}'.encode('utf-8')
    result = requests.get(url)
    result.encoding = 'utf-8'
    return result.json()[1]

