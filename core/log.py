# -*- coding: utf8 -*-
import logging
from server.core.utils import Singleton


class Log(metaclass=Singleton):

    def __init__(self):
        self.logger = logging.basicConfig(level=logging.INFO,
                                          format="%(asctime)s[%(levelname)s]%(message)s",
                                          datefmt="[%d-%m-%Y][%H:%M:%S]",
                                          filename='server.log',
                                          filemode='a')
        logging.getLogger().setLevel(logging.INFO)

    def get_logger(self):
        return logging.getLogger()


if __name__ == "__main__":
    log = Log().get_logger()
    log.info("bla bla")
