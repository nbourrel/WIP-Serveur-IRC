import socket
import threading

class Client:
    def __init__(self, address, port):
        self.server_address = address
        self.server_port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            self.client_socket.connect((self.server_address, self.server_port))
            print(f"Connected to server at {self.server_address}:{self.server_port}")
            
            # Start a thread to listen for incoming messages from the server
            threading.Thread(target=self.receive_messages, daemon=True).start()
            
            self.send_messages()
        except Exception as e:
            print(f"Failed to connect: {e}")

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                if message:
                    print(message)
                else:
                    break
            except Exception as e:
                print(f"Error receiving message: {e}")
                break

    def send_messages(self):
        while True:
            message = input()
            if message:
                try:
                    self.client_socket.sendall(message.encode())
                except Exception as e:
                    print(f"Error sending message: {e}")
                    break
            else:
                print("Empty message, please try again.")

    def close(self):
        self.client_socket.close()
        print("Disconnected from server.")
