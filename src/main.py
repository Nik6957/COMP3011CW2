import os
import json
from crawler import Crawler
from indexer import Indexer
from search import Search

filepath = os.path.join(os.path.dirname(__file__), '..', 'data', 'index.json')

def main():
    indexer = Indexer()
    search = Search(indexer)
    
    print("Web Crawler Search Tool")
    print("Options: Build(b) | Load(l) | Print a word(p) | Find a phrase(f) | Exit(e)\n")

    while True:
        try:
            inp = input("Select an option: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting tool.")
            break
        if not inp:
            continue

        inputParts = inp.split(maxsplit = 1)
        option = inputParts[0].lower()
        searchWords = inputParts[1] if len(inputParts) > 1 else ""

        if option == "b": # Build
            print("Starting the crawler.")
            crawler = Crawler()
            content = crawler.crawling()
            print(f"Crawled {len(content)} pages. Generating the index.")
            indexer.makeIndex(content)
            
            # Ensure data directory exists
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            indexer.save(filepath)
            print(f"Index written to {filepath} sucessfully.")

        elif option == "l": # Load
            if os.path.exists(filepath):
                indexer.load(filepath)
                print(f"Index loaded from {filepath} sucessfully.")
            else:
                print(f"Index file not found at {filepath}.")

        elif option == "p": # Print a word
            if not searchWords:
                print("Enter a word to print. Please select the option again.")
                continue
            wordInfo = search.printIndex(searchWords)
            if wordInfo:
                print(json.dumps(wordInfo, indent = 2))
            else:
                print(f"'{searchWords}' not found.")

        elif option == "f": # Find a word
            if not searchWords:
                print("Enter a word to find. Please select the option again.")
                continue
            results = search.findPhrase(searchWords)
            if results:
                print(f"{len(results)} page(s) with '{searchWords}': ")
                for url in results:
                    print(f" - {url}")
            else:
                print("Not found.")

        elif option == "e": # Exit
            print("Exiting tool.")
            break
        else:
            print(f"Unknown option '{option}'. Please choose any of the following:\nOptions: Build(b) | Load(l) | Print a word(p) | Find a phrase(f) | Exit(e)\n")

if __name__ == "__main__":
    main()