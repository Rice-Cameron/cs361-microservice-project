# Cameron Rice
# ricecam@oregonstate.edu

# About: User authentication so that users can access
#           their snippets and only their snippets.

# TODO: Maybe use a database to be able to assocaiate users with specific
#           code snippets? Do via attaching an id to users and that same
#           id to the snippets that they create.


import getpass
import hashlib
import socket

IP, DPORT = 'localhost', 8080


def hash_pass(password):
    sha256 = hashlib.sha256()
    sha256.update(password.encode('utf-8'))
    hashed_password = sha256.hexdigest()
    return hashed_password


def login():
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    return username, password


def auth(username, password):
    with open('users.txt', 'r') as file:
        for line in file:
            store_uname, store_pass = line.strip().split(':')
            if username == store_uname and hash_pass(password) == store_pass:
                return True
    return False


def register():
    username = input("New Username: ")
    password = getpass.getpass("New Password: ")

    # Hash the password before storing
    hashed_password = hash_pass(password)

    with open('users.txt', 'a') as file:
        file.write(f'{username}:{hashed_password}\n')

def main():
    print("Welcome to Code Snippet Manager CLI")
    while True:
        username, password = login()
        if auth(username, password):
            print(f"Welcome, {username}!")

    else:
        print("Invalid credentials. Please try again.")


if __name__ == '__main__':
    main()
