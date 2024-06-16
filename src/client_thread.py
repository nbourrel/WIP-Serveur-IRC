import threading
from src.commands import handle_command
from src.user import User

class ClientThread(threading.Thread):
    def __init__(self, client_socket, client_address, server):
        super().__init__()
        self.client_socket = client_socket
        self.client_address = client_address
        self.server = server
        self.user = User("guest")  # Default nickname

    def run(self):
        self.handle_client()

    def handle_client(self):
        with self.client_socket:
            while True:
                data = self.client_socket.recv(1024)
                if not data:
                    break
                message = data.decode().strip()
                handle_command(self, message)
        self.server.remove_client(self)

    def send_message(self, message):
        self.client_socket.sendall(message.encode())