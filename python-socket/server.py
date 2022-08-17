# import the socket module
import socket

def server_program():
    host = socket.gethostname()  # get the hostname
    # "127.0.0.1" or "localhost"
    port = 5000
    # initiate port no above 1024 till 65535

    # create the instance of socket
    server_socket = socket.socket()

    # bind host address and port number
    # The bind() function takes tuple as argument
    server_socket.bind((host, port))
    
    # start listening to the socket
    # configure how many clients server can listen simultaneously
    server_socket.listen(2)

    # accept an incoming connection
    # the accept() method will give back the conn obj and 
    # address of the incoming connection request
    conn, address = server_socket.accept()
    print('Connection from:', str(address))

    # now we can recieve the messages
    # using a while loop, keep the conneciton active and 
    # recieve messages until there is none
    while True:
        # infinite while loop to receive the data stream
        # receive the packets (max size of 1024 bytes)
        # decode the received data
        data = conn.recv(1024).decode()
        # if data is not received then terminate while loop
        if not data:
            break
        
        # if valid data print the data
        print('Message form client', str(address), ':', str(data))
        # give provision to send reply back to the client
        data = input('Send Reply: ')
        # encode the data and send it to the client
        conn.send(data.encode())
    
    # close the connection once the while loop breaks
    conn.close()

# if our python program is imported, the just be there 
# as an imported code and do not run until the user calls
# the function (default behavior)
# if we directly running it using the command python [prog.py]
# then start the function server_program() automatically
if __name__ == '__main__':
    server_program()