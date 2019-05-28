# -*- coding: utf8 -*-
import abc
import asyncio
import socket
from core.log import Log


log = Log().get_logger()


class Protocol(asyncio.Protocol, metaclass=abc.ABCMeta):
    def __init__(self):
        self.transport = None
        self.data = ''

    @abc.abstractmethod
    def connection_made(self, transport):
        self.transport = transport
        sock = self.transport.get_extra_info('socket')
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)

    @abc.abstractmethod
    def connection_lost(self, exc):
        self.transport.close()

    @abc.abstractmethod
    def data_received(self, data):
        self.data += data.decode()
