import arcade
from arcade.key import T
from game.tetromino import Tetromino
from game.tetris_grid import TetrisGrid
from game.tetromino_buffer import TetrominoBuffer

from game.constants import BRICK_LENGTH, TEXT_COLOR

#TODO: Figure out how to make a grid that doesn't look like crap

class TetrisBoard(TetrisGrid):
    def __init__(self, didLose, didWin, x, y, width = 10, height = 20, color = None):
        #enforce minimum size
        if width < 5:
            width = 5
        if height < 5:
            height = 5
        super().__init__(x, y, width, height, color=color)

        #init active_tetromino and _next_buffer
        self.active_tetromino = None
        self._next_buffer = TetrominoBuffer(self.convertGridToPixel(x=width + 4), self.convertGridToPixel(y=height - 5), 3, color)
        self._next_buffer.populate()
        self._activateNextTetromino()

        self._swap_buffer = TetrominoBuffer(self.convertGridToPixel(x=-4), self.convertGridToPixel(y=height - 2), 1, color)
        self._dropped_bricks = arcade.SpriteList()

        self._allSprites = [self.active_tetromino, self._dropped_bricks, self._next_buffer, self._swap_buffer, super()]

        #stats
        self._score = 0
        self._high_score = 0
        self._canSwap = True

        #evenHandlers
        self.didLose = didLose
        self.didWin = didWin

    def update(self, delta_time):
        if self._score > 1000:
            self.didWin()

        self.active_tetromino.move(down=1)
        self.handleCollisions()

    def draw(self):
        for sprToDraw in self._allSprites:
            sprToDraw.draw()

        #self.active_tetromino.draw_hit_box(arcade.color.RED)
        #self._dropped_bricks.draw_hit_boxes(arcade.color.RED)

        arcade.draw_text(f"Score: {self._score}", self.xCenter - 75, self.convertGridToPixel(y=-3), TEXT_COLOR, 16, align="center", width=150)   
        arcade.draw_text("Rotate: W   Left: A   Down: S   Right: D", self.xCenter - 250, self.convertGridToPixel(y=-5), TEXT_COLOR, 16, align="center", width=500)    
        arcade.draw_text("Space Bar: Store Tetromino", self.xCenter - 250, self.convertGridToPixel(y=-7), TEXT_COLOR, 16, align="center", width=500)    

        #High Score
        arcade.draw_text(f"High Score: {self._high_score}", self.xCenter - -30, self.convertGridToPixel(y=7), arcade.color.BLACK, 16, align="center", width=300)    



    def handleCollisions(self):
        if len(self._dropped_bricks) != 0:
            self._dropped_bricks.sort(key=lambda brick: brick.center_y, reverse=True)
            if arcade.check_for_collision_with_list(self._dropped_bricks[0], self.topBorder):
                self.didLose()
                return

        if arcade.check_for_collision_with_lists(self.active_tetromino, [self._dropped_bricks, self.bottomBorder]):
            self.active_tetromino.move(up=1)
            self._dropped_bricks.extend(self.active_tetromino.reduceToBricks())
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

        elif arcade.check_for_collision_with_list(self.active_tetromino, self.leftBorder):
            self.active_tetromino.move(left=1)
        elif arcade.check_for_collision_with_list(self.active_tetromino, self.rightBorder):
            #TODO:Fix bug - light blue, rotating on right wall causes clipping.
            self.active_tetromino.move(right=1)

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
        self._allSprites.remove(self.active_tetromino)
        self._activateNextTetromino()
        self._canSwap = True
        self._allSprites.insert(0, self.active_tetromino)

    def _activateNextTetromino(self):
        self.active_tetromino = self._next_buffer.deqeue()
        self._next_buffer.enqeue(Tetromino())
        self.snapToGrid(self.active_tetromino)

    def swapActiveTetromino(self):
        if self._canSwap:

            self._allSprites.remove(self.active_tetromino) #dupe code

            self._swap_buffer.enqeue(self.active_tetromino)
            if self._swap_buffer.getLength() > 1:
                self.active_tetromino = self._swap_buffer.deqeue()
                self.snapToGrid(self.active_tetromino)
            else:
                self._activateNextTetromino() #dupe code
            self._canSwap = False

            self._allSprites.insert(0, self.active_tetromino)#dupe code