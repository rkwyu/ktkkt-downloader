import base64
from bs4 import BeautifulSoup
import re
import requests

from ..object.episode import Episode
from .strategy import Strategy


EPISODE_PATTERN = '^https:\/\/www\.ktkkt\.cc\/play\/([\d|-]*)\.html$'
SERIES_PATTERN = '^https:\/\/www\.ktkkt\.cc\/movie\/index(\d+)\.html$'
SERIES_URL = 'https://www.ktkkt.cc/movie/index{series_id}.html'
# EPISODE_URL = 'https://www.ktkkt.cc/play/{episode_id}.html'
EPISODE_URL = 'https://www.ktkkt.cc{episode_href}'


class KtkktStrategy(Strategy):
    def __init__(self) -> None:
        super().__init__()

    def get_series(self, url:str) -> list:
        result = re.search(SERIES_PATTERN, url, re.IGNORECASE)
        if result is not None:
            req = requests.get(url)
            doc = BeautifulSoup(req.content, 'html.parser')
            name = doc.select_one('h1.title.text-fff').text.strip()
            elements = doc.select('a[target="_self"][title]')
            return list(map(
                lambda e: Episode(
                    e.attrs['href'].split('/')[-1].replace('.html', '').strip(),
                    name,
                    e.attrs['title'].strip(),
                    EPISODE_URL.format(episode_href=e.attrs['href']),
                    None
                ),
                elements
            ))
        else:
            raise ValueError(url)

    def get_episode(self, url:str) -> Episode:
        result = re.search(EPISODE_PATTERN, url, re.IGNORECASE)
        if result is not None:
            req = requests.get(url)
            doc = BeautifulSoup(req.content, 'html.parser')
            return Episode(
                result.group(1).strip(),
                doc.select_one('h3.title.text-fff').text.strip(),
                doc.select_one('#playlist a[style="color:red"]').attrs['title'].strip(),
                url,
                base64.b64decode(req.text.split('now=base64decode("')[1].split('");')[0]).decode("utf-8")
            )
        else:
            raise ValueError(url)

    def get_m3u8(self, url:str) -> str:
        req = requests.get(url)
        encoded = req.text.split('now=base64decode("')[1].split('");')[0]
        return base64.b64decode(encoded).decode("utf-8")


