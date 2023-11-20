# Test client to show how to use the microservice and that it works

import pickle
import socket
import errno
from time import sleep

IP, MPORT = 'localhost', 8000


def to_hex(number):
    # Verify our assumption: error is printed and program exists if assumption is violated
    assert number <= 0xffffffff, "Number too large"
    return "{:08x}".format(number)


def recv_data(conn):
    print("== Receiving command")
    data_length_hex = conn.recv(8, socket.MSG_WAITALL)
    data_length = int(data_length_hex, 16)
    full_data = b""
    bytes_recv = 0

    while bytes_recv < data_length:
        data = conn.recv(min(data_length - bytes_recv, 4096))
        full_data += data
        bytes_recv += len(data)

    deserialized_data = pickle.loads(full_data)
    return deserialized_data


def send_data(conn, command):
    print("Sending:", command)
    serialized_data = pickle.dumps(command)
    conn.sendall(to_hex(len(serialized_data)).encode())
    conn.sendall(serialized_data)


def main():
    while True:
        # Configure a socket object to use IPv4 and TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
            try:
                # Connect to the server
                conn.connect((IP, int(MPORT)))
                print(f"== Connected to microservice on port {MPORT}")

                # get command from user
                cmd = input("Enter command: ")
                # send command to microservice
                sleep(3)
                send_data(conn, cmd)
                # receive response from microservice
                sleep(5)
                res = recv_data(conn)
                # print response
                print("== Result:", res)
                sleep(5)
            except ConnectionRefusedError:
                print("== Connection refused, retrying in 5 seconds")
                sleep(5)
            except OSError as e:
                if e.errno == errno.EADDRINUSE:
                    print("== Address already in use, retrying in 5 seconds")
                    sleep(5)
                elif e.errno == errno.EISCONN:
                    print("== Already connected, retrying in 5 seconds")
                    sleep(5)
                else:
                    raise


# Run the `main()` function
if __name__ == "__main__":
    main()
