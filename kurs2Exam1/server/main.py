from kurs2Exam1.server.GuiHandler import GuiHandler
from kurs2Exam1.server.SocketHandler import SocketHandler

socketHandler = SocketHandler()
guiHandler = GuiHandler(socketHandler)
socketHandler.setGuiHandler(guiHandler)

socketHandler.startToAcceptConnection()

guiHandler.start()