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
        self.numCols = 10
        self.numRows = 20

        self.spawnTetromino()
        self.createBorders()

        arcade.play_sound(arcade.load_sound("Game/game/Assets/sound/backgroundmusic.mp3"))

        arcade.schedule(self.moveTetromino, 0.25)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        # Call draw() on all your sprite lists below

        if self.active_tetromino != None:
            self.active_tetromino.draw()
        self.tetromino_list.draw()
        self.border_list.draw()

        arcade.finish_render()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        colision = arcade.check_for_collision_with_list(self.active_tetromino,(self.tetromino_list or self.border_list))
        if colision:
            self.moveTetromino(0, False)
            self.tetromino_list.append(self.active_tetromino)
            self.spawnTetromino()

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

    def spawnTetromino(self):
        self.active_tetromino = arcade.Sprite("Game/game/Assets/tetris/tetrisO.png", SCALING, hit_box_algorithm = "Detailed")
        
        if True: #isEven(tetrominoWidth) and isEven(self.numCols)
            self.active_tetromino.center_x = self.xBoardCenter - (BRICK_LENGTH / 2)
        else:
            self.active_tetromino.center_x = self.xBoardCenter

        if False: #isEven(tetrominoHeight) and isEven(self.numRows)
            self.active_tetromino.center_x = self.yBoardCenter - (BRICK_LENGTH / 2)
        else:
            self.active_tetromino.center_y = self.yBoardCenter

    def moveTetromino(self, delta_time, goingDown = True):
        if self.active_tetromino != None:
            yPos = self.active_tetromino._get_center_y()

            deltaY = BRICK_LENGTH
            if goingDown:
                deltaY *= -1

            self.active_tetromino._set_center_y(yPos + deltaY)

    def createBorders(self):
        borders = self.border_list
        adjNumCols = self.numCols + 2
        adjNumRows = self.numRows + 1

        for i in range(0, adjNumRows):
            for j in range(0, adjNumCols):
                if i == 0 or j % (adjNumCols - 1) == 0:
                    borderBlock = arcade.Sprite("Game/game/Assets/tetris/Border Square.png")

                    # xOffset = 0
                    # if self.numCols % 2 == 0:
                    #     xOffset = BRICK_LENGTH / 2

                    # yOffset = 0
                    # if self.numCols % 2 == 0:
                    #     yOffset = BRICK_LENGTH / 2

                    borderBlock.center_x = self.xBoardCenter - 0 + ((j - (adjNumCols / 2)) * BRICK_LENGTH) 
                    borderBlock.center_y = self.yBoardCenter + 0 + ((i - (adjNumRows / 2)) * BRICK_LENGTH)

                    borders.append(borderBlock)