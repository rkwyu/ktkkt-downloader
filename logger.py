import logging

logging.basicConfig(level=logging.INFO)


def info(*msg):
    for m in msg:
        logging.info(m)


def warn(*msg):
    for m in msg:
        logging.warn(m)


def error(*msg):
    for m in msg:
        logging.error(m)
