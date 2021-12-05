import arcade
from game.constants import TEXT_COLOR
from game.tetromino import Tetromino
from game.tetris_grid import TetrisGrid
from game.tetromino_buffer import TetrominoBuffer

class TetrisBoard(TetrisGrid):
    def __init__(self, didLose, didWin, scoreToWin, x, y, width = 10, height = 20, color = None):
        #enforce minimum size
        if width < 5:
            width = 5
        if height < 5:
            height = 5
        super().__init__(x, y, width, height, color=color)

        #init active_tetromino and _next_buffer
        self._active_tetromino = None
        self._next_buffer = TetrominoBuffer(self.convertGridToPixel(x=width + 4), self.convertGridToPixel(y=height - 5), 3, color)
        self._next_buffer.populate()
        self._activateNextTetromino()

        self._swap_buffer = TetrominoBuffer(self.convertGridToPixel(x=-4), self.convertGridToPixel(y=height - 2), 1, color)
        self._dropped_bricks = arcade.SpriteList()

        self._allSprites = [self._dropped_bricks, self._next_buffer, self._swap_buffer, super(), self._active_tetromino]

        #stats
        self._score = 0
        self._scoreToWin = scoreToWin
        self._canSwap = True

        #eventHandlers
        self.didLose = didLose
        self.didWin = didWin

    def getScore(self):
        return self._score

    def getScoreToWin(self):
        return self._scoreToWin

    def update(self, delta_time):
        if self._score >= self._scoreToWin:
            self.didWin()

        self._active_tetromino.move(down=1)
        self._handleCollisions()

    def draw(self):
        for sprToDraw in self._allSprites:
            sprToDraw.draw()

    def moveTetromino(self, left = 0, right = 0, up = 0, down = 0):
        self._active_tetromino.move(left, right, up, down)
        self._handleCollisions()

    def _handleCollisions(self):
        if len(self._dropped_bricks) != 0:
            self._dropped_bricks.sort(key=lambda brick: brick.center_y, reverse=True)
            if self._dropped_bricks[0].top + 1 >= self.topBorder[0].bottom:
                self.didLose()
                return

        if arcade.check_for_collision_with_lists(self._active_tetromino, [self._dropped_bricks, self.bottomBorder]):
            self._active_tetromino.move(up=1)
            self._dropped_bricks.extend(self._active_tetromino.reduceToBricks())
            self._updateActiveTetromino()

            rowNumber = 0
            countCleared = 0
            while rowNumber < self._height:
                if self._isRowComplete(rowNumber):
                    self._clearRow(rowNumber)
                    countCleared += 1
                else:
                    rowNumber += 1
            self._score += 1000 if countCleared == 4 else 100 * countCleared

        elif arcade.check_for_collision_with_list(self._active_tetromino, self.leftBorder):
            self._active_tetromino.move(left=1)
        elif arcade.check_for_collision_with_list(self._active_tetromino, self.rightBorder):
            #TODO:Fix bug - light blue, rotating on right wall causes clipping.
            self._active_tetromino.move(right=1)

    def _isRowComplete(self, rowNumber):
        isComplete = True
        yPos = self.convertGridToPixel(y=rowNumber)
        for column in range(0, self._width):
            xPos = self.convertGridToPixel(x=column)
            if len(arcade.get_sprites_at_point([xPos, yPos], self._dropped_bricks)) == 0:
                isComplete = False
        return isComplete

    def _clearRow(self, rowNumber):
        yPos = self.convertGridToPixel(y=rowNumber)
        for column in range(0, self._width):
            xPos = self.convertGridToPixel(x=column)
            for brick in arcade.get_sprites_at_point([xPos, yPos], self._dropped_bricks):
                self._dropped_bricks.remove(brick)

        falling_bricks = []
        for brick in self._dropped_bricks:
            if brick.center_y > yPos:
                #brick.color = arcade.color.RED
                falling_bricks.append(brick)

        falling_bricks.sort(key=lambda brick: brick.center_y)
        for brick in falling_bricks:
            brick.move(down=1)
    
    def _updateActiveTetromino(self):
        self._allSprites.remove(self._active_tetromino)
        self._activateNextTetromino()
        self._canSwap = True
        self._allSprites.insert(0, self._active_tetromino)

    def _activateNextTetromino(self):
        self._active_tetromino = self._next_buffer.deqeue()
        self._next_buffer.enqeue(Tetromino())
        self.snapToGrid(self._active_tetromino)

    def swapActiveTetromino(self):
        if self._canSwap:

            self._allSprites.remove(self._active_tetromino) #dupe code

            self._swap_buffer.enqeue(self._active_tetromino)
            if self._swap_buffer.getLength() > 1:
                self._active_tetromino = self._swap_buffer.deqeue()
                self.snapToGrid(self._active_tetromino)
            else:
                self._activateNextTetromino() #dupe code
            self._canSwap = False

            self._allSprites.insert(0, self._active_tetromino)#dupe code