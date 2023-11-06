# Cameron Rice
# ricecam@oregonstate.edu

import socket
import Snippet
import Database

IP, DPORT = 'localhost', 8080
CHUNK = 100


def to_hex(number):
    assert number <= 0xffffffff, "Number too large to convert to hex"
    return "{:08x}".format(number)


def send_data(command):
    # send command to microservice via socket
    # for now, just show that the command is making it to this function which will then somehow
    # send it to the microservice in which will figure out what file to open and what function to call
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
        conn.connect((IP, int(DPORT)))
        print(f"== Sending {command} to microservice")
        conn.sendall(to_hex(len(command)).encode())
        conn.sendall(command.encode())


def recv_data():
    # receive data from microservice via socket
    # for now, just show that the command is making it to this function which will then somehow
    # send it to the microservice in which will figure out what file to open and what function to call
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
        conn.connect((IP, int(DPORT)))
        print(f"== Receiving data from microservice")
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