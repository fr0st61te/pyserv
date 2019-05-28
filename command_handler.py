# -*- coding: utf8 -*-
from commands.login_command import login_command
from commands.error_command import error_command
from core.utils import Singleton
from concurrent.futures import ThreadPoolExecutor
from core.log import Log


log = Log().get_logger()


class CommandHandler(metaclass=Singleton):

    def __init__(self):
        self.threadpool = ThreadPoolExecutor(max_workers=5)
        self.commands = {
            0: login_command,
            99: error_command,
        }

    def exec_cmd(self, transport, data):
        try:
            self.threadpool.submit(self.commands[data['id']], transport, data)
            log.debug("add command %s into threadpool"%(str(data['id'])))
        except KeyError:
            self.threadpool.submit(self.commands[99], transport, data)
