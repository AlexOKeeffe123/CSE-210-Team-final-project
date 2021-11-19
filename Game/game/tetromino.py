


import arcade


class Tetromino():
    def __init__(self, row, col, shape):
        #top left corner
        self._row = row
        self._col = col

        #if shape == "whatever"
            #self._shape = bitMap
            #self._color = color
        self._shape = [[True]]
        self._color = arcade.color.PURPLE

    #[ [1, 1, 1]
    #  [1, 0, 1]
    #  [1, 0, 1]
    #  [1, 1, 1] ]

    #GETTERS
    def getRow(self):
        return int(self._row)

    def getCol(self):
        return int(self._col)

    def getWidth(self):
        return len(self._shape[0])

    def getHeight(self):
        return len(self._shape)

    def getColor(self):
        return self._color

    #SETTERS
    def setRow(self, row):
        self._row = row

    def setCol(self, col):
        self._col = col

    #HELPERS
    def collidesWithPoint(self, row, col):
        left = self.getCol()
        top = self.getRow()
        right = left + self.getWidth() - 1
        bottom = top + self.getHeight() - 1

        #if collision exists with the space the bitmap takes up on the board
        if row >= top and row <= bottom and col >= left and col <= right: 
            #check the bitmap
            bitMapRow = row - top
            bitMapCol = col - left
            return self._shape[bitMapRow][bitMapCol]