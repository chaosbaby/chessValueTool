import unittest
from chessValueTool import tool
from chessValueTool import engineCall

class test_engineCall(unittest.TestCase):
    def setup(self):
        pass

    def teardown(self):
        pass

    # @unittest.SkipTest
    def test_getValuedFromEngine(self):
        #*arrange
        simpleFen ="3k5/9/9/9/9/2Rr5/9/9/9/4K4 w - - 0 0"
        simpleFen = "rnbakabnr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RNBAKABNR w - - 0 1"
        depth = 20
        expectedLowestScore = 3000
        #*act
        ret = engineCall.GetValue(simpleFen, depth)
        #*assert
        self.assertLess(ret, expectedLowestScore)

    # @unittest.SkipTest
    def test_getBestMoveFromEngine(self):
        #*arrange
        simpleFen ="3k5/9/9/9/9/2Rr5/9/9/9/4K4 w - - 0 0"
        depth = 20
        expectedBestMove = "c4d4"
        #*act
        ret = engineCall.getBestMove(simpleFen, depth)
        #*assert
        self.assertEqual(ret, expectedBestMove)
        
    def test_getFenInfo_mate(self):
        #*arrange
        simpleFen ="rnbakabCr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C7/9/RNBAKABNR b - - 0 0"
        depth = 20
        ret = engineCall.getFenInfo(simpleFen, depth)
        #*assert
        expectedBestMove = "i9h9"
        expectedScoreHigher = 500
        expectedPonderMovesLen = 6

        self.assertEqual(ret['bestMove'], expectedBestMove )
        self.assertGreater(expectedScoreHigher, ret['score'])
        self.assertEqual(len(ret['ponderMoves']) , expectedPonderMovesLen) 