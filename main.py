from src.server import Server
import src.config as config

def main():
    server = Server(config.server_address, config.server_port)
    server.start()

if __name__ == "__main__":
    main()