
import arcade
from game.constants import BRICK_LENGTH

class TetrisGrid():
    def __init__(self, x, y, width, height, showGrid = True):
        self.xCenter = x #+ ((width / 2) * BRICK_LENGTH)
        self.yCenter = y #- ((height / 2) * BRICK_LENGTH)
        self._width = width
        self._height = height
        self._showGrid = showGrid

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
            for row in range(0, self._height):
                yPos = self.convertGridToPixel(y=row)
                for column in range(0, self._width):
                    xPos = self.convertGridToPixel(x=column)
                    arcade.draw_point(xPos, yPos, arcade.color.PURPLE, 5)

    def snapToGrid(self, tetromino, x = None, y = None):
        if x == None:
            x = self._width / 2
        if y == None:
            y = self._height + 2 #spawn at the top

        coord = self.convertGridToPixel(x, y)
        tetromino.center_x = coord[0]
        tetromino.center_y = coord[1]

        if (tetromino.getWidth() % 2 == 0) == (self._width % 2 == 0):
            tetromino.center_x -= (BRICK_LENGTH / 2)

        if tetromino.getHeight() % 2 == 0:
            tetromino.center_y -= (BRICK_LENGTH / 2)

    def convertGridToPixel(self, x = None, y = None):
        xPos = (self.xCenter - ((self._width / 2) * BRICK_LENGTH)) + (x * BRICK_LENGTH) if x != None else x
        yPos = (self.yCenter - ((self._height / 2) * BRICK_LENGTH)) + (y * BRICK_LENGTH)  if y != None else y

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
                    block = arcade.Sprite("Game/game/Assets/image/Border Square.png")

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