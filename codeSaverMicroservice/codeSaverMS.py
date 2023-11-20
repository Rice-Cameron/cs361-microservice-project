import socket
import pickle

def process_data(data):
    # Process the received data
    if data == 1:
        return {"result": "Option 1"}
    elif data == 2:
        return {"result": "Option 2"}
    elif data == 3:
        return {"result": "Option 3"}
    elif data == 4:
        return {"result": "Option 4"}
    else:
        return {"result": "Invalid Option"}

def receive_data(client_socket):
    received_data = b""
    while True:
        chunk = client_socket.recv(1024)
        if not chunk:
            break
        received_data += chunk
        if received_data.endswith(b"__END_OF_TRANSMISSION__"):
            break
    return pickle.loads(received_data[:-len(b"__END_OF_TRANSMISSION__")])

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    host = "127.0.0.1"  # localhost
    port = 12345
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    while True:
        # Wait for a connection from a client
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        # Receive data from the client
        data = receive_data(client_socket)

        if not data:
            break

        # Process the received data
        result = process_data(data)

        # Send the result back to the client
        client_socket.send(pickle.dumps(result))

        # Close the connection
        client_socket.close()

    # Close the server socket when the loop is exited
    server_socket.close()

if __name__ == "__main__":
    start_server()
