# Cameron Rice
# ricecam@oregonstate.edu

# About: UI - Main Menu, Help Menu, Exit Menu
#        "Called" by microservice after user auth is verified
#        sockets will be used to communicate with microservice

from send_recv import send_data, recv_data

import socket
import Database
import sys
import os
import json
from time import sleep
import errno

IP, MPORT = 'localhost', 8000


def show_help_menu():
    print("-----------------------------------------------")
    print("Help Menu")
    print("-----------------------------------------------")

    help_text = {
        "add": "Add a New Code Snippet\n"
               "This command allows you to add a new code snippet. You will be prompted to enter the title, language, "
               "and content of the snippet.",

        "view all": "View List of all Code Snippets\n"
                    "This command displays a list of all existing code snippets",

        "view <id>": "View Details of a Code Snippet\n"
                     "This command allows you to view the details of a specific code snippet by entering its ID.",

        "edit": "Edit an Existing Code Snippet\n"
                "This command lets you edit an existing code snippet by giving it the id of the snippet to edit. You "
                "can select a snippet to modify its title,"
                "language, content, or tags.",

        "delete": "Delete a Code Snippet\n"
                  "This command allows you to permanently delete a code snippet from the list.",

        "search": "Search for a Code Snippet\n"
                  "This command enables you to search for code snippets using keywords or tags. Matching snippets "
                  "will be displayed.",

        "tag": "Add Tags to a Code Snippet\n"
               "This command allows you to add tags to a code snippet. Tags help you categorize and organize your "
               "snippets.",

        "export": "Export Code Snippets to a File\n"
                  "This command lets you save your code snippets to a file for backup or sharing with others.",

        "import": "Import Code Snippets from a File\n"
                  "This command allows you to load code snippets from a previously exported file.",

        "help": "Show Help Menu\n"
                "This command displays a detailed help menu providing explanations for each available command.",

        "exit": "Exit the Program\n"
                "This command terminates the Code Snippet Manager CLI application."
    }

    for command, description in help_text.items():
        print(f"\n[{command}]")
        print(description)

    input("\nPress Enter to return to the main menu.")
    display_main_menu()


def exit_program():
    print("Exiting the program. Goodbye!")
    sys.exit()


def display_main_menu():
    print("-----------------------------------------------")
    print("Welcome to Code Saver CLI: A Minimal Code Snippet Manager")
    print("-----------------------------------------------")
    print("\nAvailable Commands:")
    print("- add                                                Add a new code snippet")
    print("- view all                                           View list of all code snippets")
    print("- view <id>                                          View details of a code snippet")
    print("- edit <id> <title, lang, content, tags> <value>     Edit an existing code snippet")
    print("- delete <all, id>                                   Delete all code snippets or just one")
    print("- search <title, lang, content, tag> <value>         Search for a code snippet by passing the option and its value")
    print("- tag <id> <tag>                                     sAdd tags to a code snippet")
    print("- export <all, id> <filename>                        Export code snippets to a file")
    print("- import <filename>                                  Import code snippets from a file")
    print("- help                                               Show help menu")
    print("- exit                                               Exit the program")


def get_add_args():
    title = input("Enter the title of the snippet: ")
    lang = input("Enter the language of the snippet: ")
    content = input("Enter the content of the snippet: ")

    payload = {
        "title": title,
        "lang": lang,
        "content": content
    }

    return payload


def main():
    db = Database
    if not os.path.isfile("snippet.json"):
        with open("snippet.json", "w") as f:
            f.write("{}")
    else:
        with open("snippet.json", "r") as f:
            data = f.read()
            if data:
                db.code_snippets = json.loads(data)

    display_main_menu()
    while True:
        cmd = input("Enter command: ")
        sleep(3)
        if cmd == "add":
            payload = get_add_args()
            cmd = {"cmd": "add", "payload": payload}
        elif cmd == "delete all":
            ans = input("Are you sure you want to delete all snippets? (y/n): ")
            if ans == "n":
                continue
        elif cmd == "help":
            show_help_menu()
            continue
        elif cmd == "exit":
            exit_program()

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
            try:
                conn.connect((IP, int(MPORT)))
                send_data(conn, cmd)
                sleep(5)
                res = recv_data(conn)
                print("== Result: \n", res)
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


if __name__ == "__main__":
    main()
