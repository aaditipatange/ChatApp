from socket import AF_INET, socket, SOCK_STREAM
import time
from threading import Thread, Lock

class Client:
    """
    A simple TCP client class.
    """
    HOST ='localhost'
    PORT = 5500
    ADDR = (HOST, PORT)
    BUFSIZ = 512

    def __init__(self, name):
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(self.ADDR)
        self.messages= []
        receive_thread = Thread(target=self.receive_messages)
        receive_thread.start()
        self.send_messages(name)
        self.lock = Lock()

    def receive_messages(self):
        """
        receive messages from server
        :return: None
        """
        while True:
            try:
                msg = self.client_socket.recv(self.BUFSIZ).decode()
                self.lock.acquire()
                self.messages.append(msg)
                self.lock.release()
            except Exception as e:
                print("[Exception]",e)
                break

    def send_messages(self, msg):
        """
        send messages to server
        :param msg: str
        :return: None
        """
        self.client_socket.send(bytes(msg, "utf8"))
        if msg =="{quit}":
            self.client_socket.close()

    def get_messages(self):
        """
        """
        messages_copy = self.messages[:]


        self.lock.acquire()
        self.messages = []
        self.lock.release()

        return messages_copy
    
    def disconnect(self):
        self.send_messages("{quit}")
