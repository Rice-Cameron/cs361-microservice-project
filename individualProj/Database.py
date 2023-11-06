# Cameron Rice
# ricecam@oregonstate.edu

from Snippet import CodeSnippet as Snippet


class Database:
    code_snippets = {}

    def add_snippet(self):
        # Database.code_snippets[Snippet.snippet_id] = self
        print("== Adding snippet to database")

    def delete_snippet(id):
        # del Database.code_snippets[Snippet.get_snippet_id(id)]
        print("== Deleting snippet from database")

    def get_snippet(id):
        # return Database.code_snippets[Snippet.get_snippet_id(id)]
        print("== Getting snippet from database")

    def delete_all(self):
        # Database.code_snippets.clear()
        print("== Deleting all snippets from database")