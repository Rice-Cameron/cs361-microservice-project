# Cameron Rice
# ricecam@oregonstate.edu

import sys
import getpass
import hashlib

# Assuming you have a list to store code snippets
code_snippets = []


# def hash_pass(password):
#     sha256 = hashlib.sha256()
#     sha256.update(password.encode('utf-8'))
#     hashed_password = sha256.hexdigest()
#     return hashed_password


# def login():
#     username = input("Username: ")
#     password = getpass.getpass("Password: ")
#     return username, password


# def auth(username, password):
#     with open('users.txt', 'r') as file:
#         for line in file:
#             store_uname, store_pass = line.strip().split(':')
#             if username == store_uname and hash_pass(password) == store_pass:
#                 return True
#     return False


# def register():
#     username = input("New Username: ")
#     password = getpass.getpass("New Password: ")
#
#     # Hash the password before storing
#     hashed_password = hash_pass(password)
#
#     with open('users.txt', 'a') as file:
#         file.write(f'{username}:{hashed_password}\n')


def add_code_snippet():
    print("-----------------------------------------------")
    print("Add New Code Snippet")
    print("-----------------------------------------------")
    snippet_data = {"title": input("Enter a title: "), "language": input("Enter a language: "),
                    "content": input("Enter the content: ")}

    # Send to microservice


def view_code_snippets():
    print("-----------------------------------------------")
    print("List of Code Snippets")
    print("-----------------------------------------------")

    # Request microservice to get list of snippets


def edit_code_snippet():
    print("-----------------------------------------------")
    print("Edit Code Snippet")
    print("-----------------------------------------------")

    # Request microservice to open specific snippet and edit contents


def delete_code_snippet():
    print("-----------------------------------------------")
    print("Delete Code Snippet")
    print("-----------------------------------------------")

    # Request microservice to remove specific snippet


def search_code_snippet():
    print("-----------------------------------------------")
    print("Search for Code Snippet")
    print("-----------------------------------------------")

    # Request microservice to return specific snippet


def tag_code_snippet():
    print("-----------------------------------------------")
    print("Tag Code Snippet")
    print("-----------------------------------------------")


def export_code_snippets():
    print("-----------------------------------------------")
    print("Export Code Snippets")
    print("-----------------------------------------------")


def import_code_snippets():
    print("-----------------------------------------------")
    print("Import Code Snippets")
    print("-----------------------------------------------")


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
    "add": add_code_snippet,
    "view": view_code_snippets,
    "edit": edit_code_snippet,
    "delete": delete_code_snippet,
    "search": search_code_snippet,
    "tag": tag_code_snippet,
    "export": export_code_snippets,
    "import": import_code_snippets,
    "help": show_help_menu,
    "exit": exit_program
}


def main_menu():
    while True:
        display_main_menu()
        user_input = input("\nEnter a command: ")

        # Check if the user input is a valid command
        if user_input in command_functions:
            # Execute the corresponding function
            command_functions[user_input]()
        else:
            print("Invalid command. Please try again.")


def main():
    print("Welcome to Code Snippet Manager CLI")
    main_menu()
    # while True:
    #     username, password = login()
    #     if auth(username, password):
    #         print(f"Welcome, {username}!")

    # else:
    #     print("Invalid credentials. Please try again.")


if __name__ == '__main__':
    main()
