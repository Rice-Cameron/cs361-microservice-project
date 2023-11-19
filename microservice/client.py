# Test client to show how to use the microservice and that it works

import socket

IP, FPORT = 'localhost', 9000


# test function in placement of search, random, explore
def command():
    print("Command function called")
    return 0


routes = {
    "command": command(),
    # "search": search(),
    # "random": random(),
    # "explore": explore()
    # insert your functions here
}


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


def test_ms_call(conn):
    # Wait for the microservice to send a message
    cmd = recv_msg(conn)
    print("Received:", cmd)
    # call the function with the name 'intro'
    # if the function exists, it will be called
    # if the function does not exist, the program will crash
    if cmd in routes:
        # call the function
        res = routes[cmd]()
        if res == 0:
            # send the result back to the microservice
            send_msg(conn, "Success")
        if res != 0:
            send_msg(conn, "Failure")
    else:
        # send a message back to the microservice
        send_msg(conn, "Command not found")


def main():
    # Configure a socket object to use IPv4 and TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
        # Connect to the server
        conn.connect((IP, int(FPORT)))

        test_ms_call(conn)


# Run the `main()` function
if __name__ == "__main__":
    main()
