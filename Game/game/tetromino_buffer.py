
from game.tetromino import Tetromino
from game.tetris_grid import TetrisGrid


#drawn from top left corner
class TetrominoBuffer(TetrisGrid):
    def __init__(self, xPos, yPos, size):
        super().__init__(xPos, yPos, 6, size * 3 + 1, True)
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
        print("done")

    def deqeue(self):
        return self._tetrominos.pop()

    def _shiftTetrominosUp(self):
        if len(self._tetrominos) > 1:
            for i in range(1, len(self._tetrominos)):
                self._tetrominos[i].move(up=3)