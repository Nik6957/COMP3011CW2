from src.indexer import Indexer
from src.search import Search

def testSearch():
    indexer = Indexer()
    indexer.index = {
        "good": {
            "page1": {"freq": 1, "positions": [0]},
            "page2": {"freq": 1, "positions": [3]}
        },
        "friends": {
            "page1": {"freq": 1, "positions": [1]},
            "page3": {"freq": 2, "positions": [0, 4]}
        },
        "nonsense": {
            "page2": {"freq": 1, "positions": [0]}
        }
    }
    return Search(indexer)

def testPrint(testSearch):
    info = testSearch.printIndex("Good")
    assert "page1" in info
    assert "page2" in info

def testFind(testSearch):
    results = testSearch.findPhrase("nonsense")
    assert results == ["page2"]

def testFindMany(testSearch):
    results = testSearch.findPhrase("good friends")
    assert results == ["page1"]

def testFindDNE(testSearch):
    results = testSearch.findPhrase("missingword")
    assert results == []