# -*- coding: utf8 -*-
import hashlib
from user_manager import UserManager
from core.utils import Mlang
from core.log import Log

log = Log().get_logger()


def login_command(transport, data):
    if transport is None:
        return
    else:
        login = data['login']
        _id = int(data['id'])
        usermanager = UserManager()
        user = usermanager.get_user(login)
        if not user:
            usermanager.add_user(login)
            user = usermanager.get_user(login)
        transport.uid = user.uid
        user.transport = transport
        rspd = {'login': login, 'status': 'ok'}
        rsp = Mlang().create_rsp(rspd, _id)
        peername = transport.get_extra_info('peername')
        log.debug('client logon : %i %s' % (user.uid, str(peername)))
        transport.write(rsp.encode())
