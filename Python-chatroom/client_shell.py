# -*- coding: utf-8 -*-
"""
Created on Thu May 27 11:47:12 2021
@author: 88698
"""

import socket
import threading
import sys
import time

addrs = ("127.0.0.1", 8080)
flags = ["\b", "\0"]  # the command list


def recv():  # recv() add a new thread, and print the msg
    global flags
    send_addr = ""
    while True:
        raw_data = client.recv(1024).decode("utf-8")
        if raw_data:
            for text in raw_data:
                if text in flags:
                    break
                send_addr += text
            data = raw_data.replace(send_addr + "\b", "")
            print(f"[*] from {send_addr}:{data}")
            send_addr = ""
        else:
            break


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addrs)
recv_thread = threading.Thread(target=recv)
recv_thread.start()

while True:  # send the msg
    local_addr = socket.gethostbyname(socket.gethostname())
    msg = input('')
    if "quit()" not in msg:
        msg = (local_addr + flags[0] + msg).encode("utf-8")  # separate the msg and IP with '\b'
        client.send(msg)  # '\b' means keeps connecting
    else:
        msg = (local_addr + flags[1] + msg).encode("utf-8")  # separate the msg and IP with '\0'
        client.send(msg)  # '\0' means disconnect
        client.close()
        print("Have a nice Day(~~")
        time.sleep(1)
        sys.exit()