import arcade
from game.constants import TETROMINO_SOUND_PATH


class sounds():
    def __init__(self):
        self.background_music = arcade.load_sound(TETROMINO_SOUND_PATH[0])
        self.gameover_sound = arcade.load_sound(TETROMINO_SOUND_PATH[1])
        self.gamestart_sound = arcade.load_sound(TETROMINO_SOUND_PATH[2])
        self.tetris_drop_sound = arcade.load_sound(TETROMINO_SOUND_PATH[3])

    def play_startup_music(self):
        arcade.play_sound(self.gamestart_sound, .5, -1)
        arcade.play_sound(self.background_music, .25, 0, True)
    
    def play_gameover_sound(self):
        arcade.play_sound(self.gameover_sound,5,-1)
    
    def play_tetris_drop_sound(self):
        arcade.play_sound(self.tetris_drop_sound,.2,-1)