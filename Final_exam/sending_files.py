def send_image(client_socket, image_path):
    with open(image_path, 'rb') as file:
        image_data = file.read()
        client_socket.sendall(image_data)

def send_csv(client_socket, csv_path):
    with open(csv_path, 'r') as file:
        csv_data = file.read()
        client_socket.sendall(csv_data.encode())

def send_json(client_socket, json_data):
    json_str = json.dumps(json_data)
    client_socket.sendall(json_str.encode())