from unittest.mock import patch, MagicMock
from src.crawler import Crawler

def test_crawler():
    crawler = Crawler()
    assert len(crawler.visitedURLs) == 0

@patch('src.crawler.requests.get')
def test(tester):
    # Make a sample HTTP response
    response = MagicMock()
    response.status_code = 200
    response.text = "<html><body><p>Test Quote</p><a href='/page/2'>Next</a></body></html>"
    tester.return_value = response