
import arcade
from arcade.sprite import Sprite
from game.constants import BRICK_LENGTH, HALF_BRICK_LENGTH, SCALING

class TetrisGrid():
    def __init__(self, x, y, width, height, showGrid = True, color = None):
        self._xCenter = x
        self._yCenter = y
        self._width = width
        self._height = height
        self.showGrid = showGrid
        self.color = color

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

        if self.showGrid:
            left = self.convertGridToPixel(x=0) - HALF_BRICK_LENGTH
            right = self.convertGridToPixel(x=self._width) - HALF_BRICK_LENGTH
            bottom = self.convertGridToPixel(y=0) - HALF_BRICK_LENGTH
            top = self.convertGridToPixel(y=self._height) - HALF_BRICK_LENGTH
            color = (self.color[0], self.color[1], self.color[2], 255 / 2) if self.color != None else (0, 0, 0, 255 / 2)

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

    def getCenterX(self):
        return self._xCenter

    def getCenterY(self):
        return self._yCenter

    def getWidth(self):
        return (self._width + 2) * BRICK_LENGTH

    def getHeight(self):
        return (self._height + 2) * BRICK_LENGTH

    def getTop(self):
        return self.getCenterY() + (self.getHeight() / 2)

    def getBottom(self):
        return self.getCenterY() - (self.getHeight() / 2)

    def snapToGrid(self, tetromino, x = None, y = None):
        if x == None:
            x = self._width / 2
        if y == None:
            y = self._height - 1 #spawn at the top

        coord = self.convertGridToPixel(x, y)
        tetromino.center_x = coord[0]
        tetromino.center_y = coord[1]

        if (tetromino.getWidth() % 2 == 0) == (self._width % 2 == 0):
            tetromino.center_x -= HALF_BRICK_LENGTH

        if tetromino.getHeight() % 2 == 0:
            tetromino.center_y -= HALF_BRICK_LENGTH

    def convertGridToPixel(self, x = None, y = None):
        xPos = int((self._xCenter - ((self._width / 2) * BRICK_LENGTH)) + (x * BRICK_LENGTH)) if x != None else x
        yPos = int((self._yCenter - ((self._height / 2) * BRICK_LENGTH)) + (y * BRICK_LENGTH))  if y != None else y

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
                    if self.color != None:
                        block.color = self.color

                    block.center_x = self._xCenter - 0 + ((j- (adjNumCols / 2)) * BRICK_LENGTH) 
                    block.center_y = self._yCenter + 0 + ((i - (adjNumRows / 2)) * BRICK_LENGTH)

                    if i == 0:
                        self.bottomBorder.append(block)
                    elif i == (adjNumRows - 1):
                        self.topBorder.append(block)
                    elif j == 0:
                        self.rightBorder.append(block)
                    elif j == (adjNumCols - 1):
                        self.leftBorder.append(block)