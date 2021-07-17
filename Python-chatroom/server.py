# -*- coding: utf-8 -*-
"""
Created on Thu May 27 11:46:51 2021

@author: 88698
"""
import socket
import threading

class client_handler(threading.Thread):
    def __init__(self,client,addrs):
        self.client=client
        self.addrs=addrs
        threading.Thread.__init__(self)
    def run(self):
        while True:
            msg=self.client.recv(1024) # every thread has it own buffer for reading
            decoded_msg=msg.decode("utf-8")
            if flag[1] not in decoded_msg:
                decoded_msg=decoded_msg.replace(flag[0],"")
                print(f'[*] {self.addrs}:\n{decoded_msg}')
                send.acquire()  # lock
                self.write_client(self.client,msg)    # prevent from the error of the msg's sequence
                send.release()  # unlock
            else:
                print(f"[!] {self.addrs} disconnected!!")
                break
        self.client.close()
        client_lists.remove(self.client)
    @staticmethod
    def write_client(client_send,msg): # Repost the msg from the client
        for client in client_lists: # boardcast
            if client_send != client:
                client.send(msg)
        
send=threading.Lock()
addrs=("0.0.0.0",8080)
flag=["\b","\0"]
client_lists=[]
# handler_lists=[]
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(addrs)
server.listen(5) # the client limits=5

while(True):
    client,addrs=server.accept()
    print(f"[!] {addrs} connected!")
    client_lists.append(client) 
    thread=client_handler(client,addrs)
    thread.start()
  #  handler_lists.append(thread)
    