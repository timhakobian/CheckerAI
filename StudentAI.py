from random import randint
from BoardClasses import Move
from BoardClasses import Board
from collections import defaultdict

#The following part should be completed by students.
#Students can modify anything except the class name and exisiting functions and varibles.
class StudentAI():

    def __init__(self,col,row,p):
        self.col = col
        self.row = row
        self.p = p
        self.board = Board(col,row,p)
        self.board.initialize_game()
        self.color = ''
        self.opponent = {1:2,2:1}
        self.color = 2

    def get_move(self,move):
        if len(move) != 0:
            self.board.make_move(move,self.opponent[self.color])
        else:
            self.color = 1
        moves = self.board.get_all_possible_moves(self.color)
        index = randint(0,len(moves)-1)
        inner_index =  randint(0,len(moves[index])-1)
        # move = moves[index][inner_index]
        move = self.min_max_recursion(4, True)[0]
        self.board.make_move(move,self.color)
        return move

    def min_max_recursion(self, depth, maximizingPlayer):

        if depth == 0 and self.color == 1:
            return self.board.black_count - self.board.white_count

        elif depth == 0 and self.color == 2:
            return self.board.white_count - self.board.black_count

        maximum = -100
        max_move = ""
        minimum = 100
        min_move = ""
        if maximizingPlayer:
            selfmoves = self.board.get_all_possible_moves(self.color)
            #maximum = -100
            for s_checker_moves in selfmoves:
                for sm in s_checker_moves:
                    self.board.make_move(sm, self.color)
                    Recurs = self.min_max_recursion(depth - 1, False)
                    # print("Recurs: ",Recurs)
                    temp = maximum
                    if type(Recurs) == type(tuple()):
                        maximum = max(maximum, Recurs[1])
                    else:
                        maximum = max(maximum, Recurs)
                    # print("maximum: ",maximum)
                    if temp != maximum:
                        max_move = sm
                    #alpha = max(alpha, Recurs)
                    # print("alpha",alpha)

                    self.board.undo()

                    #if beta <= alpha:
                    #    break
            return (max_move, maximum)

        else:
            #minimum = 100
            oppmoves = self.board.get_all_possible_moves(self.opponent[self.color])
            for o_checker_moves in oppmoves:
                for om in o_checker_moves:
                    self.board.make_move(om, self.opponent[self.color])
                    Recurs = self.min_max_recursion(depth - 1, True)
                    # print("Recurs: ",Recurs)
                    temp = minimum
                    if type(Recurs) == type(tuple()):
                        minimum = min(minimum, Recurs[1])
                    else:
                        minimum = min(minimum, Recurs)
                    # print("minimum: ",minimum)
                    if temp != minimum:
                        min_move = om
                    #beta = min(beta, Recurs)
                    # print("beta: ", beta)

                    self.board.undo()

                    #if beta <= alpha:
                    #    break
            return (min_move, minimum)





"""                    for x in movesb:
                        self.board.make_move(x, self.color)
                        # movesc = self.board.get_all_possible_moves(self.opponent[self.color])
                        c.append(self.board.white_count - self.board.black_count)
                        self.undo()"""