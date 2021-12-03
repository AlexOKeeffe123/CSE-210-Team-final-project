
import arcade
from arcade.sprite import Sprite
from game.tetromino import Tetromino
from game.constants import BRICK_LENGTH, HALF_BRICK_LENGTH, SCALING

class TetrisGrid():
    def __init__(self, x, y, width, height, showGrid = True, color = None):
        self.xCenter = x #+ ((width / 2) * BRICK_LENGTH)
        self.yCenter = y #- ((height / 2) * BRICK_LENGTH)
        self._width = width
        self._height = height
        self._showGrid = showGrid
        self._color = color

        #init borders
        self.topBorder = arcade.SpriteList()
        self.bottomBorder = arcade.SpriteList()
        self.leftBorder = arcade.SpriteList()
        self.rightBorder = arcade.SpriteList()
        self._createBorders()

        self.allBorders = [self.topBorder, self.bottomBorder, self.leftBorder, self.rightBorder]

    def draw(self):
        for sprToDraw in self.allBorders:
            sprToDraw.draw()

        if self._showGrid:
            left = self.convertGridToPixel(x=0) - HALF_BRICK_LENGTH
            right = self.convertGridToPixel(x=self._width) - HALF_BRICK_LENGTH
            bottom = self.convertGridToPixel(y=0) - HALF_BRICK_LENGTH
            top = self.convertGridToPixel(y=self._height) - HALF_BRICK_LENGTH
            color = (self._color[0], self._color[1], self._color[2], 255 / 2) if self._color != None else (0, 0, 0, 255 / 2)

            for pos in range(bottom, top, BRICK_LENGTH):
                arcade.draw_line(left, pos, right, pos, color)

            for pos in range(left, right, BRICK_LENGTH):
                arcade.draw_line(pos, bottom, pos, top, color)

            #DEBUG DOTS
            # for row in range(0, self._height):
            #     yPos = self.convertGridToPixel(y=row)
            #     for column in range(0, self._width):
            #         xPos = self.convertGridToPixel(x=column)
            #         arcade.draw_point(xPos, yPos, arcade.color.PURPLE, 5)

    def snapToGrid(self, tetromino, x = None, y = None):
        if x == None:
            x = self._width / 2
        if y == None:
            y = self._height + 2 #spawn at the top

        coord = self.convertGridToPixel(x, y)
        tetromino.center_x = coord[0]
        tetromino.center_y = coord[1]

        if (tetromino.getWidth() % 2 == 0) == (self._width % 2 == 0):
            tetromino.center_x -= HALF_BRICK_LENGTH

        if tetromino.getHeight() % 2 == 0:
            tetromino.center_y -= HALF_BRICK_LENGTH

    def convertGridToPixel(self, x = None, y = None):
        xPos = int((self.xCenter - ((self._width / 2) * BRICK_LENGTH)) + (x * BRICK_LENGTH)) if x != None else x
        yPos = int((self.yCenter - ((self._height / 2) * BRICK_LENGTH)) + (y * BRICK_LENGTH))  if y != None else y

        if xPos != None and yPos != None:
            return [xPos, yPos]
        elif xPos != None:
            return xPos
        else:
            return yPos

    def _createBorders(self):
        adjNumCols = self._width + 2
        adjNumRows = self._height + 2

        for i in range(0, adjNumRows):
            for j in range(0, adjNumCols):
                if i % (adjNumRows - 1) == 0 or j % (adjNumCols - 1) == 0:
                    block = Sprite("Game/game/Assets/image/Border Square.png", SCALING)
                    if self._color != None:
                        block.color = self._color

                    block.center_x = self.xCenter - 0 + ((j- (adjNumCols / 2)) * BRICK_LENGTH) 
                    block.center_y = self.yCenter + 0 + ((i - (adjNumRows / 2)) * BRICK_LENGTH)

                    if i == 0:
                        self.bottomBorder.append(block)
                    elif i == (adjNumRows - 1):
                        self.topBorder.append(block)
                    elif j == 0:
                        self.rightBorder.append(block)
                    elif j == (adjNumCols - 1):
                        self.leftBorder.append(block)