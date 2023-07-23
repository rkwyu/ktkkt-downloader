import ffmpeg
import os
from pathvalidate import sanitize_filename
import traceback

from ..logger import Logger
logger = Logger(__name__)


class Downloader:
    def __init__(self, dir:str) -> None:
        self.dir = dir
    
    def m3u8(self, m3u8:str, filename:str) -> None:
        try:
            output = os.path.join(
                self.dir,
                sanitize_filename(filename)
            )
            os.makedirs(os.path.dirname(output), exist_ok=True)
            if os.path.exists(output) is False:
                stream = ffmpeg.input(m3u8)
                stream = ffmpeg.output(stream, output, vcodec='copy', acodec='copy')
                ffmpeg.run(stream)
                logger.info('Downloaded {} -> {}'.format(m3u8, os.path.abspath(output)))
            else:
                raise FileExistsError(output)
        except:
            logger.error(traceback.format_exc())

