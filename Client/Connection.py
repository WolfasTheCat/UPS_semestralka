from argparse import OPTIONAL
from mailbox import Message
import socket
import sys
import tkinter


class ConnectionManager():
    SOCKET = None
    DATA = ""
    ADDRESS = "127.0.0.1"
    LOCALPORT = 10000
    INET_ADDRESS = None
    CONNECTED = False
    READER = None
    WRITER = None
    S_HOST = None
    S_PORT = None
    
    
    #Builder for Connection Manager
    def __init__(self) -> None: #Co to jako je? - Návratová hodnota
        
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            option = len(sys.argv)
            match option:
                case 4:
                    pass
                    #self.is_port_in_use
                    #Prenastavit local port - zatim neni potreba
                case 2:
                    if(sys.argv[2] == "a"):
                        pass
            
    def is_port_in_use(self,port: int) -> bool:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(('localhost', port)) == 0
        

    #Creates connection to server
    def create_connection(self, S_HOST,S_PORT):
        try:
            self.S_HOST = S_HOST
            self.S_PORT = S_PORT
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.SOCKET = s
            s.connect((S_HOST,S_PORT))
            
        except:
            self.CONNECTED = False
            print("Couldn't connect")
            tkinter.messagebox.showerror(title=None, message="Problem with connection")
            return
        
        self.CONNECTED = True
        self.INET_ADDRESS = self.SOCKET.getpeername()
    
    #Recieve message from server
    def recieve_message(self):
        DATA_C = self.SOCKET.recv(1024)
        self.DATA = DATA_C.decode("utf-8")
        
    
    #Send message to server
    def send_message(self, message):
        if ((self.CONNECTED) != True):
            print("Can't send message. Connection isn't established")
        else:
            print("Sending message: " + message)
            self.SOCKET.sendall(str.encode(message))

    
    def close_connection(self):
        try:
            self.SOCKET.close()
            self.CONNECTED = False

        except:
            print("Couldn't disconnect")