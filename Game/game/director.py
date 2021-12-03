import arcade
from arcade.key import DOWN
from game.constants import BOARD_COLORS, SCREEN_HEIGHT, SCREEN_WIDTH
from game.tetris_board import TetrisBoard
import random
from game.sound import sounds


class Director(arcade.View):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self):
        super().__init__()
        # If you have sprite lists, you should create them here,
        # and set them to None
        self.board = None
        self.sound = sounds()
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT

    def setup(self, level = 0):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here
        arcade.set_background_color(arcade.color.WHITE_SMOKE)
        self.board = TetrisBoard(self.didLose, self.didWin, self.width / 2, self.height / 2, 10, 20, random.choice(BOARD_COLORS))

        arcade.play_sound(arcade.load_sound("Game/game/Assets/sound/backgroundmusic.mp3"))
        arcade.schedule(self.board.update, 0.25)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        # Call draw() on all your sprite lists below

        self.board.draw()

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
        if key == 65361 or key == 97: # left or a
            self.board.active_tetromino.move(left=1)
        if key == 65362 or key == 119: # up or w
            self.board.active_tetromino.rotate()
        if key == 65363 or key == 100: # right or d
            self.board.active_tetromino.move(right=1)
        if key == 65364 or key == 115: # down or s
            self.board.active_tetromino.move(down=1)
        if key == 32:
            self.board.swapActiveTetromino()
        self.board.handleCollisions()

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def didWin(self):
        print("didWin")

    def didLose(self):
        print("didLose")