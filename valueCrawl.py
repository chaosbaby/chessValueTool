from fenParser.fen import Position
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker

from chessValueTool import tool
from chessValueTool.dbChessValue import chessValue

# import tool
# from dbChessValue import chessValue



engine = create_engine(
    "mysql+pymysql://root:63632630@127.0.0.1:3306/chess?charset=utf8", max_overflow=50, encoding='utf-8')
Session = sessionmaker(bind=engine)
session = Session()

# pInit = Position()
# value = pInit.getValuedMoves()
# values = tool.formatChessValues(value)
# for value in values:
#     fenMove = value['move']
#     codeMove = tool.toCodeMove(fenMove) 
#     p = Position()
#     p.move(codeMove)
#     objchessValue = chessValue(fen=p.fen, move=p.moveStr, value=p.getValuedMoves())
#     session.add(objchessValue)
#     try:
#         session.commit()
#     except Exception as e:
#         raise e

def crawlValue(fenStr,valueMax = 500,valueMin= -500,valueDiff = 200 ,maxSteps = 3, steps = 1, maxDepth = 2):
    print(steps)
    if steps > maxSteps:
        return
    pInit = Position(fenStr)
    valueStr = pInit.getValuedMoves()
    values = tool.formatChessValues(valueStr)
    if len(values) < 1:
        return
    scoreFirst = values[0]['score']
    for i in range(0, len(values)):
        if i > maxDepth:
            return
        value = values[i]
        score = value['score']
        if score > valueMax or score < valueMin:
            return
        elif abs(score - scoreFirst) > valueDiff:
            return
        else:
            move = tool.toCodeMove(value['move'])
            p = Position(fenStr)
            p.move(move)
            valueStr = p.getValuedMoves()
            if valueStr is None:
                continue
            objchessValue = chessValue(fen=p.fen, move=p.moveStr, valueStr=valueStr, value = score)
            session.add(objchessValue)
            crawlValue(p.fen,valueMax,valueMin,valueDiff,steps = steps+1)



fenStr = "rnbakabr1/9/1c4nc1/p1p1p3p/6p2/9/P1P1P1P1P/1C2C1N2/9/RNBAKABR1 w - - 6 3"
crawlValue(fenStr)
session.commit()