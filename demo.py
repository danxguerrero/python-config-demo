import configparser

config = configparser.ConfigParser()

config.read('config.ini')

username = config.get('settings', 'username')
password = config.get('settings', 'password')
debug_mode = config.get('settings', 'debug')

print(f'Username: {username}, Password: {password}, Debug Mode: {debug_mode}')