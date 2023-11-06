# Cameron Rice
# ricecam@oregonstate.edu

from send_recv import send_data, recv_data, to_hex

import socket
from Database import Database
from Snippet import CodeSnippet as Snippet

IP, DPORT = 'localhost', 8080


def add_code_snippet():
    print("-----------------------------------------------")
    print("Add New Code Snippet")
    print("-----------------------------------------------")
    snippet = Snippet()
    snippet.snippet_id = len(Database.code_snippets) + 1
    snippet.title = input("== Title: ")
    snippet.language = input("== Language: ")
    snippet.content = input("== Content: ")
    snippet.tags = input("== Tags: ")
    Database.add_snippet(snippet)
    # send success message to microservice
    send_data(to_hex(f"Code snippet {snippet.snippet_id} added successfully!"))


def view_code_snippets():
    print("-----------------------------------------------")
    print("List of Code Snippets")
    print("-----------------------------------------------")
    for snippet in Database.code_snippets:
        print(f"== {snippet.snippet_id}: {snippet.title} [{snippet.language}]")
    print("-----------------------------------------------")
    print("Select a Code Snippet to View")
    print("-----------------------------------------------")
    snippet_id = int(input("== Snippet ID: "))
    snippet = Database.get_snippet(snippet_id)
    # send snippet to microservice
    send_data(to_hex(snippet))
    # print("-----------------------------------------------")
    # print(f"== {snippet.title} [{snippet.language}]")
    # print("-----------------------------------------------")
    # print(snippet.content)
    # print("-----------------------------------------------")
    # print(f"Tags: {snippet.tags}")
    # print("-----------------------------------------------")


def edit_code_snippet():
    print("-----------------------------------------------")
    print("Edit Code Snippet")
    print("-----------------------------------------------")
    print("Select a Code Snippet to Edit")
    print("-----------------------------------------------")
    snippet_id = int(input("== Snippet ID: "))
    snippet = Database.get_snippet(snippet)
    print("-----------------------------------------------")
    print(f"== {snippet.title} [{snippet.language}]")
    print("-----------------------------------------------")
    print(snippet.content)
    print("-----------------------------------------------")
    print(f"Tags: {snippet.tags}")
    print("-----------------------------------------------")
    print("Edit Menu")
    print("-----------------------------------------------")
    print("[1] Edit Title")
    print("[2] Edit Language")
    print("[3] Edit Content")
    print("[4] Edit Tags")
    print("[5] Return to Main Menu")
    print("-----------------------------------------------")
    edit_choice = int(input("== Select an option: "))
    if edit_choice == 1:
        print("-----------------------------------------------")
        new_title = input("== Enter a new title: ")
        snippet.title = new_title
        print("-----------------------------------------------")
        print(f"== {snippet.title} [{snippet.language}]")
        print("-----------------------------------------------")
        print(snippet.content)
        print("-----------------------------------------------")
        print(f"Tags: {snippet.tags}")
        print("-----------------------------------------------")
        print("Edit Menu")
        print("-----------------------------------------------")
        print("[1] Edit Title")
        print("[2] Edit Language")
        print("[3] Edit Content")
        print("[4] Edit Tags")
        print("[5] Return to Main Menu")
        print("-----------------------------------------------")
        edit_choice = int(input("== Select an option: "))
    elif edit_choice == 2:
        print("-----------------------------------------------")
        new_language = input("== Enter a new language: ")
        snippet.language = new_language
        print("-----------------------------------------------")
        print(f"== {snippet.title} [{snippet.language}]")
        print("-----------------------------------------------")
        print(snippet.content)
        print("-----------------------------------------------")
        print(f"Tags: {snippet.tags}")
        print("-----------------------------------------------")
        print("Edit Menu")
        print("-----------------------------------------------")
        print("[1] Edit Title")
        print("[2] Edit Language")
        print("[3] Edit Content")
        print("[4] Edit Tags")
        print("[5] Return to Main Menu")
        print("-----------------------------------------------")
        edit_choice = int(input("== Select an option: "))
    elif edit_choice == 3:
        print("-----------------------------------------------")
        new_content = input("== Enter new content: ")
        snippet.content = new_content
        print("-----------------------------------------------")
        print(f"== {snippet.title} [{snippet.language}]")
        print("-----------------------------------------------")
        print(snippet.content)
        print("-----------------------------------------------")
        print(f"Tags: {snippet.tags}")
        print("-----------------------------------------------")
        print("Edit Menu")
        print("-----------------------------------------------")
        print("[1] Edit Title")
        print("[2] Edit Language")
        print("[3] Edit Content")
        print("[4] Edit Tags")
        print("[5] Return to Main Menu")
        print("-----------------------------------------------")
        edit_choice = int(input("== Select an option: "))
    elif edit_choice == 4:
        print("-----------------------------------------------")
        new_tags = input("== Enter new tags: ")
        snippet.tags = new_tags
        print("-----------------------------------------------")
        print(f"== {snippet.title} [{snippet.language}]")
        print("-----------------------------------------------")
        print(snippet.content)
        print("-----------------------------------------------")
        print(f"Tags: {snippet.tags}")
        print("-----------------------------------------------")
        print("Edit Menu")
        print("-----------------------------------------------")
        print("[1] Edit Title")
        print("[2] Edit Language")
        print("[3] Edit Content")
        print("[4] Edit Tags")
        print("[5] Return to Main Menu")
        print("-----------------------------------------------")
        edit_choice = int(input("== Select an option: "))
    elif edit_choice == 5:
        print("-----------------------------------------------")
        print("Returning to Main Menu")
        print("-----------------------------------------------")
        # send message to microservice to reprint main menu in ui.py
        send_data(to_hex("Returning to Main Menu"))


