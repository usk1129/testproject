from kurs2Exam1.client.GuiHandler import GuiHandler
from kurs2Exam1.client.SocketHandler import SocketHandler

socketHandler = SocketHandler()
guiHandler = GuiHandler(socketHandler)
socketHandler.setGuiHandler(guiHandler)

socketHandler.connect('127.0.0.1',9999)

guiHandler.start()