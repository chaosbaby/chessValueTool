import unittest
from chessValueTool import tool
class test_parseValue(unittest.TestCase):
    def setup(self):
        pass

    def teardown(self):
        pass

    def testNormal(self):
        #*arrange
        retValueStr = "move:c0e2,score:15 (4),rank:2,note:! (44-11),winrate:50.30"
        #*act
        a = tool.formatChessValue(retValueStr) 
        #*assert
        self.assertEqual(a['move'] , 'c0e2')
        self.assertEqual(a['score'] , 15)
        self.assertEqual(a['rank'] , 2)
        self.assertEqual(a['winrate'] , 50.30)

    def testNormal_loneValueStr(self):
        #*arrange
        retValueStr ="move:c0e2,score:15 (4),rank:2,note:! (44-11),winrate:50.30|move:g3g4,score:15 (5),rank:2,note:! (44-02),winrate:50.38|move:h2e2,score:15 (2),rank:2,note:! (45-02),winrate:50.15|move:c3c4,score:15 (5),rank:2,note:! (44-02),winrate:50.38|move:g0e2,score:15 (4),rank:2,note:! (44-11),winrate:50.30"
        #*act
        values = tool.formatChessValues(retValueStr) 
        a = values[0]
        b = values[1]
        last = values[-1]
        #*assert
        self.assertEqual(a['move'] , 'c0e2')
        self.assertEqual(a['score'] , 15)
        self.assertEqual(a['rank'] , 2)
        self.assertEqual(a['winrate'] , 50.30)

        self.assertEqual(b['move'] , 'g3g4')
        self.assertEqual(b['score'] , 15)
        self.assertEqual(b['rank'] , 2)
        self.assertEqual(b['winrate'] , 50.38)

        self.assertEqual(last['move'] , 'g0e2')
        self.assertEqual(last['score'] , 15)
        self.assertEqual(last['rank'] , 2)
        self.assertEqual(last['winrate'] , 50.30)

    def test_formatScoreValue_withExtra(self):
        #*arrange
        scoreStr = "15 (4)"
        #*act
        score = tool.getScore(scoreStr) 
        #*assert
        expectedScore = 15
        self.assertEqual(score, expectedScore)

    def test_formatScoreValue(self):
        #*arrange
        scoreStr = "15"
        #*act
        score = tool.getScore(scoreStr) 
        #*assert
        expectedScore = 15
        self.assertEqual(score, expectedScore)
    
    def test_ToCodeMove(self):
        #*arrange
        fenMove = "h2e2"
        #*act
        codeMove = tool.toCodeMove(fenMove)
        #*assert
        expected = '7747'
        self.assertEqual(codeMove, expected)

    def test_ToCodeMove_Long(self):
        #*arrange
        fenMove = "h2e2g3g4c0e2"
        #*act
        codeMove = tool.toCodeMove(fenMove)
        #*assert
        expected = '774766652947'
        self.assertEqual(codeMove, expected)


    def test_ToFenMove_aUnit(self):
        #*arrange
        codeMove = "7747"
        #*act
        fenMove = tool.toFenMove(codeMove)
        #*assert
        expected = 'h2e2'
        self.assertEqual(fenMove, expected)

    def test_ToFenMove_manyUnit(self):
        #*arrange
        codeMove = '774766652947'
        #*act
        fenMove = tool.toFenMove(codeMove)
        #*assert
        expected = "h2e2g3g4c0e2"
        self.assertEqual(fenMove, expected)