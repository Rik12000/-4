import socket
import threading
import os

UDP_MAX_SIZE = 65535

# Function to listen to incoming messages and display them
def listen(s: socket.socket):
    while True:
        msg = s.recv(UDP_MAX_SIZE)
        print('\r\r' + msg.decode('utf-8') + '\n' + f'you: ', end='')

def connect(host: str = '127.0.0.1', port: int = 3000):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Client connects to the server
    s.connect((host, port))

    threading.Thread(target=listen, args=(s,), daemon=True).start()

    # Inform the server that the client has joined the chat
    s.send('__join'.encode('utf-8'))

    # Client can write messages as many times as they want
    while True:
        msg = input(f'you: ')
        s.send(msg.encode('utf-8'))

# Clear the terminal, greet the client, and connect to the server
if __name__ == '__main__':
    os.system('clear')
    print('Welcome to chat!')
    connect()
