# Cameron Rice
# ricecam@oregonstate.edu

# About: Definitions for search, tag, export, and import
#        Defs used when "called' upon via microservice


from send_recv import send_data, recv_data, to_hex
from Database import Database
from Snippet import CodeSnippet as Snippet

import socket
import Snippet
import Database
import io


def search_code_snippet():
    print("-----------------------------------------------")
    print("Search for Code Snippet")
    print("-----------------------------------------------")
    # Ask user what they would like to search by: title, lang, content, tag
    print("Search by:")
    print("1. Title")
    print("2. Language")
    print("3. Content")
    print("4. Tag")
    print("5. Return to Main Menu")
    print("-----------------------------------------------")
    search_choice = int(input("== Select an option: "))
    if search_choice == 1:
        print("-----------------------------------------------")
        search_title = input("== Enter a title to search for: ")
        # send title to microservice
        send_data(to_hex(search_title))
        # receive snippet from microservice
        snippet = recv_data()
        print("-----------------------------------------------")
        print(f"== {snippet.title} [{snippet.language}]")
        print("-----------------------------------------------")
        print(snippet.content)
        print("-----------------------------------------------")
        print(f"Tags: {snippet.tags}")
        print("-----------------------------------------------")
    elif search_choice == 2:
        print("-----------------------------------------------")
        search_lang = input("== Enter a language to search for: ")
        # send lang to microservice
        send_data(to_hex(search_lang))
        # receive snippet from microservice
        snippet = recv_data()
        print("-----------------------------------------------")
        print(f"== {snippet.title} [{snippet.language}]")
        print("-----------------------------------------------")
        print(snippet.content)
        print("-----------------------------------------------")
        print(f"Tags: {snippet.tags}")
        print("-----------------------------------------------")
    elif search_choice == 3:
        print("-----------------------------------------------")
        search_content = input("== Enter content to search for: ")
        # send content to microservice
        send_data(to_hex(search_content))
        # receive snippet from microservice
        snippet = recv_data()
        print("-----------------------------------------------")
        print(f"== {snippet.title} [{snippet.language}]")
        print("-----------------------------------------------")
        print(snippet.content)
        print("-----------------------------------------------")
        print(f"Tags: {snippet.tags}")
        print("-----------------------------------------------")
    elif search_choice == 4:
        print("-----------------------------------------------")
        search_tag = input("== Enter a tag to search for: ")
        # send tag to microservice
        send_data(to_hex(search_tag))
        # receive snippet from microservice
        snippet = recv_data()
        print("-----------------------------------------------")
        print(f"== {snippet.title} [{snippet.language}]")
        print("-----------------------------------------------")
        print(snippet.content)
        print("-----------------------------------------------")
        print(f"Tags: {snippet.tags}")
        print("-----------------------------------------------")
    elif search_choice == 5:
        print("-----------------------------------------------")
        print("Returning to Main Menu")
        print("-----------------------------------------------")
        # send main menu request to microservice
        send_data(to_hex("Returning to Main Menu"))
    else:
        print("-----------------------------------------------")
        print("Invalid input, please try again")
        print("-----------------------------------------------")
        # send invalid input to microservice
        send_data(to_hex("Invalid input, please try again"))


def tag_code_snippet():
    print("-----------------------------------------------")
    print("Tag Code Snippet")
    print("-----------------------------------------------")
    # Ask user what keyword they would like to tag the snippet with, only accept one word tags
    # What snippet would you like to add a tag to?
    # Please enter the id of the snippet you would like to add a tag to:
    id = input("== Enter the id of the snippet you would like to add a tag to: ")
    # What tag would you like to add to the snippet?
    tag = input("== Enter the tag you would like to add to the snippet: ")
    # send id and tag to microservice
    send_data(to_hex(id))
    send_data(to_hex(tag))
    # receive confirmation from microservice
    confirmation = recv_data()
    print("-----------------------------------------------")
    print(confirmation)
    print("-----------------------------------------------")


def export_code_snippets():
    print("-----------------------------------------------")
    print("Export Code Snippets")
    print("-----------------------------------------------")
    print("Would you like to export all snippets or a specific snippet?")
    print("1. All snippets")
    print("2. Specific snippet")
    print("3. Return to Main Menu")
    print("-----------------------------------------------")
    export_choice = int(input("== Select an option: "))
    if export_choice == 1:
        # Ask if the user is sure they want to export all snippets
        print("-----------------------------------------------")
        print("Are you sure you want to export all snippets?")
        print("1. Yes")
        print("2. No")
        print("-----------------------------------------------")
        export_all_choice = int(input("== Select an option: "))
        if export_all_choice == 1:
            # send export all request to microservice
            send_data(to_hex("Export all"))
            # receive confirmation from microservice
            confirmation = recv_data()
            print("-----------------------------------------------")
            print(confirmation)
            print("-----------------------------------------------")
        elif export_all_choice == 2:
            print("-----------------------------------------------")
            print("Returning to Export Code Snippets Menu")
            print("-----------------------------------------------")
            # send return to export menu request to microservice
            send_data(to_hex("Returning to Export Code Snippets Menu"))
        else:
            print("-----------------------------------------------")
            print("Invalid input, please try again")
            print("-----------------------------------------------")
            # send invalid input to microservice
            send_data(to_hex("Invalid input, please try again"))
    elif export_choice == 2:
        # Ask user what snippet they would like to export
        print("-----------------------------------------------")
        export_id = input("== Enter the id of the snippet you would like to export: ")
        # send export id to microservice
        send_data(to_hex(export_id))
        # receive confirmation from microservice
        confirmation = recv_data()
        print("-----------------------------------------------")
        print(confirmation)
        print("-----------------------------------------------")
    elif export_choice == 3:
        print("-----------------------------------------------")
        print("Returning to Main Menu")
        print("-----------------------------------------------")
        # send main menu request to microservice
        send_data(to_hex("Returning to Main Menu"))
    else:
        print("-----------------------------------------------")
        print("Invalid input, please try again")
        print("-----------------------------------------------")
        # send invalid input to microservice
        send_data(to_hex("Invalid input, please try again"))


def import_code_snippets():
    print("-----------------------------------------------")
    print("Import Code Snippets")
    print("-----------------------------------------------")
    print("Before you proceed, make sure the file you are attempting to import follows the following requirements: ")
    print("1. The file must be in your current working directory")
    print("2. The file must be formatted as such: id,title,language,content,tags;(second snippet;(third snippet);")
    print("Note: Each snippet must be delimited by a semicolon (;) and the attributes are separated by a comma (,)")
    print("-----------------------------------------------")
    print("Please enter the file name of the file you would like to import:")
    file_name = input("== Enter the file name: ")
    # open file and read info
    with open(file_name, "r") as file:
        data = file.read()
        # file formatted as id, title, language, content, tags, delimited with ;
        # Package all of the snippets in a dictionary and send to microservice
        send_data(to_hex(data))
        # receive confirmation from microservice
        confirmation = recv_data()
        print("-----------------------------------------------")
        print(confirmation)
        print("-----------------------------------------------")
