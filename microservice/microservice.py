# This microservice is for Brandon Healey's Lego Set Database program in which the user searches for a set and the
# program returns it.

# This program will act as a route manager to direct the request to the correct files to access
# their functions, rather than direct calls

# The user can search for a set, get a random set, or explore Lego Starwars.

# Receive message from LegoProjectUI.py


import socket
from time import sleep

# import importlib

# FPORT = Function Port; MPORT = Main port (your UI or driver file will use MPORT)
IP, FPORT, MPORT = 'localhost', 8123, 8000
CHUNK = 100

commands = ["search", "random", "explore", "command"]


def to_hex(number):
    assert number <= 0xffffffff, "Number too large to convert to hex"
    return "{:08x}".format(number)


def send_data(command, conn):
    print(f"== Sending {command}")
    conn.sendall(to_hex(len(command)).encode())
    conn.sendall(command.encode())


def recv_data(conn):
    print(f"== Receiving data")
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
        microservice_sock.bind((IP, int(MPORT)))
        microservice_sock.listen()

        print(f"== Microservice listening on port {MPORT}")

        while True:
            conn, addr = microservice_sock.accept()
            with conn:
                print(f"== Received connection from {addr}")
                sleep(5)
                command = recv_data(conn)
                print(f"== Received command: {command}")
                # check which command was sent against routes dict
                if command in commands:
                    print(f"== In if statement")
                    function_to_call = commands[commands.index(command)]
                    # close connection, open new one on FPORT
                    conn.close()
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as newsocket:
                        newsocket.connect((IP, int(FPORT)))
                        # Error: address already in use for the line above
                        print("== In new conn")
                        # send command to function port
                        send_data(function_to_call, newsocket)
                        # receive data from function port
                        sleep(5)
                        recv_data(newsocket)
                        newsocket.close()
                print(f"== Sent results to client")
                conn.close()


if __name__ == "__main__":
    main()
