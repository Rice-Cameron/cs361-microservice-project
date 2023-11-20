# Cameron Rice
# ricecam@oregonstate.edu
import Database


class CodeSnippet(Database):
    def __init__(self, snippet_id, title, language, content, tags=None):
        self.snippet_id = snippet_id
        self.title = title
        self.language = language
        self.content = content
        self.tags = tags if tags is not None else []
        super().__init__(self)
        # add self to code_snippets from Database
        self.add_snippet()

    def __str__(self):
        return f"ID: {self.snippet_id}\nTitle: {self.title}\nLanguage: {self.language}\nContent: {self.content}\nTags: {', '.join(self.tags)}"

    def add_tag(self, tag):
        self.tags.append(tag)

    def remove_tag(self, tag):
        if tag in self.tags:
            self.tags.remove(tag)

    def edit_title(self, title):
        self.title = title

    def edit_language(self, language):
        self.language = language

    def edit_content(self, content):
        self.content = content

    def edit_tags(self, tags):
        self.tags = tags

    def get_snippet_id(self):
        return self.snippet_id

    def get_title(self):
        return self.title

    def get_language(self):
        return self.language

    def get_content(self):
        return self.content

    def get_tags(self):
        return self.tags

    def get_snippet(self):
        return self.snippet_id, self.title, self.language, self.content, self.tags
