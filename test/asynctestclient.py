import asyncio
import struct

class EchoClientProtocol(asyncio.Protocol):
    def __init__(self, message, loop):
        self.message = message
        self.loop = loop

    def connection_made(self, transport):
        transport.write(self.message)
        print('Data sent: {!r}'.format(self.message))

    def data_received(self, data):
        print('Data received: {!r}'.format(data.decode()))

    def connection_lost(self, exc):
        print('The server closed the connection')
        print('Stop the event loop')
        self.loop.stop()

loop = asyncio.get_event_loop()
text = b"""
<cmd id="0">
    <ps archive="0">
	<p login="vasyapupkin" t="c" />
	<p password="123456" t="c" />
    </ps>
</cmd>
"""
text = text + struct.pack('b', 0)
coro = loop.create_connection(lambda: EchoClientProtocol(text, loop),
                              '127.0.0.1', 7777)
loop.run_until_complete(coro)
loop.run_forever()
loop.close()
