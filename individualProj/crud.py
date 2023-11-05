# Cameron Rice
# ricecam@oregonstate.edu

from send_recv import send_data, recv_data, to_hex

import socket

IP, DPORT = 'localhost', 8080


def add_code_snippet():
    print("-----------------------------------------------")
    print("Add New Code Snippet")
    print("-----------------------------------------------")
    snippet_data = {"title": input("Enter a title: "), "language": input("Enter a language: "),
                    "content": input("Enter the content: ")}


def view_code_snippets():
    print("-----------------------------------------------")
    print("List of Code Snippets")
    print("-----------------------------------------------")


def edit_code_snippet():
    print("-----------------------------------------------")
    print("Edit Code Snippet")
    print("-----------------------------------------------")


def delete_code_snippet():
    print("-----------------------------------------------")
    print("Delete Code Snippet")
    print("-----------------------------------------------")



