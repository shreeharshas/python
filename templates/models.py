from pprint import pprint
from math import floor
import random


class Cell:
    row = 0
    col = 0
    val = 0

    def __init__(self, x=0, y=0):
        self.row = x
        self.col = y
        self.val = 0

    def __repr__(self):
        return str(self.val)

    def isValid(self):
        return (self.val > 0 and self.val < 10)


class Board:
    dimensions = 0
    data = [[]]

    def __init__(self, dim):
        self.dimensions = dim
        self.data = [[Cell() for i in range(dim)] for i in range(dim)]

    def display(self):
        #print('\n'.join([''.join(['{:4}'.format(item.val) for item in row]) for row in self.data]))
        pprint(self.data)

    def row(self, i):
        return self.data[i]

    def column(self, i):
        return [row[i] for row in self.data]

    def square(self, i):
        # top left (ii, jj) to bottom right (ii+3, jj+3)
        print("parsecounter is", i)
        ii = int(i/3)
        jj = int(i % 3 * 3)

        # return [[self.data[i][j] for i in range(ii, ii+3)] for j in range(jj, jj+3)]
        retLst = []
        for icount in range(ii, ii+3):
            for jcount in range(jj, jj+3):
                #print("(i,j):", icount, jcount)
                retLst.append(self.data[icount][jcount])
        return retLst

    def validate(self):
        items = set([i for i in range(1, 10)])  # 1 to 9 both inclusive
        # do 9 * 3 checks
        for parseCounter in range(0, 9):
            # validate row
            if set([i for i in self.row(parseCounter)]) != items:
                return False
            # validate column
            if set([i for i in self.column(parseCounter)]) != items:
                return False
            # validate square
            # mat = self.square(parseCounter)
            # print("matrix is:")
            # pprint(mat)
            if set([i for i in self.square(parseCounter)]) == items:
                return False
        return True

    def populateBoardRandom(self):
        if self.data:
            self.data.clear()

        i = 0
        while i < 9:
            my_randoms = random.sample(range(1, 10), 9)
            self.data.append(my_randoms)
            i += 1


class Game:
    nOfCellsToPopulate = 15
    brd = Board(9)

    def StartGame(self):
        self.brd.populateBoardRandom()
        self.brd.display()
        self.RunValidateLogic()

    def RunValidateLogic(self):
        output = self.brd.validate()
        print(output)


gm = Game()
gm.StartGame()
