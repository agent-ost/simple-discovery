#!/usr/bin/env python
import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.settimeout(1)
client.bind(("", 0))
while True:
    try:
        client.sendto(socket.gethostname(),('<broadcast>',7890))
        data, addr = client.recvfrom(1024)
        print("Got response from ", data, addr)
        time.sleep(1)
    except socket.timeout:
        print("Nothing...")
