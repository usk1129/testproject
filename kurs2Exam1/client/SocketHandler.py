import socket

import _thread

class SocketHandler:
    def __init__(self):
        self.clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def setGuiHandler(self,guiHandler_):
        self.guiHandler = guiHandler_

    def connect(self,ip, port):
        self.clientSocket.connect((ip,port))
        self.startReceiverThread()

    def sendMsg(self,text):
        self.clientSocket.send(str.encode(text))

    def startReceiverThread(self):
        _thread.start_new_thread(self.startReceiving,())

    def startReceiving(self):
        while True:
            msg = self.clientSocket.recv(1024).decode()
            self.guiHandler.showMessage(msg)
