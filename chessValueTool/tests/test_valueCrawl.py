import unittest
from fenParser.fen import Position
from chessValueTool import tool

class test_valueCrawl(unittest.TestCase):
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_crawlInitPos(self):
        #*arrange
        simpleFen ="3k5/9/9/9/9/2Rr5/9/9/9/4K4 w - - 0 0"
        p = Position(simpleFen)
        #*act
        #*assert
        expected = "move:c4d4,score:29999,rank:2,note:! (W-M-0001)"
        expectedValues = tool.formatChessValues(expected)
        ret = p.getValuedMoves()[:-1]
        retValues = tool.formatChessValues(ret)
        # self.maxDiff = None
        # for i in range(0,0):
        #     self.assertDictEqual(retValues[i], expectedValues[i])

        self.assertDictEqual(retValues[0], expectedValues[0])

        
