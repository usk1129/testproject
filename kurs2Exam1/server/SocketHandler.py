import socket
import _thread

class SocketHandler:
    def __init__(self):
        self.serverSocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.serverSocket.bind(('',9999))
        self.serverSocket.listen()

    def setGuiHandler(self,guiHandler_):
        self.guiHandler = guiHandler_

    def startToAcceptConnection(self):
        self.clientSocket, self.clientAddr = self.serverSocket.accept()
        self.startReceiverThread()


    def sendMsg(self,text):
        self.clientSocket.send(str.encode(text))

    def startReceiverThread(self):
        _thread.start_new_thread(self.startReceiving,())

    def startReceiving(self):
        while True:
            msg = self.clientSocket.recv(1024).decode()
            self.guiHandler.showMessage(msg)
