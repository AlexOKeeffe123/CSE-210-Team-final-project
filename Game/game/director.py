import arcade
from game.constants import SCREEN_HEIGHT, SCREEN_WIDTH, BRICK_LENGTH
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
        self.board = None
        arcade.set_background_color(arcade.color.AMAZON)

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here
        self.board = Board()
        self.board.spawnTetromino()

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        xCenter = SCREEN_WIDTH / 2
        yCenter = SCREEN_HEIGHT / 2

        boardWidth = self.board.getNumCols() * BRICK_LENGTH
        boardHeight = self.board.getNumRows() * BRICK_LENGTH
        arcade.draw_rectangle_filled(xCenter, yCenter, boardWidth, boardHeight, arcade.color.AFRICAN_VIOLET)

        for i in range(0, self.board.getNumRows()):
            for j in range(0, self.board.getNumCols()):
                xPos = (xCenter - (boardWidth / 2)) + (BRICK_LENGTH * j)
                yPos = (yCenter + (boardHeight / 2)) - (BRICK_LENGTH * i)
                arcade.draw_lrtb_rectangle_filled(xPos, xPos + BRICK_LENGTH, yPos + BRICK_LENGTH, yPos, self.board.getColorAt(i, j))
                arcade.draw_lrtb_rectangle_outline(xPos, xPos + BRICK_LENGTH, yPos + BRICK_LENGTH, yPos, (255, 255, 255, 100))

        # Call draw() on all your sprite lists below

        arcade.finish_render()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.board.moveTetromino()

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