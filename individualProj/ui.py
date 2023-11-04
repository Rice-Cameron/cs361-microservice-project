# Cameron Rice
# ricecam@oregonstate.edu

# About: UI - Main Menu, Help Menu, Exit Menu
#        "Called" by microservice after user auth is verified
#        sockets will be used to communicate with microservice

import sys
import socket

IP, DPORT = 'localhost', 8080


def to_hex(number):
    assert number <= 0xffffffff, "Number too large to convert to hex"
    return "{:08x}".format(number)


def send_to_microservice(command):
    # send command to microservice via socket
    # for now, just show that the command is making it to this function which will then somehow
    # send it to the microservice in which will figure out what file to open and what function to call
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
        conn.connect((IP, int(DPORT)))
        print(f"== Sending {command} to microservice")
        conn.sendall(to_hex(len(command)).encode())
        conn.sendall(command.encode())


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
    print("Welcome to Code Snippet Manager CLI")
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
    "add": lambda: send_to_microservice("add"),
    "view": lambda: send_to_microservice("view"),
    "edit": lambda: send_to_microservice("edit"),
    "delete": lambda: send_to_microservice("delete"),
    "search": lambda: send_to_microservice("search"),
    "tag": lambda: send_to_microservice("tag"),
    "export": lambda: send_to_microservice("export"),
    "import": lambda: send_to_microservice("import"),
    "help": show_help_menu,
    "exit": exit_program
}


def main():
    display_main_menu()
    while True:
        user_input = input("\nEnter a command: ")

        if user_input in command_functions:
            command_functions[user_input]()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
