# -*- coding: utf8 -*-
from server.core.protocol import Protocol
from server.command_handler import CommandHandler

from server.core.utils import Mlang


class ClientProtocol(Protocol):

    def connection_made(self, transport):
        super().connection_made(transport)

    def connection_lost(self, exc):
        super().connection_lost(exc)

    def data_received(self, data):
        super().data_received(data)
        self.parse_cmd()

    def parse_cmd(self):
        cmds = self.data.split('\00')
        self.data = cmds.pop()
        for cmd in cmds:
            data = Mlang().parse_rsp(cmd)
            self.handle_cmd(data)

    def handle_cmd(self, data):
        CommandHandler().exec_cmd(self.transport, data)

