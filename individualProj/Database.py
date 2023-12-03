# Cameron Rice
# ricecam@oregonstate.edu

import json


class Database:
    code_snippets = dict()

    def __init__(self):
        try:
            with open("snippet.json", "r") as f:
                self.code_snippets = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.code_snippets = {}
            with open("snippet.json", "w") as f:
                json.dump(self.code_snippets, f)

    def get_snippet(self, snippet_id):
        print("== Getting snippet from database")
        with open("snippet.json", "r") as f:
            code_dict = json.load(f)
            return code_dict[str(snippet_id)]

    def delete_snippet(self, snippet_id):
        print("== Deleting snippet from database")
        with open("snippet.json", "r") as f:
            code_dict = json.load(f)
            del code_dict[str(snippet_id)]
        with open("snippet.json", "w") as f:
            json.dump(code_dict, f)

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
        snippet_id = str(self.get_length() + 1)
        with open("snippet.json", "r") as f:
            code_dict = json.load(f)
        code_dict[snippet_id] = snippet
        with open("snippet.json", "w") as f:
            json.dump(code_dict, f)

    def add_snippet(self, snippet):
        print("== Adding snippet to database")
        with open("snippet.json", "r") as f:
            code_dict = json.load(f)
        code_dict[str(len(code_dict) + 1)] = snippet
        with open("snippet.json", "w") as f:
            json.dump(code_dict, f)

    # def delete_snippet(self, snippet_id):
    #     # del Database.code_snippets[Snippet.get_snippet_id(id)]
    #     print("== Deleting snippet from database")
    #     with open("snippet.json", "r") as f:
    #         code_dict = json.load(f)
    #         del code_dict[snippet_id]
    #     with open("snippet.json", "w") as f:
    #         json.dump(code_dict, f)

    # def get_snippet(self, snippet_id):
    #     # return Database.code_snippets[Snippet.get_snippet_id(id)]
    #     print("== Getting snippet from database")
    #     with open("snippet.json", "r") as f:
    #         code_dict = json.load(f)
    #         return code_dict[snippet_id]

    def delete_all(self):
        # Database.code_snippets.clear()
        print("== Deleting all snippets from database")
        with open("snippet.json", "w") as f:
            f.write("{}")

    def get_length(self):
        with open("snippet.json", "r") as f:
            code_dict = json.load(f)
            snippet_count = sum(1 for item in code_dict.values() if isinstance(item, dict))
            return snippet_count

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

    # def search_snippets(self, search_option, search_value):
    #     matching_snippets = {}
    #     with open("snippet.json", "r") as f:
    #         code_dict = json.load(f)
    #         for snippet_id, snippet in code_dict.items():
    #             if snippet[search_option] == search_value:
    #                 matching_snippets[snippet_id] = snippet
    #     return matching_snippets

    # def add_tag(self, snippet_id, tag):
    #     with open("snippet.json", "r") as f:
    #         code_dict = json.load(f)
    #         snippet = code_dict[str(snippet_id)]
    #         if 'tags' in snippet:
    #             snippet['tags'].append(tag)
    #         else:
    #             snippet['tags'] = [tag]
    #     with open("snippet.json", "w") as f:
    #         json.dump(code_dict, f)
    #
    # def export_snippet(self, snippet_id, filename):
    #     with open("snippet.json", "r") as f:
    #         code_dict = json.load(f)
    #         snippet = code_dict[str(snippet_id)]
    #     with open(filename, "w") as f:
    #         json.dump(snippet, f)
    #
    # def import_snippet(self, filename):
    #     with open(filename, "r") as f:
    #         snippet = json.load(f)
    #     snippet_id = self.get_length() + 1
    #     with open("snippet.json", "r") as f:
    #         code_dict = json.load(f)
    #     code_dict[str(snippet_id)] = snippet
    #     with open("snippet.json", "w") as f:
    #         json.dump(code_dict, f)