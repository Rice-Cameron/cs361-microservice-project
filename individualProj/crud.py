# Cameron Rice
# ricecam@oregonstate.edu

from send_recv import send_data, recv_data
from Database import Database
from time import sleep
import socket
import json
import errno

IP, CPORT = 'localhost', 8123

# initialize database
db = Database()


def process(conn):
    # Wait for the microservice to send a message
    data = recv_data(conn)
    print("Received:", data)

    if isinstance(data, dict) and "cmd" in data:
        cmd = data["cmd"]
        payload = data.get("payload", None)  # Optional, will be None if not provided
        if cmd == "add" and payload is not None:
            res = routes[cmd](payload)
            print(f"== Result: {res}")
            # send the result back to the microservice
            sleep(5)
            send_data(conn, res)
        else:
            # send a message back to the microservice
            sleep(5)
            send_data(conn, "Command not found")
    elif isinstance(data, str):
        cmd_parts = data.split()
        if cmd_parts[0] in routes:
            if len(cmd_parts) > 3:
                res = routes[cmd_parts[0]](cmd_parts[1], cmd_parts[2], cmd_parts[3])
            elif len(cmd_parts) > 2:
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


def add_code_snippet(payload):
    title = payload["title"]
    lang = payload["lang"]
    content = payload["content"]
    tags = payload.get("tags", "")  # Optional, will be an empty string if not provided
    snippet = {
        "title": title,
        "lang": lang,
        "content": content,
        "tags": tags
    }
    Database.add_snippet(db, snippet)
    snippet_id = Database.get_length(db)
    return f"Code snippet {snippet_id} added successfully!"


def view_code_snippets(arg=None):
    response = {
        "header": "List of Code Snippets",
        "snippets": [],
        "message": ""
    }

    if arg == "all":
        snippets = Database.get_all(db)
        db.code_snippets = json.loads(snippets)
        for snippet_id, snippet in db.code_snippets.items():
            response["snippets"].append({
                "title": snippet["title"],
                "lang": snippet["lang"],
                "content": snippet["content"],
                "tags": snippet["tags"]
            })
        return f"{response['header']}\n" + "\n".join(
            [f"{snippet_id}. Title: {snippet['title']}, Language: {snippet['lang']}, Content: {snippet['content']}" for snippet_id, snippet in
             db.code_snippets.items()])
    elif arg.isdigit():
        snippet_id = int(arg)
        snippet = Database.get_snippet(db, snippet_id)
        response["snippets"].append({
            "title": snippet["title"],
            "lang": snippet["lang"],
            "content": snippet["content"],
            "tags": snippet["tags"]
        })
        return f"{response['header']}\n" + "\n".join(
            [f"{snippet_id}. Title: {snippet['title']}, Language: {snippet['lang']}, Content:{snippet['content']}" for snippet_id, snippet in
             enumerate(response["snippets"])])

    else:
        response["message"] = "Invalid argument for view command"


def edit_code_snippet(snippet_id, edit_choice, new_value):
    snippet_id = int(snippet_id)
    snippet = Database.get_snippet(db, snippet_id)
    if edit_choice == 'title':
        snippet["title"] = new_value
    elif edit_choice == 'lang':
        snippet["lang"] = new_value
    elif edit_choice == 'content':
        snippet["content"] = new_value
    elif edit_choice == 'tags':
        snippet["tags"] = new_value
    db.code_snippets[str(snippet_id)] = snippet
    with open("snippet.json", "w") as f:
        json.dump(db.code_snippets, f)
    return f"Code snippet {snippet_id} edited successfully!"


def delete_code_snippet(delete_choice):
    if delete_choice == 'all':
        db.delete_all()
        return "All code snippets deleted successfully!"
    elif delete_choice.isdigit():
        snippet_id = int(delete_choice)
        db.delete_snippet(snippet_id)
        return f"Code snippet {snippet_id} deleted successfully!"

    return "Invalid option selected, returning to main menu"


routes = {
    "add": add_code_snippet,
    "view": view_code_snippets,
    "edit": edit_code_snippet,
    "delete": delete_code_snippet
}


def main():
    # Configure a socket object to use IPv4 and TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
        conn.bind((IP, int(CPORT)))
        conn.listen()
        print(f"== CRUD listening on port {CPORT}")
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


if __name__ == "__main__":
    main()
