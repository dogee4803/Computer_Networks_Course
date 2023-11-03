# Importing Required Modules
import socket
import threading
import time

# Setting up UDP Server
def setup_udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 12345))
    print("UDP server set up on port 12345")
    while True:
        data, address = server_socket.recvfrom(1024)
        threading.Thread(target=handle_client, args=(server_socket, data, address)).start()


# Handling Client Connection
def handle_client(server_socket, data, address):
    server_socket.sendto(b"Server: Hi, Client!", address)
    print(f"Received: {data.decode()} from {address}.")
    server_socket.close()

# Simulating UDP Clients
def setup_udp_client(client_id):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto(f"Client {client_id}: Hi, Server!".encode(), ("localhost", 12345))
    data, address = client_socket.recvfrom(1024)
    print(f"Received: {data.decode()} from {address}.")
    client_socket.close()

# Measuring Data Transfer Rate
def measure_transfer_rate():
    start_time = time.time()
    threads = []
    for i in range(1, 11):
        thread = threading.Thread(target=setup_udp_client, args=(i,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\nData transfer time: {elapsed_time} seconds")

def main():
    print("Starting the lab session setup...")
    server_thread = threading.Thread(target=setup_udp_server)
    server_thread.daemon = True
    server_thread.start()
    time.sleep(2)
    measure_transfer_rate()
    print("Lab session setup is completed.")

if __name__ == "__main__":
    main()
