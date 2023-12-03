# Cameron Rice
# ricecam@oregonstate.edu

"""
This is the microservice that will be listening on MPORT (8000) for connections from the UI file.
It will then connect to either CPORT (8123) or APORT (8124) depending on the command received from the UI file.
"""

import pickle
import socket
from time import sleep

# FPORT = Function Port (funcs.py listens on this); MPORT = Main port (your UI or driver file will connect using MPORT)
IP, CPORT, MPORT, APORT = 'localhost', 8123, 8000, 8124
CHUNK = 100

commands = ["add", "view", "edit", "delete", "search", "tag", "export", "import", "help", "exit"]
crud_cmds = ["add", "view", "edit", "delete"]
adv_cmds = ["search", "tag", "export", "import"]


def to_hex(number):
    assert number <= 0xffffffff, "Number too large to convert to hex"
    return "{:08x}".format(number)


def send_data(command, conn):
    serialized_command = pickle.dumps(command)
    conn.sendall(to_hex(len(serialized_command)).encode())
    result = conn.sendall(serialized_command)


def recv_data(conn):
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
                # Tokenize and check first part of command
                print(command)
                if not isinstance(command, dict):
                    command_token = command.split()[0]
                    if command_token in commands:
                        function_to_call = commands[commands.index(command_token)]
                        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as newsocket:
                            # If in crud_cmds, connect to CPORT, if in adv_cmds, connect to APORT
                            if function_to_call in crud_cmds:
                                newsocket.connect((IP, int(CPORT)))
                            elif function_to_call in adv_cmds:
                                newsocket.connect((IP, int(APORT)))
                            send_data(command, newsocket)
                            sleep(8)
                            res = recv_data(newsocket)
                            send_data(res, conn)
                # Logic for add dict()
                elif isinstance(command, dict):
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as newsocket:
                        newsocket.connect((IP, int(CPORT)))
                        send_data(command, newsocket)
                        sleep(8)
                        res = recv_data(newsocket)
                        send_data(res, conn)
                else:
                    send_data("Command not found", conn)
            conn.close()
            print("== Connection closed, sleeping for 5 seconds")
            sleep(5)


if __name__ == "__main__":
    main()
