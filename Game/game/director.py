import arcade
from arcade.sprite import Sprite
from game.constants import SCREEN_HEIGHT, SCREEN_WIDTH, BRICK_LENGTH, SCALING
from game.board import Board


class Director(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        # If you have sprite lists, you should create them here,
        # and set them to None
        self.active_tetromino = None
        self.tetromino_list = arcade.SpriteList()
        self.border_list = arcade.SpriteList()

        self.numCols = None
        self.numRows = None
        self.xBoardCenter = self.width / 2
        self.yBoardCenter = self.height / 2

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here
        arcade.set_background_color(arcade.color.AMAZON)
        self.numCols = 2
        self.numRows = 20

        self.active_tetromino = arcade.Sprite("Game/game/Assets/tetris/tetrisO.png", SCALING, hit_box_algorithm = "Detailed") 
        self.active_tetromino.center_y = self.height / 2
        self.active_tetromino.center_x = self.width / 2

        self.createBorders()

        arcade.schedule(self.moveTetromino, 3.0)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        # Call draw() on all your sprite lists below

        #self.active_tetromino.draw()

        arcade.finish_render()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def moveTetromino(self, delta_time):
        yPos = self.active_tetromino._get_center_y()
        self.active_tetromino._set_center_y(yPos - BRICK_LENGTH)

    def createBorders(self):
        boardWidth = self.numCols * BRICK_LENGTH
        boardHeight = self.numRows * BRICK_LENGTH

        borders = self.border_list

        for i in range(0, self.numRows):
            for j in range(0, self.numCols):
                borderBlock = arcade.sprite("Game/game/Assets/tetris/Border Square.png")

                xOffset = 0
                if self.numCols % 2 == 0:
                    offset = BRICK_LENGTH / 2

                borderBlock.center_x = xScreenCenter - xOffset
                borderBlock.center_y = yScreenCenter
                borders.append()