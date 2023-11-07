# Cameron Rice
# ricecam@oregonstate.edu

import json


class Database:
    code_snippets = {}

    def __init__(self):
        # open snippet.json
        # save data to dict
        with open("snippet.json", "r") as f:
            self.code_snippets = json.load(f)

    def add_snippet(self):
        # Database.code_snippets[Snippet.snippet_id] = self
        print("== Adding snippet to database")
        # store self in code_snippets
        # append to snippet.json
        with open("snippet.json", "a") as f:
            json.dump(self, f)

    def delete_snippet(self):
        # del Database.code_snippets[Snippet.get_snippet_id(id)]
        print("== Deleting snippet from database")
        with open("snippet.json", "r") as f:
            code_dict = json.load(f)
            del code_dict[self]
        with open("snippet.json", "w") as f:
            json.dump(code_dict, f)

    def get_snippet(self, id):
        # return Database.code_snippets[Snippet.get_snippet_id(id)]
        print("== Getting snippet from database")
        with open("snippet.json", "r") as f:
            code_dict = json.load(f)
            return code_dict[id]

    def delete_all(self):
        # Database.code_snippets.clear()
        print("== Deleting all snippets from database")
        with open("snippet.json", "w") as f:
            f.write("{}")


    def get_length(self):
        with open("snippet.json", "r") as f:
            code_dict = json.load(f)
            return len(code_dict)

    def get_all(self):
        # return json dump
        with open("snippet.json", "r") as f:
            code_dict = json.load(f)
            return json.dumps(code_dict)