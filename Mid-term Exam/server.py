import socket

def server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = '127.0.0.1'
    port = 12345

    # Bind the socket to a specific address and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(10)

    print("Server located on {}:{}".format(host, port))

    while True:
        # Accept a client connection
        client_socket, addr = server_socket.accept()
        print("Client with this address: {}".format(addr))

        while True:
            # Receive data from the client
            data = client_socket.recv(1024).decode()
            print("Received message: {}".format(data))

            if not data:
                break

            response = "pong"
            client_socket.send(response.encode())

        client_socket.close()

if __name__ == '__main__':
    server()
