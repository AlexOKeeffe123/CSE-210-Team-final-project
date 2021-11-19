from math import trunc
import arcade
import random
from game.tetromino import Tetromino
from game.constants import BRICK_LENGTH, SCREEN_HEIGHT, SCREEN_WIDTH

class BoardSquare():
    def __init__(self, isPlayable):
        self._isPlayable = isPlayable
        if isPlayable:           
            self._color = arcade.color.AIR_FORCE_BLUE     
        else:
            self._color = (0, 0, 0, 255) 

    def getColor(self):
        return self._color

class Board():
    # The origin is the top left on 2D grids cause it's easier.
    #[ [1, 1, 1]
    #  [1, 0, 1]
    #  [1, 0, 1]
    #  [1, 1, 1] ]

    def __init__(self, width = 10, height = 20):
        #enforce minimum size
        if width < 5:
            width = 5
        if height < 5:
            height = 5

        #add borders
        self._width = width + 2
        self._height = height + 2

        self._numBufferRows = 2
        self._activeTetromino = None

        self._grid = []
        for i in range(0, self._height + self._numBufferRows):
            self._grid.append([])
            for j in range(0, self._width):
                isPlayable = not(j % (self._width - 1) == 0 or i % (self._height - 1) == 0)
                self._grid[i].append(BoardSquare(isPlayable))
        

    def getNumRows(self):
        return len(self._grid) - self._numBufferRows

    def getNumCols(self):
        return len(self._grid[0])

    def getColorAt(self, row, col):
        if row == 0:
            return self._grid[0][0].getColor()
        elif self.activeTetrominoExists() and self._activeTetromino.collidesWithPoint(row, col):
            return self._activeTetromino.getColor()
        else:
            return self._grid[row][col].getColor()

    def activeTetrominoExists(self):
        return self._activeTetromino is not None

    def spawnTetromino(self):
        shapeOptions = ["I", "J", "L", "O", "S", "Z", "T"]
        self._activeTetromino = Tetromino(1, self.getNumCols() / 2, random.choice(shapeOptions))

    def moveTetromino(self):
        self._activeTetromino.setRow(self._activeTetromino.getRow() + 1)
        

