#!/usr/bin/env python

"""
A simple echo client
"""

import socket
import struct

host = 'localhost'
port = 7777
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
text = b"""
<cmd id="0">
    <ps archive="0">
	<p login="vasyapupkin" t="c" />
	<p password="123456" t="c" />
    </ps>
</cmd>
"""
text = text + struct.pack('b', 0)
s.send(text)
data = s.recv(size)
s.close()
print('Received:', data)
