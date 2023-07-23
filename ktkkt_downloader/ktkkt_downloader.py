from ktkkt_downloader.downloader import Downloader

from .scraper import KtkktStrategy, Scraper

from .logger import Logger
logger = Logger(__name__)


FILENAME = '{name}.E{episode_no}.mp4'


class KtkktDownloader():
    def __init__(self, dir:str) -> None:
        self.downloader = Downloader(dir)
        self.scraper = Scraper()
        self.scraper.set_strategy(KtkktStrategy())

    def download_series(self, url:str):
        episodes = self.scraper.get_series(url)
        for episode in episodes:
            if episode.m3u8 is None:
                episode.m3u8 = self.scraper.get_m3u8(episode.url)
            self.downloader.m3u8(
                episode.m3u8,
                FILENAME.format(
                    name=episode.name,
                    episode_no=episode.episode_no
                )
            )

    def download_episode(self, url:str):
        episode = self.scraper.get_episode(url)
        if episode.m3u8 is None:
            episode.m3u8 = self.scraper.get_m3u8(episode.url)
        self.downloader.m3u8(
            episode.m3u8,
            FILENAME.format(
                name=episode.name,
                episode_no=episode.episode_no
            )
        )
