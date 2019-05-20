# encoding=utf-8

__author__ = 'Q-Whai'
'''
DESC: 这是一款曾经很火的游戏——2048

Blog: http://blog.csdn.net/lemon_tree12138
Create Date: 2016/2/24
Last Modify: 2016/3/9
version: 0.0.2
'''

import random
import copy

class Game2048(object):
    # --------------------------------- #
    # default initial                   #
    # --------------------------------- #
    def __init__(self):
        self.declare = "←：a/h  ↓: s/j ↑: w/k →: d/l , q(uit), b(ack)"
        self.illegal = "Illegal operation!"
        self.no_efficient = "This move has no efficient"
        self.score = 0
        self.step = 0
        self.matrix = init_matrix()
        self.mtr_stk = []  # use step for back
        self.scr_stk = []

        self.tmp = copy.deepcopy(self.matrix)
        self.mtr_stk.append(self.tmp)  # push the init matrix ensure the stack is not empty
        self.scr_stk.append(0)
        display(self.matrix)

    def play(self):
        while check(self.matrix, self.score):
            dirct = raw_input("Step :%d Score :%d (%s):" % (self.step, self.score, self.declare))
            dirct = dirct.lower()  # ensure the direction operation is lower
            # map 0 left,1 down,2 up ,3 right
            if dirct == "q":  # quit
                print("Game is over. Your Score is :%d" % self.score)
                break
            elif dirct == "a" or dirct == "h":  # normal mode and the vim mode
                dirct = 0
            elif dirct == "s" or dirct == "j":
                dirct = 1
            elif dirct == "w" or dirct == "k":
                dirct = 2
            elif dirct == "d" or dirct == "l":
                dirct = 3
            elif dirct == "b":
                if len(self.mtr_stk) == 1: # step one
                    print "Can't Back.."
                else:
                    self.mtr_stk.pop()   # pop up
                    self.scr_stk.pop()
                    self.step -= 1       # step back
                    self.matrix = copy.deepcopy(self.mtr_stk[-1])  # matrix back
                    self.score = self.scr_stk[-1]
                continue        # no move
            else:
                print self.illegal    # not in the operation set
                continue         # has no move
            tmp = copy.deepcopy(self.matrix)   # use to compare the move is efficient ?
            op_scr = move(self.matrix, dirct)
            if tmp != self.matrix:
                self.score = self.score + op_scr  # the move gains
                update(self.matrix)  # insert a number values of 2 or 4
                tmp = copy.deepcopy(self.matrix)  # need to deep copy..
                self.mtr_stk.append(tmp)  # use to back
                self.scr_stk.append(int(self.score))
                self.step += 1  # step++
                display(self.matrix)  # output the matrix
            else:
                print self.no_efficient

# --------------------------------- #
# initial of matrix                 #
# --------------------------------- #
def init_matrix():
    matrix = [[0 for i in range(4)] for j in range(4)]
    ran_pos = random.sample(range(16), 2)
    matrix[ran_pos[0]/4][ran_pos[0] % 4] = matrix[ran_pos[1]/4][ran_pos[1] % 4] = 2
    return matrix

# --------------------------------- #
# output function                   #
# --------------------------------- #
def display(matrix):
    a = ("┌", "├", "├", "├", "└")
    b = ("┬", "┼", "┼", "┼", "┴")
    c = ("┐", "┤", "┤", "┤", "┘")
    for i in range(4):
        print a[i] + ("─" * 5 + b[i]) * 3 + ("─" * 5 + c[i])
        for j in range(4):
            print "│%9s" % (matrix[i][j] if matrix[i][j] else ' '),
        print "│"
    print a[4] + ("─" * 5 + b[4]) * 3 + ("─" * 5 + c[4])

# --------------------------------- #
# update matrix function            #
# --------------------------------- #
def update(matrix):
    ran_pos = []
    ran_num = [2, 4]
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                ran_pos.append(4 * i + j)
    if len(ran_pos) > 0:  # can insert
        k = random.choice(ran_pos)
        n = random.choice(ran_num)
        matrix[k / 4][k % 4] = n

# --------------------------------- #
# check for the game is over ?      #
# --------------------------------- #
def check(matrix, score):
    if 2048 in matrix:  # 2048 and win
        print "Great!You win!Your score is ", score
        raw_input("Press any key to continue...")
        exit()
    if 0 in matrix:  # can insert number！
        return True
    for i in range(4):
        for j in range(4):   # can merge number!
            if i < 3 and matrix[i][j] == matrix[i + 1][j]:
                return True
            if j < 3 and matrix[i][j] == matrix[i][j + 1]:
                return True
    print "Gameover!"
    return False

# ---------------------------------------- #
# the core code!move by the four direction #
# ---------------------------------------- #
def move(matrix, dirct):
    score = 0
    visit = []
    if dirct == 0:  # left
        for i in range(4):
            for j in range(1, 4):
                for k in range(j, 0, -1):
                    if matrix[i][k - 1] == 0:
                        matrix[i][k - 1] = matrix[i][k]
                        matrix[i][k] = 0
                    elif matrix[i][k - 1] == matrix[i][k] and 4 * i + k - 1 not in visit and 4 * i + k not in visit:
                        matrix[i][k - 1] *= 2
                        matrix[i][k] = 0
                        score += matrix[i][k - 1]
                        visit.append(4 * i + k)
                        visit.append(4 * i + k - 1)
    elif dirct == 1:  # down
        for j in range(4):
            for i in range(3, 0, -1):
                for k in range(0, i):
                    if matrix[k + 1][j] == 0:
                        matrix[k + 1][j] = matrix[k][j]
                        matrix[k][j] = 0
                    elif matrix[k + 1][j] == matrix[k][j] and (4 * (k + 1) + j) not in visit and (4 * k + j) not in visit:
                        matrix[k + 1][j] *= 2
                        matrix[k][j] = 0
                        score = matrix[k + 1][j]
                        visit.append(4 * k + j)
                        visit.append(4 * (k + 1) + j)
    elif dirct == 2:  # up
        for j in range(4):
            for i in range(1, 4):
                for k in range(i, 0, -1):
                    if matrix[k-1][j] == 0:
                        matrix[k-1][j] = matrix[k][j]
                        matrix[k][j] = 0
                    elif matrix[k-1][j] == matrix[k][j] and (4 * (k - 1) + j) not in visit and (4 * k + j) not in visit:
                        matrix[k-1][j] *= 2
                        matrix[k][j] = 0
                        score += matrix[k - 1][j]
                        visit.append(4 * k + j)
                        visit.append(4 * (k - 1) + j)
    elif dirct == 3:  # right
        for i in range(4):
            for j in range(3, 0, -1):
                for k in range(j):
                    if matrix[i][k + 1] == 0:
                        matrix[i][k + 1] = matrix[i][k]
                        matrix[i][k] = 0
                    elif matrix[i][k] == matrix[i][k + 1] and 4 * i + k + 1 not in visit and 4 * i + k not in visit:
                        matrix[i][k + 1] *= 2
                        matrix[i][k] = 0
                        score += matrix[i][k + 1]
                        visit.append(4 * i + k + 1)
                        visit.append(4 * i + k)
    return score
