import client_ui  # Can modify the file name
import time
import socket
import threading
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMessageBox


addrs = ("127.0.0.1", 8080)
class Chat_MainWindow(client_ui.Ui_MainWindow):
    def __init__(self):
        self.flags=['\b', '\0']
        # socket connect
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(addrs)
        self.local_addr=socket.gethostbyname(socket.gethostname())
        self.recv_thread = threading.Thread(target=self.recv)
        self.recv_thread.start()

    def setupUi(self,MainWindow):
        super().setupUi(MainWindow) # Is quite bit faster than super(Chat_MainWindow,self).setupUi()
        # here is the setting append latter
        #MainWindow.setFixedWidth(850)  # lock the window's size
        #MainWindow.setFixedHeight(600)
        self.textEdit.setFont(QFont('Times', 16))  # set the text font
        self.textEdit_2.setFont(QFont('Times', 14))
        self.textEdit_3.setFont(QFont('Times', 14))
        self.textEdit.setReadOnly(True)
        self.textEdit_3.setReadOnly(True)
        self.pushButton.clicked.connect(self.send_packet)
        self.pushButton_2.clicked.connect(lambda : self.get_emoji(self.pushButton_2))
        self.pushButton_3.clicked.connect(lambda : self.get_emoji(self.pushButton_3))
        self.pushButton_4.clicked.connect(lambda : self.get_emoji(self.pushButton_4))
        self.pushButton_5.clicked.connect(lambda : self.get_emoji(self.pushButton_5))
        self.pushButton_6.clicked.connect(lambda : self.get_emoji(self.pushButton_6))
        self.pushButton_7.clicked.connect(lambda : self.get_emoji(self.pushButton_7))
        self.pushButton_8.clicked.connect(lambda : self.get_emoji(self.pushButton_8))
        self.pushButton_9.clicked.connect(lambda : self.get_emoji(self.pushButton_9))
        self.actionsend.triggered.connect(self.send_packet)
        self.actionquit.triggered.connect(self.quit)
        self.actionsave_message.triggered.connect(self.save)
        # --------------------------------

    def send_packet(self):  # send the msg
        msg = self.textEdit_2.toPlainText()
        self.textEdit_2.setText("")
        if "!!QUIT" not in msg:
            self.textEdit.append(f"[*]from you send:\n{msg}")  # The end of msg has "\n"
            msg = (self.local_addr + self.flags[0] + msg).encode("utf-8")  # separate the addrs and msg with '\b' ,
            self.client.send(msg)  # and '\b' means keep connecting
        else:
            self.quit()  # separate the addrs and msg with '\0', and '\0' means disconnecting

    def recv(self):  # recv() open a new thread, and display the msg
        addr_lists = []
        send_addr = ""
        while True:
            raw_data = self.client.recv(1024).decode("utf-8")
            if raw_data:
                for text in raw_data:
                    if text in self.flags:
                        break
                    send_addr += text
                if send_addr not in addr_lists:
                    addr_lists.append(send_addr)
                    self.textEdit_3.append(f"IP{addr_lists.index(send_addr)}:{send_addr}")
                data = raw_data.replace(send_addr + "\b", "")
                data = f"[*] from {send_addr} send:\n{data}"  # The end of data has "\n"
                self.textEdit.append(data)
                send_addr = ""
            else:
                break

    @staticmethod
    def save(self):
        with open("save.txt", "a+") as file:
            file.write("\n" + self.textEdit.toPlainText())
            file.close()

    def quit(self):
        self.client.send(self.flags[1].encode("utf-8"))
        self.client.close()
        self.textEdit.setText("Have a nice Day(~~")
        QMessageBox.about(MainWindow, "Shut down", "Have a nice day(~~")
        time.sleep(1)
        sys.exit()

    def get_emoji(self,button): # The emoji will be added into textedit_2
        self.textEdit_2.insertPlainText(button.text())

class Window(client_ui.QtWidgets.QMainWindow):
    def __init__(self):
        client_ui.QtWidgets.QMainWindow.__init__(self)
        self.chat_window= ""
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.chat_window.quit()

if __name__ == "__main__":
    app = client_ui.QtWidgets.QApplication(sys.argv)
    MainWindow = Window()
    chat_window = Chat_MainWindow()
    chat_window.setupUi(MainWindow)
    MainWindow.chat_window=chat_window
    MainWindow.show()
    #close the windows
    sys.exit(app.exec_())