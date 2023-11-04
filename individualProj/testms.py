# NOT ACTUAL MICROSERVICE, JUST A TEST

import socket

INTERFACE, SPORT = 'localhost', 8080
CHUNK = 100


def receive_command(conn):
    data_length_hex = conn.recv(8, socket.MSG_WAITALL)

    data_length = int(data_length_hex, 16)

    data = b""
    full_data = b""
    bytes_recv = 0

    while bytes_recv < data_length:
        data = conn.recv(CHUNK)
        full_data += data
        bytes_recv += len(data)

    return full_data.decode()


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as microservice_sock:
        microservice_sock.bind((INTERFACE, int(SPORT)))
        microservice_sock.listen()

        print(f"== Microservice listening on port {SPORT}")

        while True:
            conn, addr = microservice_sock.accept()
            with conn:
                print(f"== Received connection from {addr}")
                command = receive_command(conn)
                print(f"== Received command: {command}")


if __name__ == "__main__":
    main()
