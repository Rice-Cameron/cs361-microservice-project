# This microservice is for Brandon Healey's Lego Set Database program in which the user searches for a set and the
# program returns it.
# This program will act as a route manager to direct the request to the correct files to access
# their functions, rather than direct calls

# The user can search for a set, get a random set, or explore Lego Starwars.

# Receive message from LegoProjectUI.py


# TODO. SEND REQUEST SOMEHOW TO THE CORRECT FILE

# TODO. Test using importlib.import_module() to import the correct file and run the correct function


import socket, subprocess
# import importlib

# FPORT = Function Port; MPORT = Main port
IP, FPORT, MPORT = 'localhost', 9000, 8080
CHUNK = 100

commands = ["search", "random", "explore", "test"]


def to_hex(number):
    assert number <= 0xffffffff, "Number too large to convert to hex"
    return "{:08x}".format(number)


def send_data(command, port):
    # send command to microservice via socket
    # for now, just show that the command is making it to this function which will then somehow
    # send it to the microservice in which will figure out what file to open and what function to call
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
        conn.connect((IP, int(port)))
        print(f"== Sending {command} to microservice")
        conn.sendall(to_hex(len(command)).encode())
        conn.sendall(command.encode())


def recv_data(port):
    # receive data from microservice via socket
    # for now, just show that the command is making it to this function which will then somehow
    # send it to the microservice in which will figure out what file to open and what function to call
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
        conn.connect((IP, int(port)))
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


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as microservice_sock:
        microservice_sock.bind((IP, int(MPORT)))
        microservice_sock.listen()

        print(f"== Microservice listening on port {MPORT}")

        while True:
            conn, addr = microservice_sock.accept()
            with conn:
                print(f"== Received connection from {addr}")
                command = recv_data(MPORT)
                print(f"== Received command: {command}")
                # check which command was sent against routes dict
                if command in commands:
                    function_to_call = commands[commands.index(command)]
                    # close connection, open new one on FPORT
                    conn.close()
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
                        conn.connect((IP, int(FPORT)))
                        # send command to function port
                        send_data(function_to_call, FPORT)
                        # receive data from function port
                        recv_data(FPORT)
                        conn.close()
                print(f"== Sent results to client")
                conn.close()


if __name__ == "__main__":
    main()
