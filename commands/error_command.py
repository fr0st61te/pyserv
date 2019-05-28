# -*- coding: utf8 -*-
from server.core.utils import Mlang
from server.core.log import Log

log = Log().get_logger()

def error_command(transport, data):
    if transport is None:
        return
    else:
        if 'id' in data:
            _id = data['id']
        else:
            _id = 99
        data['error_code'] = 1
        response = Mlang().create_rsp(data, _id)
        peername = transport.get_extra_info('peername')
        log.debug('error command %s for transport %s'%(str(_id), str(peername)))
        transport.write(response)
