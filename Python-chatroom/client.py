# -*- coding: utf-8 -*-
"""
Created on Thu May 27 11:47:12 2021

@author: 88698
"""

import socket
import threading
import sys
import time

addrs=("127.0.0.1",8080)
send_addr=""
flags=["\b", "\0"]

def recv():         # recv() 加開一個執行緒，負責將收到的訊息打印出來     
    global send_addr
    global flags
    while True:
        raw_data=client.recv(1024).decode("utf-8")
        if raw_data:
            for text in raw_data:
                if text in flags:
                    break
                send_addr+=text
            data=raw_data.replace(send_addr+"\b","")
            print(f"[*] from {send_addr}:{data}")
            send_addr=""
        else:
            break
        
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(addrs)
recv_thread=threading.Thread(target=recv)
recv_thread.start()

while True:  # 負責轉傳訊息
    local_addr = socket.gethostbyname(socket.gethostname())
    msg=input('')
    if "quit()" not in msg:
        msg=(local_addr + flags[0] + msg).encode("utf-8") # '\b'換行字元區隔出IP跟訊息，還有編碼
        client.send(msg)
    else:
        msg = (local_addr + flags[1] + msg).encode("utf-8") #'\a'字元代表結束傳訊
        client.send(msg)
        client.close()
        print("Have a nice Day(~~")
        time.sleep(1)
        sys.exit()

