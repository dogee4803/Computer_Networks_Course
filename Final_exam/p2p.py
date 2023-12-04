import socket
import threading
import json

# A func to send a list of adresses to clients
def send_address_list_to_client(client_socket, addresses):
    address_list = json.dumps(addresses)
    client_socket.send(address_list.encode('utf-8'))

# Getting adress and sending a list of all
def handle_client(client_socket, clients):
    print("New connection from:", client_socket.getpeername())
    addresses = [f"{client.getpeername()[0]}:{client.getpeername()[1]}" for client in clients]
    send_address_list_to_client(client_socket, addresses)

def run_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    host = '127.0.0.1'
    port = 12345
    server_socket.bind((host, port))

    print("Server located on {}:{}".format(host, port))

    # Staring to accept all 3 clients connections
    server_socket.listen(3) 
    print("Waiting for connections...")
    clients = []
    while len(clients) < 3:
        client_socket, addr = server_socket.accept()
        clients.append(client_socket)

    # Making multiple listening available
    for client_socket in clients:
        threading.Thread(target=handle_client, args=(client_socket, clients)).start()

if __name__ == '__main__':
    run_server()
