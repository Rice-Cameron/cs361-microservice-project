from Snippet import CodeSnippet as Snippet


class Database:
    code_snippets = {}

    def add_snippet(self):
        Database.code_snippets[Snippet.snippet_id] = self

    def delete_snippet(id):
        del Database.code_snippets[Snippet.get_snippet_id(id)]

    def get_snippet(id):
        return Database.code_snippets[Snippet.get_snippet_id(id)]

    def delete_all(self):
        Database.code_snippets.clear()