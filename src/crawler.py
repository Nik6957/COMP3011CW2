import time
import urllib.parse
import requests
from bs4 import BeautifulSoup

class Crawler:
    def __init__(self, homeURL="https://quotes.toscrape.com/"):
        self.homeURL = homeURL
        self.visitedURLs = set()
        self.content = {}

    def crawling(self):
        queue = [self.homeURL]
        
        while queue:
            curURL = queue.pop(0)
            if curURL in self.visitedURLs:
                continue
                
            print(f"Crawling: {curURL}")
            try:
                # 6 sec delay
                time.sleep(6.0)
                response = requests.get(curURL, timeout = 10)
                
                if response.status_code != 200:
                    print(f"Failed fetching {curURL}. Error code {response.status_code}.")
                    continue
                    
                self.visitedURLs.add(curURL)
                parser = BeautifulSoup(response.text, 'html.parser')
                
                # Extract text
                context = parser.get_text(separator=' ')
                self.content[curURL] = context
                
                # Move on to next pages and add them to queue
                for anchor in parser.find_all('a', href=True):
                    href = anchor['href']
                    fullURL = urllib.parse.urljoin(self.homeURL, href)
                    
                    # Stay in target domain only 
                    if fullURL.startswith(self.homeURL) and fullURL not in self.visitedURLs:
                        if fullURL not in queue:
                            queue.append(fullURL)
                            
            except requests.RequestException as e:
                print(f"Network error {e}.")
                
        return self.content