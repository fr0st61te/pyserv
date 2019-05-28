# -*- coding: utf8 -*-
import asyncio
import logging
from server.core.utils import Mlang
from server.client_protocol import ClientProtocol as Protocol
from server.core.log import Log

log = Log().get_logger()
log.setLevel(logging.DEBUG)
Mlang('xml')

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    server_coroutine = loop.create_server(Protocol, '127.0.0.1', 7777)
    try:


        def shutdown_exception_handler(_loop, context):
            if "exception" not in context \
                    or not isinstance(context["exception"], asyncio.CancelledError):
                _loop.default_exception_handler(context)

        loop.set_exception_handler(shutdown_exception_handler)
        loop.run_until_complete(server_coroutine)
        loop.run_forever()
    except KeyboardInterrupt as e:
        print("Server is down. Caught keyboard interrupt...")
    finally:
        loop.close()
