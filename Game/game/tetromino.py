from game.constants import SCALING, BRICK_LENGTH

import arcade

class Tetromino(arcade.Sprite):
    def __init__(self, filename = "Game/game/Assets/image/Grid Square.png", scale = SCALING):
        super().__init__(filename, scale)

        type = filename[-5]
        if type == "I":
            custom_hit_box = [[-2, -0.5], [-2, 0.5], [2, 0.5], [2, -0.5]]
            self.relativeCenter = [0, 0.5]
        elif type == "J":
            custom_hit_box = [[-1.5, -1], [-1.5, 1], [-0.5, 1], [-0.5, 0], [1.5, 0], [1.5, -1]]
            self.relativeCenter = [0, -0.5]
        elif type == "L":
            custom_hit_box = [[-1.5, -1], [-1.5, 0], [0.5, 0], [0.5, 1], [1.5, 1], [1.5, -1]]
            self.relativeCenter = [0, -0.5]
        elif type == "O":
            custom_hit_box = [[-1, -1], [-1, 1], [1, 1], [1, -1]]
            self.relativeCenter = [0, 0]
        elif type == "S":
            custom_hit_box = [[-1.5, -1], [-1.5, 0], [-0.5, 0], [-0.5, 1], [1.5, 1], [1.5, 0], [0.5, 0], [0.5, -1]]
            self.relativeCenter = [0, 0.5]
        elif type == "T":
            custom_hit_box = [[-1.5, -1], [-1.5, 0], [-0.5, 0], [-0.5, 1], [0.5, 1], [0.5, 0], [1.5, 0], [1.5, -1]]
            self.relativeCenter = [0, -0.5]
        elif type == "Z":
            custom_hit_box = [[-1.5, 0], [-1.5, 1], [0.5, 1], [0.5, 0], [1.5, 0], [1.5, -1], [-0.5, -1], [-0.5, 0]]
            self.relativeCenter = [0, 0.5]
        else:
            custom_hit_box = [[-0.5, -0.5], [-0.5, 0.5], [0.5, 0.5], [0.5, -0.5]]
            self.relativeCenter = [0, 0]

        self.hit_box = list(map(lambda point: list(map(lambda coord: coord * BRICK_LENGTH, point)), custom_hit_box))

    def move(self, left = 0, right = 0, up = 0, down = 0):
        deltaX = (right - left) * BRICK_LENGTH 
        if deltaX != 0:
            self._set_center_x(self._get_center_x() + deltaX)

        deltaY = (up - down) * BRICK_LENGTH
        if deltaY != 0:
            self._set_center_y(self._get_center_y() + deltaY)

    def rotate(self):
        self.turn_right()
        newRelCenter = [self.relativeCenter[1], -self.relativeCenter[0]]
        self._set_center_x(self._get_center_x() + (self.relativeCenter[0] - newRelCenter[0]) * BRICK_LENGTH)
        self._set_center_y(self._get_center_y() + (self.relativeCenter[1] - newRelCenter[1]) * BRICK_LENGTH)
        self.relativeCenter = newRelCenter

    def getWidth(self):
        if self.getAngle() == 90 or self.getAngle() == 270:
            return int(self._get_height() / BRICK_LENGTH)
        else:
            return int(self._get_width() / BRICK_LENGTH)

    def getHeight(self):
        if self.getAngle() == 90 or self.getAngle() == 270:
            return int(self._get_width() / BRICK_LENGTH)
        else:
            return int(self._get_height() / BRICK_LENGTH)

    def getAngle(self):
        return ((abs(self.angle) / 90) % 4) * 90

    def reduceToBricks(self):
        bricks = []
        for row in range(0, self.getHeight()):
            for col in range(0, self.getWidth()):
                xPos = (self._get_center_x() - ((self.getWidth() / 2) * BRICK_LENGTH)) + (col * BRICK_LENGTH) + (BRICK_LENGTH / 2)
                yPos = (self._get_center_y() - ((self.getHeight() / 2) * BRICK_LENGTH)) + (row * BRICK_LENGTH) + (BRICK_LENGTH / 2)

                if self.collides_with_point([xPos, yPos]):
                    brick = Tetromino()
                    brick._set_center_x(xPos)
                    brick._set_center_y(yPos)
                    bricks.append(brick)
        return bricks

        
