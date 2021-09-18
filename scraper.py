import base64
from bs4 import BeautifulSoup
import re
import requests

import constant
from module import Series
from module import Product


def get_series(url: str):
    patterns = [
        '^https:\/\/www\.ktkkt\.top\/movie\/index(\d+)\.html$',
        '^https:\/\/www\.ktkkt\.top\/play\/(\d+)-[\d|-]*\.html$'
    ]
    for pattern in patterns:
        result = re.search(pattern, url, re.IGNORECASE)
        if result is not None:
            url = constant.SERIES_URL.format(series_id=result.group(1))
            req = requests.get(url)
            doc = BeautifulSoup(req.content, 'html.parser')
            return Series(
                result.group(1),
                doc.select('h1.title.text-fff')[0].text
            )
    raise ValueError(url)


def get_products(url: str):
    url = constant.SERIES_URL.format(series_id=get_series(url)['id'])
    req = requests.get(url)
    doc = BeautifulSoup(req.content, 'html.parser')
    elements = doc.select('a[target="_self"][title]')
    return list(map(
        lambda e: Product(
            e.attrs['href'].split('/')[-1].replace('.html', ''),
            e.attrs['title']
        ),
        elements
    ))


def get_product(url: str):
    result = re.search(
        '^https:\/\/www\.ktkkt\.top\/play\/([\d|-]*)\.html$', url, re.IGNORECASE)
    if result is not None:
        req = requests.get(url)
        doc = BeautifulSoup(req.content, 'html.parser')
        return Product(
            result.group(1),
            doc.select('#playlist a[style="color:red"]')[0].attrs['title']
        )
    else:
        raise ValueError(url)


def get_m3u8(product_id: str):
    url = constant.EPISODE_URL.format(product_id=product_id)
    req = requests.get(url)
    encoded = req.text.split('now=base64decode("')[1].split('");')[0]
    return base64.b64decode(encoded).decode("utf-8")
