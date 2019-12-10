from fenParser.fen import Position
from chessValueTool import engineCall, tool


def getValueDiff(startfen, moves, diff, depth=20):
    ret = {}
    p = Position(startfen)
    fenMoveList = [moves[i:i+4] for i in range(0, len(moves), 4)]
    startScore = 0
    pos = 0
    for move in fenMoveList:
        pos += 1
        curFen = p.oneMove(move)
        fenInfo = engineCall.getFenInfo(curFen, depth)
        if fenInfo['score'] - startScore > diff:
            fenInfo['pos'] = pos
            return fenInfo


def getValuesDiff(startfen, moves, diff, depth=20):
    ret = {}
    p = Position(startfen)
    moveList = [moves[i:i+4] for i in range(0, len(moves), 4)]
    lastFenInfo = engineCall.getFenInfo(p.fen ,depth)
    lastScore = lastFenInfo['score']
    if p.active is "b":
        lastScore = -lastScore
    pos = 0
    infos = {}
    for move in moveList:
        pos += 1
        curFen = p.oneMove(move)
        fenInfo = engineCall.getFenInfo(curFen, depth)
        scoreOnW = 0
        if p.active is 'b':
            scoreOnW = 0 - fenInfo['score']
        else: 
            scoreOnW = fenInfo['score']
        info = {}
        info['score'] = scoreOnW
        info['ponderMoves'] = lastFenInfo['ponderMoves']
        valueDiff = scoreOnW - lastScore
        if p.active is 'b':
            if valueDiff + diff < 0:
                infos[pos] = info
        else:
            if valueDiff - diff > 0:
                infos[pos] = info
        lastFenInfo = fenInfo
        lastScore = scoreOnW
    return infos
