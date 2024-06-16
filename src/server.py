import socket
import threading
from src.client_thread import ClientThread

class Server:
    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.clients = []
        self.channels = {}  # Initialize the channels dictionary

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.address, self.port))
        self.server_socket.listen(5)
        print(f"Server started on {self.address}:{self.port}")

        while True:
            client_socket, client_address = self.server_socket.accept()
            client_thread = ClientThread(client_socket, client_address, self)
            client_thread.start()
            self.clients.append(client_thread)

    def remove_client(self, client_thread):
        if client_thread in self.clients:
            for channel_name in client_thread.user.channels:
                self.channels[channel_name].remove_user(client_thread.user)
            self.clients.remove(client_thread)