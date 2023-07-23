from io import StringIO
import unittest
from unittest.mock import patch
from unittest import TestCase

from ktkkt_downloader.logger import Logger
logger = Logger(__name__)


MESSAGE = 'TEST_MESSAGE'


class TestLogger(TestCase):
    def test_print(self):
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(MESSAGE)
            self.assertEqual(fake_out.getvalue(), '{}\n'.format(MESSAGE))

    def test_info(self):
        with TestCase.assertLogs(__name__, level='INFO') as cm:
            logger.info(MESSAGE)
            self.assertEqual(cm.output, ['INFO:{}:{}'.format(__name__, MESSAGE)])

    def test_warning(self):
        with TestCase.assertLogs(__name__, level='WARN') as cm:
            logger.warning(MESSAGE)
            self.assertEqual(cm.output, ['WARNING:{}:{}'.format(__name__, MESSAGE)])

    def test_error(self):
        with TestCase.assertLogs(__name__, level='ERROR') as cm:
            logger.error(MESSAGE)
            self.assertEqual(cm.output, ['ERROR:{}:{}'.format(__name__, MESSAGE)])


if __name__ == '__main__':
    unittest.main()