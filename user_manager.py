# -*- coding: utf8 -*-
from core.utils import Singleton
from bean.user_bean import UserBean
from core.log import Log
import threading

log = Log().get_logger()

class UserManager(metaclass=Singleton):

    def __init__(self):
        self.__users = {}
        self.__lock = threading.Lock()

    @property
    def lock(self):
        return self.__lock

    @property
    def users(self):
        return self.__users

    def add_user(self, login, transport=None):
        self.lock.acquire()
        if not (login in self.users):
            self.users[login] = User(login, transport)
            self.lock.release()
            return 1
        else:
            self.lock.release()
            return 0

    def get_user(self, login):
        if login in self.users:
            return self.users[login]
        else:
            return

    def del_user(self, login):
        self.lock.acquire()
        if login in self.users:
            del self.users[login]
            self.lock.release()
            return 1
        else:
            self.lock.release()
            return 0

    def len_users(self):
        return len(self.users)


class DummyClient(object):
    def __init__(self):
        self.uid = -1

    def write(self, response):
        pass


class User(object):
    """ User and his properties """

    def __init__(self, login, transport=None):
        self.login = login
        self.state = None
        self.transport = transport
        log.debug("trying to get user...")
        uid = UserBean.get_user_bean(login)
        if uid is None:
            UserBean.set_user_bean(login)
            uid = UserBean.get_user_bean(login)
        log.debug("get user %i" % uid)
        self.uid = uid
