import logging


logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s-%(name)s-%(levelname)-8s: %(message)s',
)


class Logger():
    def __init__(self, logger_name:str) -> None:
        self.logger = logging.getLogger(logger_name)

    def info(self, *messages) -> None:
        for message in messages: self.logger.info(message)

    def warning(self, *messages) -> None:
        for message in messages: self.logger.warning(message)

    def error(self, *messages) -> None:
        for message in messages: self.logger.error(message)
