# Cameron Rice
# ricecam@oregonstate.edu

# NOT ACTUAL MICROSERVICE, JUST A TEST


from send_recv import send_data, recv_data, to_hex

import socket
import Snippet
import Database

INTERFACE, SPORT = 'localhost', 8080
CHUNK = 100


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as microservice_sock:
        microservice_sock.bind((INTERFACE, int(SPORT)))
        microservice_sock.listen()

        print(f"== Microservice listening on port {SPORT}")

        while True:
            conn, addr = microservice_sock.accept()
            with conn:
                print(f"== Received connection from {addr}")
                command = recv_data(conn)
                print(f"== Received command: {command}")
                send_data("test send")
                print(f"== Sent results to client")


if __name__ == "__main__":
    main()
