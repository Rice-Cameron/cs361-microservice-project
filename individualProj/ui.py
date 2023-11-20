# Cameron Rice
# ricecam@oregonstate.edu

# About: UI - Main Menu, Help Menu, Exit Menu
#        "Called" by microservice after user auth is verified
#        sockets will be used to communicate with microservice

from send_recv import send_data, recv_data, to_hex

import socket, Database, sys, os, io, json
from Snippet import CodeSnippet as Snippet


IP, DPORT = 'localhost', 8080


def show_help_menu():
    print("-----------------------------------------------")
    print("Help Menu")
    print("-----------------------------------------------")

    help_text = {
        "add": "Add a New Code Snippet\n"
               "This command allows you to add a new code snippet. You will be prompted to enter the title, language, "
               "and content of the snippet.",

        "view": "View List of Code Snippets\n"
                "This command displays a list of all existing code snippets. You can select a snippet to view its "
                "details.",

        "edit": "Edit an Existing Code Snippet\n"
                "This command lets you edit an existing code snippet. You can select a snippet to modify its title, "
                "language, and content.",

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
    print("- add          Add a new code snippet")
    print("- view         View list of code snippets")
    print("- edit         Edit an existing code snippet")
    print("- delete       Delete a code snippet")
    print("- search       Search for a code snippet")
    print("- tag          Add tags to a code snippet")
    print("- export       Export code snippets to a file")
    print("- import       Import code snippets from a file")
    print("- help         Show help menu")
    print("- exit         Exit the program")


# Define a dictionary mapping commands to their respective functions

command_functions = {
    "add": lambda: send_data("add"),
    "view": lambda: send_data("view"),
    "edit": lambda: send_data("edit"),
    "delete": lambda: send_data("delete"),
    "search": lambda: send_data("search"),
    "tag": lambda: send_data("tag"),
    "export": lambda: send_data("export"),
    "import": lambda: send_data("import"),
    "help": show_help_menu,
    "exit": exit_program
}


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
        user_input = input("\nEnter a command: ")

        if user_input in command_functions:
            command_functions[user_input]()
            # Sleep here?
            # recv_data()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
