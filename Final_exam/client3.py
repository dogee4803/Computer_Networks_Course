import socket
import threading
from menu_form import menu
import json

# A func to get address list
def receive_address_list_from_server(connected_client_socket):
    address_list = connected_client_socket.recv(1024).decode('utf-8')
    addresses = json.loads(address_list)
    print(addresses)
    return addresses

# Handling incoming messages
def handle_incoming_messages(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print("Received message:", data.decode())
    client_socket.close()

def run_client3():
    # Making a client socket and connecting
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_host = '127.0.0.1'
    server_port = 12345
    client_socket.connect((server_host, server_port))

    # Working with list of addresses to make appropriate format for port and host
    addresses = receive_address_list_from_server(client_socket)
    client1, client2, client3 = addresses
    print(f"Address listing: {client1} , {client2} , {client3}")

    client1_host, client1_port = client1.split(":")
    client2_host, client2_port = client2.split(":")
    client3_host, client3_port = client3.split(":")

    # Creating a sub-sockets for multiconnections to each others
    client1_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client2_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client3_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client1_socket.connect((client1_host, int(client1_port)))
    client2_socket.connect((client2_host, int(client2_port)))
    client3_socket.connect((client3_host, int(client3_port)))

    # Making multiple listening available
    threading.Thread(target=handle_incoming_messages, args=(client1_socket,)).start()
    threading.Thread(target=handle_incoming_messages, args=(client2_socket,)).start()
    threading.Thread(target=handle_incoming_messages, args=(client3_socket,)).start()

    while True:
        choice = menu() #Menu-form
        message = input("Enter msg: ")
        if choice == "target": # Sending data to one client
            target = int(input("Choose client 1/2/3: "))
            if target == 1:
                client1_socket.sendall(message.encode())
            elif target == 2:
                client2_socket.sendall(message.encode())
            elif target == 3:
                client3_socket.sendall(message.encode())
        elif choice == "all": # Sending data to all clients
            client1_socket.sendall(message.encode())
            client2_socket.sendall(message.encode())
            client3_socket.sendall(message.encode())
        elif choice == "pass": # Just pass
            continue
        elif choice == "close socket": # Finishing working and closing all sockets
            print("Socket is closed")
            client1_socket.close()
            client2_socket.close()
            client3_socket.close()
            break
        else:
            print("Incorrect input. Try again.")

if __name__ == '__main__':
    run_client3()