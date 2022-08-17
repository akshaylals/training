from email import message
import socket

def client_program():
    # host = socket.gethostname()
    host = '192.168.5.168'
    # as both code
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input('-> ')
    while message.lower().strip() != 'exit':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print('Message from server:', data)

        message = input('Reply to server: ')
    client_socket.close() # close the connection

if __name__ == '__main__':
    client_program()