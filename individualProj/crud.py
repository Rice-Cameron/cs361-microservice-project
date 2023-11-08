# Cameron Rice
# ricecam@oregonstate.edu

from send_recv import send_data, recv_data, to_hex

import socket
import json
from Database import Database
from Snippet import CodeSnippet as Snippet

IP, DPORT = 'localhost', 8080

# initialize database
db = Database()


def add_code_snippet():
    print("-----------------------------------------------")
    print("Add New Code Snippet")
    print("-----------------------------------------------")
    snippet_id = len(Database.get_length(db)) + 1
    title = input("== Title: ")
    language = input("== Language: ")
    content = input("== Content: ")
    tags = input("== Tags: ")
    snippet_string = ('{"snippet_id": ' + str(snippet_id) + ', "title": "' + title + '", "language": "' + language +
                      '", "content": "' + content + '", "tags": "' + tags + '"}')
    snippet = json.loads(snippet_string)
    Database.add_snippet(snippet)
    # send success message to microservice
    # send_data(to_hex(f"Code snippet {snippet.snippet_id} added successfully!"))


def view_code_snippets():
    print("-----------------------------------------------")
    print("List of Code Snippets")
    print("-----------------------------------------------")
    # ask user if they would like to view all or just one
    print("View:")
    print("[1] All")
    print("[2] One")
    print("[3] Return to Main Menu")
    print("-----------------------------------------------")
    view_choice = int(input("== Select an option: "))
    if view_choice == 1:
        # print contents from snippet.json
        snippets = Database.get_all(db)
        db.code_snippets = snippets
        for snippet in db.code_snippets:
            print(f"== {snippet.title} [{snippet.language}]")
            print("-----------------------------------------------")
            print(snippet.content)
            print("-----------------------------------------------")
            print(f"Tags: {snippet.tags}")
            print("-----------------------------------------------")
    elif view_choice == 2:
        print("-----------------------------------------------")
        print("Enter the ID of the Code Snippet You Would Like to View")
        print("-----------------------------------------------")
        snippet_id = int(input("== Snippet ID: "))
        # return the snippet object with the given id
        snippet = Database.get_snippet(db, snippet_id)
        print("-----------------------------------------------")
        print(f"== {snippet.title} [{snippet.language}]")
        print("-----------------------------------------------")
        print(snippet.content)
        print("-----------------------------------------------")
        print(f"Tags: {snippet.tags}")
        print("-----------------------------------------------")
    elif view_choice == 3:
        print("-----------------------------------------------")
        print("Returning to Main Menu")
        print("-----------------------------------------------")
        # send message to microservice to reprint main menu in ui.py
        # send_data(to_hex("Returning to Main Menu"))
    # confirm to microservice


def edit_code_snippet():
    print("-----------------------------------------------")
    print("Edit Code Snippet")
    print("-----------------------------------------------")
    print("Select a Code Snippet to Edit")
    print("-----------------------------------------------")
    snippet_id = int(input("== Snippet ID: "))
    # return the snippet object with the given id
    snippet = Database.get_snippet(db, snippet_id)
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
        db.code_snippets[snippet_id] = snippet
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
        db.code_snippets[snippet_id] = snippet
        print("-----------------------------------------------")
        print(f"== {snippet.title} [{snippet.language}]")
        print("-----------------------------------------------")
        print(snippet.content)
        print("-----------------------------------------------")
        print(f"Tags: {snippet.tags}")
        print("Test tags")
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
        db.code_snippets[snippet_id] = snippet
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
        db.code_snippets[snippet_id] = snippet
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
        # send_data(to_hex("Returning to Main Menu"))
    # update changes to snippet.json
    with open("snippet.json", "w") as f:
        json.dump(db.code_snippets, f)


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
            db.delete_all()
            print("-----------------------------------------------")
            print("All code snippets deleted successfully!")
            print("-----------------------------------------------")
            # send message to microservice to reprint main menu in ui.py
            # send_data(to_hex("All code snippets deleted successfully!"))
        elif delete_choice == 2:
            print("-----------------------------------------------")
            print("Returning to Main Menu")
            print("-----------------------------------------------")
            # send message to microservice to reprint main menu in ui.py
            # send_data(to_hex("Returning to Main Menu"))
    elif delete_choice == 2:
        print("-----------------------------------------------")
        print("Select a Code Snippet to Delete")
        print("-----------------------------------------------")
        snippet_id = int(input("== Snippet ID: "))
        db.delete_snippet(db, snippet_id)
        print("-----------------------------------------------")
        print("Code snippet deleted successfully!")
        print("-----------------------------------------------")
        # send message to microservice to reprint main menu in ui.py
        # send_data(to_hex("Code snippet deleted successfully!"))
    elif delete_choice == 3:
        print("-----------------------------------------------")
        print("Returning to Main Menu")
        print("-----------------------------------------------")
        # send message to microservice to reprint main menu in ui.py
        # send_data(to_hex("Returning to Main Menu"))
    else:
        print("-----------------------------------------------")
        print("Invalid option selected, returning to main menu")
        print("-----------------------------------------------")
        # send message to microservice to reprint main menu in ui.py
        # send_data(to_hex("Invalid option selected, returning to main menu"))


def main():
    print("Test")


if __name__ == "__main__":
    main()
