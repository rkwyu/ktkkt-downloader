import ffmpeg
import os
from pathvalidate import sanitize_filename
import traceback

import logger


def download_m3u8(m3u8: str, directory: str, filename: str):
    try:
        output = os.path.join(
            directory,
            sanitize_filename(filename)
        )
        os.makedirs(os.path.dirname(output), exist_ok=True)
        if os.path.exists(output) is False:
            stream = ffmpeg.input(m3u8)
            stream = ffmpeg.output(
                stream, output, vcodec='copy', acodec='copy')
            ffmpeg.run(stream)
            logger.info('Downloaded', m3u8, output)
        else:
            raise FileExistsError(output)
    except:
        logger.error(traceback.format_exc())
