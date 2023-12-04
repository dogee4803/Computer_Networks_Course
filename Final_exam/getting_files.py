def receive_image(client_socket, image_path):
    with open(image_path, 'wb') as file:
        while True:
            image_data = client_socket.recv(1024)
            if not image_data:
                break
            file.write(image_data)

def receive_csv(client_socket, csv_path):
    with open(csv_path, 'w') as file:
        while True:
            csv_data = client_socket.recv(1024).decode()
            if not csv_data:
                break
            file.write(csv_data)

def receive_json(client_socket):
    json_data = client_socket.recv(1024).decode()
    return json.loads(json_data)