# This microservice is for Brandon Healey's Lego Set Database program in which the user searches for a set and the
# program returns it.

# This program will act as a route manager to direct the request to the correct files to access
# their functions, rather than direct calls

# The user can search for a set, get a random set, or explore Lego Starwars.

# Receive message from LegoProjectUI.py


import pickle
import socket
from time import sleep

# FPORT = Function Port (funcs.py listens on this); MPORT = Main port (your UI or driver file will connect using MPORT)
IP, FPORT, MPORT = 'localhost', 8123, 8000
CHUNK = 100

commands = ["search", "random", "explore", "command"]


def to_hex(number):
    assert number <= 0xffffffff, "Number too large to convert to hex"
    return "{:08x}".format(number)


def send_data(command, conn):
    # print(f"== Sending {command}")
    serialized_command = pickle.dumps(command)
    conn.sendall(to_hex(len(serialized_command)).encode())
    result = conn.sendall(serialized_command)


def recv_data(conn):
    # print("== Receiving command")
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


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as microservice_sock:
        microservice_sock.bind((IP, int(MPORT)))
        microservice_sock.listen()
        print(f"== Microservice listening on port {MPORT}")
        while True:
            conn, addr = microservice_sock.accept()
            with conn:
                print(f"== Received connection from {addr}")
                sleep(5)
                command = recv_data(conn)
                # print(f"== Received command: {command}")
                if command in commands:
                    function_to_call = commands[commands.index(command)]
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as newsocket:
                        newsocket.connect((IP, int(FPORT)))
                        send_data(function_to_call, newsocket)
                        sleep(8)
                        res = recv_data(newsocket)
                        # print("== Res:", res)
                        send_data(res, conn)
                else:
                    send_data("Command not found", conn)
            conn.close()
            print("== Connection closed, sleeping for 5 seconds")
            sleep(5)


if __name__ == "__main__":
    main()
