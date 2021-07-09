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
            msg=self.client.recv(1024) #每個執行緒有自己的讀寫緩衝區
            decoded_msg=msg.decode("utf-8")
            if flag[1] not in decoded_msg:
                decoded_msg=decoded_msg.replace(flag[0],"")
                print(f'[*] {self.addrs}:\n{decoded_msg}')
                send.acquire()  #鎖住
                self.write_client(self.client,msg)    #防止順序混亂
                send.release()  #釋放
            else:
                print(f"[!] {self.addrs} disconnected!!")
                break
        self.client.close()
        client_lists.remove(self.client)
    @staticmethod
    def write_client(client_send,msg): #將訊息轉傳至其他客戶端
        for client in client_lists: #廣播
            if client_send != client:
                client.send(msg)
        
send=threading.Lock() #執行緒鎖
addrs=("0.0.0.0",8080)
flag=["\b","\0"]
client_lists=[]
# handler_lists=[]
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(addrs)
server.listen(5) #監聽連結最多5人

while(True):
    client,addrs=server.accept()
    print(f"[!] {addrs} connected!")
    client_lists.append(client) 
    thread=client_handler(client,addrs)
    thread.start()
  #  handler_lists.append(thread)
    