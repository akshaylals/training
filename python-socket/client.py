import socket

def client_program():
    host = socket.gethostname()
    # host = '192.168.5.168'
    # as both code
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    # getting the message to sent to server
    message = input('-> ')
    while message.lower().strip() != 'exit':
        # if the msg is not 'exit', encode and send ti to server
        client_socket.send(message.encode())
        # receive any reply data from the server
        data = client_socket.recv(1024).decode()
        # print the received data as text
        print('Received from server:', data)

        message = input('Reply to server: ')

    client_socket.close() # close the connection

if __name__ == '__main__':
    client_program()