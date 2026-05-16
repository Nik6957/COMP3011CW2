import re

class Search:
    def __init__(self, indexer):
        self.indexer = indexer

    def printIndex(self, word):
        # Find the saved info on word from the index 
        word = word.lower().strip()
        return self.indexer.index.get(word, {})

    def findPhrase(self, phrase):
        query = []
        cur = ""
        
        for char in phrase.lower():
            if char.isalnum():
                cur += char
            else:
                if cur:
                    query.append(cur)
                    cur = ""
        if cur:
            query.append(cur)

        # Find what has the first word
        firstWord = query[0]
        if firstWord not in self.indexer.index:
            return []
            
        sameURL = set(self.indexer.index[firstWord].keys())

        # Match first word selection with selections of rest of search 
        for word in query[1:]:
            if word not in self.indexer.index:
                return []
            sameURL.intersection_update(self.indexer.index[word].keys())

        return list(sameURL)