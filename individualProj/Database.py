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

    def delete_snippet(self, snippet_id):
        # del Database.code_snippets[Snippet.get_snippet_id(id)]
        print("== Deleting snippet from database")
        with open("snippet.json", "r") as f:
            code_dict = json.load(f)
            del code_dict[snippet_id]
        with open("snippet.json", "w") as f:
            json.dump(code_dict, f)

    def get_snippet(self, snippet_id):
        # return Database.code_snippets[Snippet.get_snippet_id(id)]
        print("== Getting snippet from database")
        with open("snippet.json", "r") as f:
            code_dict = json.load(f)
            return code_dict[snippet_id]

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

    def export_all(self, filename):
        # export all snippets to file named filename
        print("== Exporting all snippets to file")
        with open(filename, "w") as f:
            json.dump(self.code_snippets, f)

    def search_snippets(self, search_option, search_value):
        matching_snippets = {}
        with open("snippet.json", "r") as f:
            code_dict = json.load(f)
            for snippet_id, snippet in code_dict.items():
                if snippet[search_option] == search_value:
                    matching_snippets[snippet_id] = snippet
        return matching_snippets

    def add_tag(self, snippet_id, tag):
        with open("snippet.json", "r") as f:
            code_dict = json.load(f)
            snippet = code_dict[str(snippet_id)]
            if 'tags' in snippet:
                snippet['tags'].append(tag)
            else:
                snippet['tags'] = [tag]
        with open("snippet.json", "w") as f:
            json.dump(code_dict, f)

    def export_snippet(self, snippet_id, filename):
        with open("snippet.json", "r") as f:
            code_dict = json.load(f)
            snippet = code_dict[str(snippet_id)]
        with open(filename, "w") as f:
            json.dump(snippet, f)

    def import_snippet(self, filename):
        with open(filename, "r") as f:
            snippet = json.load(f)
        snippet_id = self.get_length() + 1
        with open("snippet.json", "r") as f:
            code_dict = json.load(f)
        code_dict[str(snippet_id)] = snippet
        with open("snippet.json", "w") as f:
            json.dump(code_dict, f)