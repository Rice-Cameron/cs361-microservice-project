# Test funcs to show how to use the microservice and that it works

import pickle
import socket
from time import sleep

IP, FPORT = 'localhost', 8123


# test function in placement of search, random, explore
def command():
    print("Command function called")
    return 0


routes = {
    "command": lambda: command(),
    # "search": search(),
    # "random": random(),
    # "explore": explore()
    # insert your functions here
}


def to_hex(number):
    # Verify our assumption: error is printed and program exists if assumption is violated
    assert number <= 0xffffffff, "Number too large"
    return "{:08x}".format(number)


def recv_data(conn):
    print("== Receiving command")
    try:
        data_length_hex = conn.recv(8, socket.MSG_WAITALL)
        data_length = int(data_length_hex, 16)
        full_data = b""
        bytes_recv = 0
        while bytes_recv < data_length:
            data = conn.recv(min(data_length - bytes_recv, 4096))
            full_data += data
            bytes_recv += len(data)
    except socket.timeout:
        print("== No data received within the timeout period")
        return 0

    deserialized_data = pickle.loads(full_data)
    return deserialized_data


def send_data(conn, message):
    print("Sending:", message)
    serialized_message = pickle.dumps(message)
    conn.sendall(to_hex(len(serialized_message)).encode())
    conn.sendall(serialized_message)


def test_ms_call(conn):
    # Wait for the microservice to send a message
    cmd = recv_data(conn)
    print("Received:", cmd)
    # call the function with the name 'intro'
    # if the function exists, it will be called
    # if the function does not exist, the program will crash
    if cmd in routes:
        # call the function
        res = routes[cmd]()
        print(f"== Result: {res}")
        if res == 0:
            # send the result back to the microservice
            sleep(5)
            send_data(conn, res)
        if res != 0:
            sleep(5)
            send_data(conn, "Error in function")
    else:
        # send a message back to the microservice
        sleep(5)
        send_data(conn, "Command not found")


def main():
    # Configure a socket object to use IPv4 and TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
        conn.bind((IP, int(FPORT)))
        conn.listen()
        print(f"== Funcs listening on port {FPORT}")
        while True:
            client_conn, addr = conn.accept()
            with client_conn:
                client_conn.settimeout(10.0)
                print(f"== Received connection from {addr}")
                try:
                    test_ms_call(client_conn)
                    conn.close()
                    return None
                except socket.timeout:
                    print("== Connection timed out")


# Run the `main()` function
if __name__ == "__main__":
    main()
