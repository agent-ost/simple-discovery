#!/usr/bin/env python
import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.settimeout(1)
client.bind(("", 7890))
while True:
    try:
        data, addr = client.recvfrom(1024)
        client.sendto(socket.gethostname(), addr)
        print("Woke", addr)
    except socket.timeout:
        pass