def delete_code_snippet():
    print("-----------------------------------------------")
    print("Delete Code Snippet")
    print("-----------------------------------------------")
    print("Select a Code Snippet to Delete or delete all")
    print("-----------------------------------------------")
    print("[1] Delete All")
    print("[2] Delete One")
    print("[3] Return to Main Menu")
    print("-----------------------------------------------")
    delete_choice = int(input("== Select an option: "))
    if delete_choice == 1:
        print("-----------------------------------------------")
        print("Are you sure you want to delete all code snippets?")
        print("-----------------------------------------------")
        print("[1] Yes")
        print("[2] No")
        print("-----------------------------------------------")
        delete_choice = int(input("== Select an option: "))
        if delete_choice == 1:
            Database.delete_all()
            print("-----------------------------------------------")
            print("All code snippets deleted successfully!")
            print("-----------------------------------------------")
            # send message to microservice to reprint main menu in ui.py
            send_data(to_hex("All code snippets deleted successfully!"))
        elif delete_choice == 2:
            print("-----------------------------------------------")
            print("Returning to Main Menu")
            print("-----------------------------------------------")
            # send message to microservice to reprint main menu in ui.py
            send_data(to_hex("Returning to Main Menu"))
    elif delete_choice == 2:
        print("-----------------------------------------------")
        print("Select a Code Snippet to Delete")
        print("-----------------------------------------------")
        snippet_id = int(input("== Snippet ID: "))
        Database.delete_snippet(snippet_id)
        print("-----------------------------------------------")
        print("Code snippet deleted successfully!")
        print("-----------------------------------------------")
        # send message to microservice to reprint main menu in ui.py
        send_data(to_hex("Code snippet deleted successfully!"))
    elif delete_choice == 3:
        print("-----------------------------------------------")
        print("Returning to Main Menu")
        print("-----------------------------------------------")
        # send message to microservice to reprint main menu in ui.py
        send_data(to_hex("Returning to Main Menu"))
    else:
        print("-----------------------------------------------")
        print("Invalid option selected, returning to main menu")
        print("-----------------------------------------------")
        # send message to microservice to reprint main menu in ui.py
        send_data(to_hex("Invalid option selected, returning to main menu"))





