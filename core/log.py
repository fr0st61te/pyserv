# -*- coding: utf8 -*-
import logging
from core.utils import Singleton
from systemd.journal import JournalHandler


class Log(metaclass=Singleton):

    def __init__(self):
        logger = logging.getLogger()

        # instantiate the JournaldHandler to hook into systemd
        journald_handler = JournalHandler()
        # set a formatter to include the level name
        journald_handler.setFormatter(logging.Formatter(
            '[%(levelname)s] %(message)s'
        ))
        # add the journald handler to the current logger
        logger.addHandler(journald_handler)
        logging.getLogger().setLevel(logging.INFO)

    def get_logger(self):
        return logging.getLogger()


if __name__ == "__main__":
    log = Log().get_logger()
    log.info("bla bla")
