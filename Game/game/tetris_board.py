
import arcade
import random

from game.tetromino import Tetromino
from game.constants import BRICK_LENGTH

class TetrisBoard():
    def __init__(self, x, y, width = 10, height = 20):
        #position center
        self.xCenter = x
        self.yCenter = y

        #enforce minimum size
        if width < 5:
            width = 5
        if height < 5:
            height = 5
        self._width = width
        self._height = height

        #init tetrominos
        self.active_tetromino = self._createTetromino()
        self._dropped_bricks = arcade.SpriteList()

        #init borders
        self._bottomBorder = arcade.SpriteList()
        self._leftBorder = arcade.SpriteList()
        self._rightBorder = arcade.SpriteList()
        self._borders = [self._leftBorder, self._rightBorder, self._bottomBorder]
        self._createBorders()

        self._score = 0

    def update(self, delta_time):
        self.active_tetromino.move(down=1)
        self.checkForCollisions()

    def draw(self):
        #active, borders, dropped_bricks,
        self.active_tetromino.draw()
        for wall_sprite_list in self._borders:
            wall_sprite_list.draw()
        self._dropped_bricks.draw()

        #purple debug dots and hitboxes
        for row in range(0, self._height):
            yPos = self._convertGridToPixel(y=row)
            for column in range(0, self._width):
                xPos = self._convertGridToPixel(x=column)
                arcade.draw_point(xPos, yPos, arcade.color.PURPLE, 5)
        #self.active_tetromino.draw_hit_box(arcade.color.RED)
        self._dropped_bricks.draw_hit_boxes(arcade.color.RED)

        arcade.draw_text(f"Score: {self._score}", self.xCenter - 75, self._convertGridToPixel(y=0) - (BRICK_LENGTH * 3), arcade.color.WHITE, 16, align="center", width=150)    
        arcade.draw_text("Rotate: W   Left: A   Down: S   Right: D", self.xCenter - 250, self._convertGridToPixel(y=0) - (BRICK_LENGTH * 5), arcade.color.WHITE, 16, align="center", width=500)    



    def checkForCollisions(self):
        if arcade.check_for_collision_with_lists(self.active_tetromino, [self._dropped_bricks, self._bottomBorder]):
            self.active_tetromino.move(up=1)
            self._dropped_bricks.extend(self.active_tetromino.reduceToBricks())
            self.active_tetromino = self._createTetromino()

            rowNumber = 0
            countCleared = 0
            while rowNumber < self._height:
                if self._isRowComplete(rowNumber):
                    self._clearRow(rowNumber)
                    countCleared += 1
                else:
                    rowNumber += 1
            self._score += 1000 if countCleared == 4 else 100 * countCleared

        elif arcade.check_for_collision_with_list(self.active_tetromino, self._leftBorder):
            self.active_tetromino.move(left=1)
        elif arcade.check_for_collision_with_list(self.active_tetromino, self._rightBorder):
            #TODO:Fix bug - light blue, rotating on right wall causes clipping.
            self.active_tetromino.move(right=1)

    def _isRowComplete(self, rowNumber):
        isComplete = True
        yPos = self._convertGridToPixel(y=rowNumber)
        for column in range(0, self._width):
            xPos = self._convertGridToPixel(x=column)
            if len(arcade.get_sprites_at_point([xPos, yPos], self._dropped_bricks)) == 0:
                isComplete = False
        return isComplete

    def _clearRow(self, rowNumber):
        yPos = self._convertGridToPixel(y=rowNumber)
        for column in range(0, self._width):
            xPos = self._convertGridToPixel(x=column)
            for brick in arcade.get_sprites_at_point([xPos, yPos], self._dropped_bricks):
                self._dropped_bricks.remove(brick)

        falling_bricks = []
        for brick in self._dropped_bricks:
            if brick.center_y > yPos:
                brick.color = arcade.color.RED
                falling_bricks.append(brick)

        falling_bricks.sort(key=lambda brick: brick.center_y)
        for brick in falling_bricks:
            brick.move(down=1)
            

    def _createTetromino(self):
        tetrominoAssets = ["tetrisI.png", "tetrisJ.png", "tetrisL.png", "tetrisO.png", "tetrisS.png", "tetrisT.png", "tetrisZ.png"]
        fileName = random.choice(tetrominoAssets)
        filePath = (f"Game/game/Assets/image/{fileName}")

        active_tetromino = Tetromino(filePath)
        active_tetromino.center_x = self.xCenter
        active_tetromino.center_y = self.yCenter + (BRICK_LENGTH * self._height / 2) #spawn at the top

        if (active_tetromino.getWidth() % 2 == 0) == (self._width % 2 == 0):
            active_tetromino.center_x -= (BRICK_LENGTH / 2)

        if not(active_tetromino.getHeight() % 2 == 0):
            active_tetromino.center_y -= (BRICK_LENGTH / 2)
        
        return active_tetromino

    def _createBorders(self):
        adjNumCols = self._width + 2
        adjNumRows = self._height + 1

        for i in range(0, adjNumRows):
            for j in range(0, adjNumCols):
                if i == 0 or j % (adjNumCols - 1) == 0:
                    block = arcade.Sprite("Game/game/Assets/image/Border Square.png")

                    block.center_x = self.xCenter - 0 + ((j - (adjNumCols / 2)) * BRICK_LENGTH) 
                    block.center_y = self.yCenter + 0 + ((i - (adjNumRows / 2)) * BRICK_LENGTH)

                    if i == 0:
                        self._bottomBorder.append(block)
                    elif j == 0:
                        self._rightBorder.append(block)
                    elif j == (adjNumCols - 1):
                        self._leftBorder.append(block)

    def _convertGridToPixel(self, x = None, y = None):
        xPos = (self.xCenter - ((self._width / 2) * BRICK_LENGTH)) + (x * BRICK_LENGTH) if x != None else x
        yPos = (self.yCenter - ((self._height / 2) * BRICK_LENGTH)) + (y * BRICK_LENGTH) + (BRICK_LENGTH / 2) if y != None else y

        if xPos != None and yPos != None:
            return [xPos, yPos]
        elif xPos != None:
            return xPos
        else:
            return yPos
