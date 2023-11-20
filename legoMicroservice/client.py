# Test client to show how to use the microservice and that it works

import socket
from time import sleep

IP, MPORT = 'localhost', 8000


def to_hex(number):
    # Verify our assumption: error is printed and program exists if assumption is violated
    assert number <= 0xffffffff, "Number too large"
    return "{:08x}".format(number)


def recv_msg(conn):
    full_data = b""
    data = b""

    while data != b'\n':
        data = conn.recv(1)
        full_data += data

    return full_data.decode()


def send_msg(conn, message):
    conn.sendall(to_hex(len(message)).encode())
    conn.sendall(message.encode())


def main():
    # Configure a socket object to use IPv4 and TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
        # Connect to the server
        conn.connect((IP, int(MPORT)))
        print(f"== Connected to microservice on port {MPORT}")

        # get command from user
        cmd = input("Enter command: ")
        # send command to microservice
        sleep(3)
        send_msg(conn, cmd)
        # receive response from microservice
        sleep(5)
        response = recv_msg(conn)
        # print response
        print(response)


# Run the `main()` function
if __name__ == "__main__":
    main()
