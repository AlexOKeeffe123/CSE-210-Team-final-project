from game.tetromino import Tetromino
from game.tetris_grid import TetrisGrid

class TetrominoBuffer(TetrisGrid):
    def __init__(self, xPos, yPos, size, color = None):
        super().__init__(xPos, yPos, 6, size * 3 + 1, color=color)
        self._tetrominos = []
        self._size = size

    def draw(self):
        super().draw()
        for tetromino in self._tetrominos:
            tetromino.draw()

    def getLength(self):
        return len(self._tetrominos)

    def enqeue(self, tetromino):
        self._tetrominos.insert(0, tetromino)        
        self.snapToGrid(self._tetrominos[0], y=2)
        self._shiftTetrominosUp()

    def populate(self):
        for _ in range(0, self._size):
            self.enqeue(Tetromino())

    def deqeue(self):
        return self._tetrominos.pop()

    def _shiftTetrominosUp(self):
        if len(self._tetrominos) > 1:
            for i in range(1, len(self._tetrominos)):
                self._tetrominos[i].move(up=3)