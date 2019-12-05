import subprocess, os
import sys
import io
enginePath = r"E:\game\三元佳佳鱼九版兵河五四3.6\Engines\佳佳0519\NewGG20180519.exe"
formatEnginInput = "position fen {fen}\n go depth {depth}\n"
def GetValue(fen, depth):
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
    command = formatEngineInput.format(fen= fen , depth = depth)
    stdin.write(command)
    stdin.flush()
    value, baseMove = 0, None
    while True:
        for i in iter(stdout.readline, 'b'):
            print(i)
            if i.find("bestmove") >= 0:
                print("find best move")
                return int(value)

            elif i.find("score") > 0:
                pos = i.find("score")
                value = i.split()[6] or 0

            # elif i == "\n":
            #     print("no result ")
            # elif i.find("info") < 0:
            #     print("not info measage")
            # elif i == None:
            #     print("i is none")
                
def getBestMove(fen, depth):
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
    command = formatEngineInput.format(fen= fen , depth = depth)
    stdin.write(command)
    stdin.flush()
    value, baseMove = None, None
    while True:
        for i in iter(stdout.readline, 'b'):
            print(i)
            if i.find("bestmove") >= 0:
                print("find best move")
                return i.split()[1]

                
            elif i.find("score") > 0:
                value = i.split()[6] or 0

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
    command = formatEngineInput.format(fen= fen , depth = depth)
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
                
    

 


if __name__ == "__main__":
   fen = "rnbakabnr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RNBAKABNR w - - 0 1"
   depth = 20
   ret = GetValue(fen,depth) 
   print("get getvalue result %d"%ret)