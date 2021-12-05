import arcade
import random

from arcade.key import DOWN
from game.constants import BOARD_COLORS, TEXT_COLOR

import game.game_views
from game.sound_manager import SoundManager
from game.tetris_board import TetrisBoard


class Director(arcade.View):
    """
    Main application class.
    """

    def __init__(self):
        super().__init__()
        # If you have sprite lists, you should create them here,
        # and set them to None
        self.board = None
        self.speed = None
        self.sound = SoundManager()
        self.width = self.window.width
        self.height = self.window.height

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here
        arcade.set_background_color(arcade.color.WHITE_SMOKE)
        self.speed = 1 - (((self.window.level - 1) % 12) * 0.08)
        levelUpScore = 250 * self.window.level

        self.board = TetrisBoard(self.didLose, self.didWin, levelUpScore, self.width / 2, self.height / 2, 10, 20, random.choice(BOARD_COLORS))
        arcade.schedule(self.board.update, self.speed)
        self.sound.play_startup_music()

    def on_show(self):
        self.setup()

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()

        arcade.draw_text(f"LEVEL: {self.window.level}", self.board.getCenterX(), self.board.getTop() + 100, TEXT_COLOR, 64, anchor_x="center")
        arcade.draw_text(f"Next Level: {self.board.getScoreToWin() + self.window.total_score}", self.board.getCenterX(), self.board.getTop() + 50, TEXT_COLOR, 24, anchor_x="center")
        self.board.draw()
        arcade.draw_text(f"High Score: {self.window.high_score}", self.board.getCenterX(), self.board.getBottom() - 50, TEXT_COLOR, 24, anchor_x="center")
        arcade.draw_text(f"Score: {self.getTotalScore()}", self.board.getCenterX(), self.board.getBottom() - 100, TEXT_COLOR, 24, anchor_x="center") 

        arcade.finish_render()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        if self.getTotalScore() > self.window.high_score:
            self.window.high_score = self.getTotalScore()

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        if key == 32:
            self.board.swapActiveTetromino()
            self.sound.play_tetris_drop_sound()

        if key == 65361 or key == 97: # left or a
            self.board.moveTetromino(left=1)
        if key == 65362 or key == 119: # up or w
            self.board._active_tetromino.rotate()
            self.sound.play_tetris_drop_sound()
        if key == 65363 or key == 100: # right or d
            self.board.moveTetromino(right=1)
        if key == 65364 or key == 115: # down or s
            self.board.moveTetromino(down=1)

        if key == 65505 or key == 65506: # left or right shift
            arcade.unschedule(self.board.update)
            arcade.schedule(self.board.update, 0.05)

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        if key == 65505 or key == 65506:
            arcade.unschedule(self.board.update)
            arcade.schedule(self.board.update, self.speed)

    def didWin(self):
        self.endRound()
        self.window.level += 1
        self.setup()

    def didLose(self):
        self.endRound()
        self.window.level = 1
        end_view = game.game_views.GameOverView()
        self.window.show_view(end_view)

    def endRound(self):
        self.sound.stopMusic()
        arcade.unschedule(self.board.update)
        self.window.total_score += self.board.getScore()

    def getTotalScore(self):
        return self.board.getScore() + self.window.total_score

