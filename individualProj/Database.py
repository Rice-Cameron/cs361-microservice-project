# Cameron Rice
# ricecam@oregonstate.edu

import json


class Database:
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

    def get_snippet(self):
        # return Database.code_snippets[Snippet.get_snippet_id(id)]
        print("== Getting snippet from database")
        with open("snippet.json", "r") as f:
            code_dict = json.load(f)
            return code_dict[self]

    def delete_all(self):
        # Database.code_snippets.clear()
        print("== Deleting all snippets from database")
        with open("snippet.json", "w") as f:
            f.write("{}")
