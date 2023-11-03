# Importing Required Modules
import socket
import threading
import time

# Setting up TCP Server
def setup_tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(10)
    print("TCP server set up on port 12345")
    while True:
        client_socket, address = server_socket.accept()
        threading.Thread(target=handle_client, args=(client_socket, address)).start()

# Handling Client Connection
def handle_client(client_socket, address):
    client_socket.sendall(b"Server: Hi, Client!")
    data = client_socket.recv(1024)
    print(f"Received: {data.decode()} from {address}.")
    client_socket.close()

# Simulating TCP Clients
def setup_tcp_client(client_id):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    client_socket.sendall(f"Client {client_id}: Hi, Server!".encode())
    data = client_socket.recv(1024)
    print(f"Received: {data.decode()} from {client_socket.getpeername()}")
    client_socket.close()

# Measuring Data Transfer Rate
def measure_transfer_rate():
    start_time = time.time()
    threads = []
    for i in range(1, 11):
        thread = threading.Thread(target=setup_tcp_client, args=(i,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\nData transfer time: {elapsed_time} seconds")


def main():
    print("Starting the lab session setup...")
    server_thread = threading.Thread(target=setup_tcp_server)
    server_thread.daemon = True
    server_thread.start()
    time.sleep(2)
    measure_transfer_rate()
    print("Lab session setup is completed.")

if __name__ == "__main__":
    main()
