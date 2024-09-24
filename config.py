import configparser

config = configparser.ConfigParser()
config.read('config.ini')

BASE_URL = config['DEFAULT']['BASE_URL']
TIMEOUT = int(config['DEFAULT']['TIMEOUT'])