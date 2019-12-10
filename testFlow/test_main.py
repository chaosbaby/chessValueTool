import unittest
from chessValueTool import tool
from chessValueTool import engineCall
from chessValueTool import valueTool
from crawls.chessPlay import Play


class test_valueAMoveList(unittest.TestCase):
    def setup(self):
        pass

    def teardown(self):
        pass

    # @unittest.SkipTest
    def test_getAValueDiffMove(self):
        # *arrange
        startFen = None
        moveList = "77471219"
        dif = 150
        # *act
        ret = valueTool.getValueDiff(startFen, moveList, dif)
        # *assert
        pos = 2
        valueDiffLower = 100
        bestMove = 'a0b0'
        ponderMovesLen = 6

        self.assertEqual(ret["pos"], pos)
        self.assertGreater(ret["score"], valueDiffLower)
        self.assertEqual(ret["bestMove"], bestMove)
        self.assertEqual(len(ret["ponderMoves"]), ponderMovesLen)


    # @unittest.SkipTest
    def test_getValueDiffMoves_pos(self):
        #*arrange
        startFen = None
        moveList = "777080707967121909197242191870781858"
        dif = 150
        depth = 15
        # *act
        moveInfos = valueTool.getValuesDiff(startFen, moveList, dif, depth)
        # *assert
        diffPoses = [1,4,8,9]
        self.assertListEqual(list(moveInfos.keys()), diffPoses)
        

class test_valueAUbbPlay(unittest.TestCase):
    def setup(self):
        pass

    def teardown(self):
        pass

    @unittest.SkipTest
    def test_addValueComments(self):
        ubbPlayStr = """
[DhtmlXQ]
[DhtmlXQ_ver]www_dpxq_com[/DhtmlXQ_ver]
[DhtmlXQ_init]500,350[/DhtmlXQ_init]
[DhtmlXQ_title]无标题[/DhtmlXQ_title]
[DhtmlXQ_event][/DhtmlXQ_event]
[DhtmlXQ_date][/DhtmlXQ_date]
[DhtmlXQ_place][/DhtmlXQ_place]
[DhtmlXQ_round][/DhtmlXQ_round]
[DhtmlXQ_table][/DhtmlXQ_table]
[DhtmlXQ_red][/DhtmlXQ_red]
[DhtmlXQ_redteam][/DhtmlXQ_redteam]
[DhtmlXQ_redrating][/DhtmlXQ_redrating]
[DhtmlXQ_blacktime][/DhtmlXQ_time]
[DhtmlXQ_black][/DhtmlXQ_black]
[DhtmlXQ_blackteam][/DhtmlXQ_blackteam]
[DhtmlXQ_blackrating][/DhtmlXQ_blackrating]
[DhtmlXQ_blacktime][/DhtmlXQ_time]
[DhtmlXQ_result]未知[/DhtmlXQ_result]
[DhtmlXQ_remark][/DhtmlXQ_remark]
[DhtmlXQ_author]chaos[/DhtmlXQ_author]
[DhtmlXQ_binit]0919293949596979891777062646668600102030405060708012720323436383[/DhtmlXQ_binit]
[DhtmlXQ_movelist]777080707967121909197242191870781858[/DhtmlXQ_movelist]
[DhtmlXQ_comment0][FEN "rnbakabnr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RNBAKABNR w"][/DhtmlXQ_comment0]
[DhtmlXQ_type]实战全局/开局[/DhtmlXQ_type]
[DhtmlXQ_timerule][/DhtmlXQ_timerule]
[DhtmlXQ_endtype][/DhtmlXQ_endtype]
[DhtmlXQ_owner]chaos[/DhtmlXQ_owner]
[DhtmlXQ_firstnum]0[/DhtmlXQ_firstnum]
[DhtmlXQ_gametype][/DhtmlXQ_gametype]
[DhtmlXQ_generator]www.ccbridge.net[/DhtmlXQ_generator]
[/DhtmlXQ]
        """
        #*arrange
        p = Play(1000000,ubbPlayStr)
        #*act
        moveList = p.dhtml_xq_movelist
        dif = 150
        depth = 15
        moveInfos = valueTool.getValuesDiff(None, moveList, dif, depth)
        parent = 0
        for i in list(moveInfos.keys()):
            info =  moveInfos[i]
            print(info)
            pos = i
            comment = """
            score :  {score}
            ponderMove : {move}
            """.format(score = info['score'], move ="".join(info['ponderMoves']))
            p.addComment(pos,parent,comment)
            
        retUbb = p.generateUbb()
        print(retUbb) 
        self.fail()
        #*assert

    @unittest.SkipTest
    def test_addMoves_Trunk(self):
        ubbPlayStr = """
[DhtmlXQ]
[DhtmlXQ_ver]www_dpxq_com[/DhtmlXQ_ver]
[DhtmlXQ_init]500,350[/DhtmlXQ_init]
[DhtmlXQ_title]无标题[/DhtmlXQ_title]
[DhtmlXQ_event][/DhtmlXQ_event]
[DhtmlXQ_date][/DhtmlXQ_date]
[DhtmlXQ_place][/DhtmlXQ_place]
[DhtmlXQ_round][/DhtmlXQ_round]
[DhtmlXQ_table][/DhtmlXQ_table]
[DhtmlXQ_red][/DhtmlXQ_red]
[DhtmlXQ_redteam][/DhtmlXQ_redteam]
[DhtmlXQ_redrating][/DhtmlXQ_redrating]
[DhtmlXQ_blacktime][/DhtmlXQ_time]
[DhtmlXQ_black][/DhtmlXQ_black]
[DhtmlXQ_blackteam][/DhtmlXQ_blackteam]
[DhtmlXQ_blackrating][/DhtmlXQ_blackrating]
[DhtmlXQ_blacktime][/DhtmlXQ_time]
[DhtmlXQ_result]未知[/DhtmlXQ_result]
[DhtmlXQ_remark][/DhtmlXQ_remark]
[DhtmlXQ_author]chaos[/DhtmlXQ_author]
[DhtmlXQ_binit]0919293949596979891777062646668600102030405060708012720323436383[/DhtmlXQ_binit]
[DhtmlXQ_movelist]777080707967121909197242191870781858[/DhtmlXQ_movelist]
[DhtmlXQ_comment0][FEN "rnbakabnr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RNBAKABNR w"][/DhtmlXQ_comment0]
[DhtmlXQ_type]实战全局/开局[/DhtmlXQ_type]
[DhtmlXQ_timerule][/DhtmlXQ_timerule]
[DhtmlXQ_endtype][/DhtmlXQ_endtype]
[DhtmlXQ_owner]chaos[/DhtmlXQ_owner]
[DhtmlXQ_firstnum]0[/DhtmlXQ_firstnum]
[DhtmlXQ_gametype][/DhtmlXQ_gametype]
[DhtmlXQ_generator]www.ccbridge.net[/DhtmlXQ_generator]
[/DhtmlXQ]
        """
        #*arrange
        p = Play(1000000,ubbPlayStr)
        #*act
        moveList = p.dhtml_xq_movelist
        dif = 150
        depth = 15
        moveInfos = valueTool.getValuesDiff(None, moveList, dif, depth)
        parent = 0
        for i in list(moveInfos.keys()):
            info =  moveInfos[i]
            print(info)
            pos = i
            p.addMoves(pos,0,info['ponderMoves'])
        retUbb = p.generateUbb()
        print(retUbb) 
        self.fail()
        #*assert