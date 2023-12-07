# Cameron Rice
# ricecam@oregonstate.edu

# About: Definitions for search, tag, export, and import
#        Defs used when "called' upon via microservice


from send_recv import send_data, recv_data
from Database import Database
from time import sleep
import socket
import json
import errno

IP, APORT = 'localhost', 8124

db = Database()


def process(conn):
    # Wait for the microservice to send a message
    data = recv_data(conn)
    print("Received:", data)
    # Tokenize and check first word of command
    cmd = data.split()[0]
    if cmd in routes:
        # call the function
        cmd_parts = data.split()
        if len(cmd_parts) > 2:
            res = routes[cmd_parts[0]](cmd_parts[1], cmd_parts[2])
        elif len(cmd_parts) > 1:
            res = routes[cmd_parts[0]](cmd_parts[1])
        else:
            res = routes[cmd_parts[0]]()
        print(f"== Result: {res}")
        # send the result back to the microservice
        sleep(5)
        send_data(conn, res)
    else:
        # send a message back to the microservice
        sleep(5)
        send_data(conn, "Command not found")


def search_code_snippet(search_option, search_value):
    if search_option in ['title', 'lang', 'content', 'tags']:
        # Search the database for the snippet
        snippets = Database.search_snippets(db, search_option, search_value)

        response = {
            "header": "Search Results",
            "snippets": [],
            "message": ""
        }

        for snippet_id, snippet in snippets.items():
            response["snippets"].append({
                "title": snippet["title"],
                "lang": snippet["lang"],
                "content": snippet["content"],
                "tags": snippet["tags"]
            })

        return f"{response['header']}\n" + "\n".join(
            [f"{snippet_id}. Title: {snippet['title']}, lang: {snippet['lang']}, Content:{snippet['content']}" for snippet_id, snippet
             in snippets.items()])
    else:
        return "Invalid search option"


def tag_code_snippet(snippet_id, tag):
    # Add the tag to the snippet in the database
    Database.add_tag(db, snippet_id, tag)
    return f"Tag {tag} added to snippet {snippet_id}"


def export_code_snippets(export_choice, filename):
    if export_choice == 'all':
        # Export all snippets from the database to a file
        Database.export_all(db, filename)
        return "All code snippets exported successfully"
    elif export_choice.isdigit():
        # Export the specified snippet from the database to a file
        snippet_id = int(export_choice)
        Database.export_snippet(db, snippet_id, filename)
        return f"Code snippet {snippet_id} exported successfully"
    else:
        return "Invalid export choice"

def import_code_snippets(filename):
    # Import snippets from the file to the database
    Database.import_snippet(db, filename)
    return f"Code snippets imported from {filename} successfully"


routes = {
    "search": search_code_snippet,
    "tag": tag_code_snippet,
    "export": export_code_snippets,
    "import": import_code_snippets
}


def main():
    # Configure a socket object to use IPv4 and TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
        conn.bind((IP, int(APORT)))
        conn.listen()
        print(f"== Adv Funcs listening on port {APORT}")
        while True:
            try:
                client_conn, addr = conn.accept()
                with client_conn:
                    print(f"== Received connection from {addr}")
                    client_conn.settimeout(10.0)
                    process(client_conn)
                print("== Connection closed, sleeping for 5 seconds")
                sleep(5)
            except socket.timeout:
                print("== Connection timed out")
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


# Run the `main()` function
if __name__ == "__main__":
    main()
