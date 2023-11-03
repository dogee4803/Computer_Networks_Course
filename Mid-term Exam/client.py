import socket
import time
import pandas as pd
from sensor_data import read_data
from generate_data import generate_data

def client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set the timeout for the socket
    timeout = 10
    client_socket.settimeout(timeout)

    server_host = "127.0.0.1"
    server_port = 12345

    client_socket.connect((server_host, server_port))

    sensor_data = read_data("wheel_rotation_data.xlsx")

    for row in sensor_data:
        timestamp = str(row[0])
        rotation_count = str(row[1])
        data = f"Timestamp: {timestamp}, Rotation Count: {rotation_count}"

        # Start the timer
        start_time = time.time()

        # Send a ping message with the sensor data to the server
        message = "ping: {}".format(data)
        client_socket.sendall(message.encode())

        # Handling packet loss
        try:
            # Recieve the response from the server
            response = client_socket.recv(1024).decode()
        except socket.timout:
            print("Appropriate message: 'Packet was lost.'")
            continue

        rtt = (time.time() - start_time)

        print(f"Received response: {response}.")
        print(f"Round Trip Time: {rtt * 1000} miliseconds.")

        calculated_timeout = max(rtt, timeout) * 2
        client_socket.settimeout(calculated_timeout)

    # Close the connection
    client_socket.close()

if __name__ == '__main__':
    generate_data('wheel_rotation_data.xlsx')
    client()
