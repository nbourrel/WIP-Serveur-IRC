import configparser

config = configparser.ConfigParser()
config.read('config/config.conf')

# Access the configuration values
server_address = config['server']['address']
server_port = int(config['server']['port'])