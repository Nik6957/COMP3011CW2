import tempfile
import os
from src.indexer import Indexer

def testStripText():
    indexer = Indexer()
    text = "Lorem ipsum DOLOR! sit amet. Expliciting  alit. "
    cleaned = indexer.stripText(text)
    assert cleaned == ["lorem", "ipsum", "dolor", "sit", "amet", "expliciting", "alit"]

def testMakeIndex():
    indexer = Indexer()
    testURL = {"http://test.com/1": "Alpha bravo alpha charlie",}
    index = indexer.makeIndex(testURL)
    
    assert "alpha" in index
    assert index["alpha"]["http://test.com/1"]["freq"] == 2
    assert index["alpha"]["http://test.com/1"]["positions"] == [0, 2]

def testFiling():
    indexer = Indexer()
    indexer.index = {"test": {"url": {"freq": 1, "positions": [0]}}}
    
    with tempfile.NamedTemporaryFile(delete = False) as temp:
        tempPath = temp.name
        
    try:
        indexer.save(tempPath)
        newIndexer = Indexer()
        newIndexer.load(tempPath)
        assert "test" in newIndexer.index
    finally:
        os.remove(tempPath)