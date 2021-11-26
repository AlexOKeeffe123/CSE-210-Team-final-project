
import arcade
import random

from arcade.arcade_types import Rect
from game.tetromino import Tetromino
from game.constants import BRICK_LENGTH, SCREEN_HEIGHT, SCREEN_WIDTH

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
        self.dropped_bricks = arcade.SpriteList()

        #init borders
        self.bottomBorder = arcade.SpriteList()
        self.leftBorder = arcade.SpriteList()
        self.rightBorder = arcade.SpriteList()
        self.borders = [self.leftBorder, self.rightBorder, self.bottomBorder]
        self._createBorders()

    def update(self, delta_time):
        self.active_tetromino.move(down=1)
        self.checkForCollisions()

    def draw(self):
        self.active_tetromino.draw()
        self.active_tetromino.draw_hit_box(arcade.color.RED)
        for wall_sprite_list in self.borders:
            wall_sprite_list.draw()
        self.dropped_bricks.draw()
        self.dropped_bricks.draw_hit_boxes(arcade.color.RED)

        for rowNum in range(0, self._height):
            for col in range(0, self._width):
                xPos = (self.xCenter - ((self._width / 2) * BRICK_LENGTH)) + (col * BRICK_LENGTH)
                yPos = (self.yCenter - ((self._height / 2) * BRICK_LENGTH)) + (rowNum * BRICK_LENGTH) + (BRICK_LENGTH / 2)
                arcade.draw_point(xPos, yPos, arcade.color.PURPLE, 5)


    def checkForCollisions(self):

        if arcade.check_for_collision_with_lists(self.active_tetromino, [self.dropped_bricks, self.bottomBorder]):
            self.active_tetromino.move(up=1)
            self.dropped_bricks.extend(self.active_tetromino.reduceToBricks())

            for rowNum in range(0, self._height):
                if self._isRowComplete(rowNum):
                    self._clearRow(rowNum)
                    rowNum -= 1

            self.active_tetromino = self._createTetromino()
        elif arcade.check_for_collision_with_list(self.active_tetromino, self.leftBorder):
            self.active_tetromino.move(left=1)
        elif arcade.check_for_collision_with_list(self.active_tetromino, self.rightBorder):
            self.active_tetromino.move(right=1)

    def _isRowComplete(self, rowNum):
        isComplete = True
        for col in range(0, self._width):
            xPos = (self.xCenter - ((self._width / 2) * BRICK_LENGTH)) + (col * BRICK_LENGTH)
            yPos = (self.yCenter - ((self._height / 2) * BRICK_LENGTH)) + (rowNum * BRICK_LENGTH) + (BRICK_LENGTH / 2)
            if len(arcade.get_sprites_at_point([xPos, yPos], self.dropped_bricks)) == 0:
                isComplete = False
        return isComplete

    def _clearRow(self, rowNum):
        print(f"Cleared: {rowNum}")
        for col in range(0, self._width):
            xPos = (self.xCenter - ((self._width / 2) * BRICK_LENGTH)) + (col * BRICK_LENGTH)
            yPos = (self.yCenter - ((self._height / 2) * BRICK_LENGTH)) + (rowNum * BRICK_LENGTH) + (BRICK_LENGTH / 2)
            for brick in arcade.get_sprites_at_point([xPos, yPos], self.dropped_bricks):
                self.dropped_bricks.remove(brick)
            for brick in self.dropped_bricks:
                if brick.center_y > yPos:
                    brick.move(down=1)
            

    def _createTetromino(self):
        tetrominoAssets = ["tetrisI.png", "tetrisJ.png", "tetrisL.png", "tetrisO.png", "tetrisS.png", "tetrisT.png", "tetrisZ.png"]
        fileName = random.choice(tetrominoAssets)
        filePath = (f"Game/game/Assets/image/{fileName}")

        active_tetromino = Tetromino(filePath)
        active_tetromino.center_x = self.xCenter
        active_tetromino.center_y = self.yCenter + (BRICK_LENGTH * self._height / 2)

        if active_tetromino.getWidth() % 2 == 0 and self._width % 2 == 0:
            active_tetromino.center_x -= (BRICK_LENGTH / 2)

        if not(active_tetromino.getHeight() % 2 == 0 and self._height % 2 == 0):
            active_tetromino.center_y -= (BRICK_LENGTH / 2)
        
        return active_tetromino

    def _createBorders(self):
        adjNumCols = self._width + 2
        adjNumRows = self._height + 1

        for i in range(0, adjNumRows):
            for j in range(0, adjNumCols):
                if i == 0 or j % (adjNumCols - 1) == 0:
                    block = arcade.Sprite("Game/game/Assets/image/Border Square.png")

                    # xOffset = 0
                    # if self.numCols % 2 == 0:
                    #     xOffset = BRICK_LENGTH / 2

                    # yOffset = 0
                    # if self.numCols % 2 == 0:
                    #     yOffset = BRICK_LENGTH / 2

                    block.center_x = self.xCenter - 0 + ((j - (adjNumCols / 2)) * BRICK_LENGTH) 
                    block.center_y = self.yCenter + 0 + ((i - (adjNumRows / 2)) * BRICK_LENGTH)

                    if i == 0:
                        self.bottomBorder.append(block)
                    elif j == 0:
                        self.rightBorder.append(block)
                    elif j == (adjNumCols - 1):
                        self.leftBorder.append(block)
