import subprocess
import os
import sys
import io
enginePath = r"E:\game\三元佳佳鱼九版兵河五四3.6\Engines\佳佳0519\NewGG20180519.exe"
formatEnginInput = "position fen {fen}\n go depth {depth}\n"


def getFenInfo(fen, depth):
    proc = subprocess.Popen(
        enginePath,
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    stdin = io.TextIOWrapper(
        proc.stdin,
        # encoding='utf-8',
        line_buffering=True,  # send data on newline
    )
    stdout = io.TextIOWrapper(
        proc.stdout,
        # encoding='utf-8',
    )
    sys.stderr.flush()
    formatEngineInput = "position fen {fen}\n go depth {depth}\n"
    command = formatEngineInput.format(fen=fen, depth=depth)
    stdin.write(command)
    stdin.flush()
    ret = {}
    ret["score"] = None
    ret["bestMove"] = None
    ret["ponderMoves"] = None
    while True:
        for i in iter(stdout.readline, 'b'):
            if i.find("depth {}".format(depth)) > 0:
                mark = " pv "
                pos = i.find(mark) + len(mark)
                ret["ponderMoves"] = i[pos:].split()[:6]
            elif i.find("score") > 0:
                ret['score'] = int(i.split()[6]) or 0
            elif i.find("bestmove") >= 0:
                print("find best move")
                ret["bestMove"] = i.split()[1]
                return ret


def GetValue(fen, depth):
    info = getFenInfo(fen, depth)
    return info['score']


def getBestMove(fen, depth):
    info = getFenInfo(fen, depth)
    return info['bestMove'] 



if __name__ == "__main__":
    fen = "rnbakabnr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RNBAKABNR w - - 0 1"
    depth = 20
    ret = GetValue(fen, depth)
    print("get getvalue result %d" % ret)
