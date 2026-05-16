import json

class Indexer:
    def __init__(self):
        self.index = {}

    def stripText(self, text):
        # Keep only letters, numbers and spaces
        words = []
        cur = ""

        for char in text.lower():
            if char.isalnum():  # Checks if character is a letter or number
                cur += char
            else:
                if cur:
                    words.append(cur)
                    cur = ""
        if cur:
            words.append(cur)

        return words

    def makeIndex(self, content):
        self.index = {}
        for url, text in content.items():
            words = self.stripText(text)
            for position, word in enumerate(words):
                if word not in self.index:
                    self.index[word] = {}
                if url not in self.index[word]:
                    self.index[word][url] = {"freq": 0, "positions": []}
                
                self.index[word][url]["freq"] += 1
                self.index[word][url]["positions"].append(position)
        return self.index

    def save(self, filepath):
        # Save complete index to JSON file
        with open(filepath, 'w', encoding = 'utf-8') as file:
            json.dump(self.index, file, indent = 4)

    def load(self, filepath):
        # Load up existing index from file
        with open(filepath, 'r', encoding = 'utf-8') as file:
            self.index = json.load(file)