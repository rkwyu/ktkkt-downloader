import unittest
from unittest import TestCase

from ktkkt_downloader.object import Episode
from ktkkt_downloader.scraper import KtkktStrategy, Scraper


class TestScraper(TestCase):
    def test_ktkkt_series(self):
        ktkktStrategy = KtkktStrategy()
        scraper = Scraper()
        scraper.set_strategy(ktkktStrategy)
        episodes = scraper.get_series('https://www.ktkkt.cc/movie/index8080.html')
        self.assertEqual(episodes[0].id, '8080-0-0')
        self.assertEqual(episodes[0].name, '龙珠Z粤语')
        self.assertEqual(episodes[0].episode_no, '01')
        self.assertEqual(episodes[0].url, 'https://www.ktkkt.cc/play/8080-0-0.html')

    def test_ktkkt_episode(self):
        ktkktStrategy = KtkktStrategy()
        scraper = Scraper()
        scraper.set_strategy(ktkktStrategy)
        episode = scraper.get_episode('https://www.ktkkt.cc/play/8080-0-0.html')
        self.assertEqual(episode.id, '8080-0-0')
        self.assertEqual(episode.name, '龙珠Z粤语')
        self.assertEqual(episode.episode_no, '01')
        self.assertEqual(episode.url, 'https://www.ktkkt.cc/play/8080-0-0.html')


if __name__ == '__main__':
    unittest.main()