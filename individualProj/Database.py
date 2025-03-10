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
        # Update the snippet_id of the remaining snippets
        new_code_dict = {str(i + 1): snippet for i, snippet in enumerate(code_dict.values())}
        with open("snippet.json", "w") as f:
            json.dump(new_code_dict, f)

    def search_snippets(self, search_option, search_value):
        matching_snippets = {}
        with open("snippet.json", "r") as f:
            code_dict = json.load(f)
            for snippet_id, snippet in code_dict.items():
                # Check if search_option is a valid key in the snippet dictionary
                if search_option in snippet:
                    if search_option == 'tags':
                        # If search_option is 'tags', iterate over each tag in the list
                        for tag in snippet[search_option]:
                            if tag.lower() == search_value.lower():
                                matching_snippets[snippet_id] = snippet
                                break
                    elif snippet[search_option].lower() == search_value.lower():
                        matching_snippets[snippet_id] = snippet
        return matching_snippets

    def add_tag(self, snippet_id, tag):
        with open("snippet.json", "r") as f:
            code_dict = json.load(f)
            snippet = code_dict[str(snippet_id)]
            if 'tags' in snippet:
                # Ensure that tags is a list before appending
                if isinstance(snippet['tags'], list):
                    snippet['tags'].append(tag)
                else:
                    snippet['tags'] = [snippet['tags'], tag]
            else:
                snippet['tags'] = [tag]
        with open("snippet.json", "w") as f:
            json.dump(code_dict, f)

    def export_snippet(self, snippet_id, filename):
        with open("snippet.json", "r") as f:
            code_dict = json.load(f)
            snippet = code_dict[str(snippet_id)]

        with open(filename, "w") as f:
            # Include the snippet_id in the exported object
            json.dump({snippet_id: snippet}, f)

    def import_snippet(self, filename):
        with open(filename, "r") as f:
            imported_snippets = json.load(f)

        with open("snippet.json", "r") as f:
            current_snippets = json.load(f)

        for snippet_id, snippet in imported_snippets.items():
            current_snippets[str(len(current_snippets) + 1)] = snippet

        with open("snippet.json", "w") as f:
            json.dump(current_snippets, f)

    def add_snippet(self, snippet):
        print("== Adding snippet to database")
        try:
            with open("snippet.json", "r") as f:
                code_dict = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            code_dict = {}
        snippet_id = str(len(code_dict) + 1)
        code_dict[snippet_id] = snippet
        with open("snippet.json", "w") as f:
            json.dump(code_dict, f)

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
        print("== Exporting all snippets to file")
        with open("snippet.json", "r") as f:
            code_dict = json.load(f)
        with open(filename, "w") as f:
            json.dump(code_dict, f)
