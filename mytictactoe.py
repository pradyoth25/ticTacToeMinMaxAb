import GameApp

def mymove(board,mysymbol):
    print "Board as seen by the machine:",
    print board
    print "The machine is playing:",
    print mysymbol
    '''if first turn, make a random move'''
    if sum([i==0 for i in board]) == 9:
        return 3

    this_depth = sum([i!=0 for i in board])
    test_gamestate = gamestate(board, mysymbol)
    choices = []
    possiblemoves = test_gamestate.allmoves()

    for move in possiblemoves:
        test_gamestate.makemove(move, mysymbol)
        choices.append(minmax(test_gamestate, user_symbol(mysymbol), mysymbol, this_depth + 1))
        test_gamestate.revertmove(move)

    print "list of moves: ", possiblemoves
    print "list of scores: ", choices
    print "MOVE CHOSEN: ", possiblemoves[choices.index(max(choices))]

    return possiblemoves[choices.index(max(choices))]

class gamestate:
    def __init__(self, board, mysymbol):
        self.board = board
        self.best_score = 0
    def allmoves(self):
        return [i + 1 for i in [i for i, e in enumerate(self.board) if e == 0]]
    def makemove(self, move, mysymbol):
        self.board[move-1] = 1 if mysymbol == "X" else -1
    def revertmove(self, move):
        self.board[move-1] = 0

# minmax implementation
def minmax(gamestate, symbol, mysymbol, depth):
    if GameApp.check_win(gamestate.board) == mysymbol:
        return 10 - depth
    else:
        if GameApp.check_win(gamestate.board) == user_symbol(mysymbol):
            return depth - 10
        if GameApp.check_win(gamestate.board) == "No Winner" and len(gamestate.allmoves()) == 0:
            return 0
    score_list = []
    for move in gamestate.allmoves():
        gamestate.makemove(move, symbol)
        score_list.append(minmax(gamestate, user_symbol(symbol), mysymbol, depth + 1))
        gamestate.revertmove(move)
    print "==========================="
    print "list of scores here: ", score_list
    if machine_turn(mysymbol, depth):
        print "machine turn, return ", max(score_list)
        return max(score_list)
    else:
        print "other turn, return ", min(score_list)
        return min(score_list)

'''helper functions'''

# given a symbol, return the opponent's symbol
def user_symbol(symbol):
    return "X" if symbol == "O" else "O"

# given machine symbol and depth of tree, return true it's machine's turn
def machine_turn(mysymbol, depth):
    if mysymbol == 'X':
        return 1 if depth%2 == 0 else 0
    else:
        return 0 if depth%2 == 0 else 1



