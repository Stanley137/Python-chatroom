# -*- coding: utf-8 -*-
"""
Created on Thu May 27 11:47:12 2021

@author: 88698
"""

import socket
import threading

addrs=("127.0.0.1",8080)
send_addr=""

def recv():         # recv() 加開一個執行緒，負責將收到的訊息打印出來     
    global send_addr
    while True:
        raw_data=client.recv(4096).decode("utf-8")    
        for text in raw_data:
            if text=="\n":
                break
            send_addr+=text   
        data=raw_data.replace(send_addr+"\n","")
        print(f"[*] from {send_addr}:")
        print(f"{data}")
        send_addr=""
        
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(addrs)
recv_thread=threading.Thread(target=recv)
recv_thread.start()
while True:  # 負責轉傳訊息
    msg=input("Msg:")
    hostname=socket.gethostname()
    local_addr=socket.gethostbyname(hostname)
    msg=(local_addr+'\n'+msg).encode("utf-8") # '\n'換行字元區隔出IP跟訊息，還有編碼
    client.send(msg)   
