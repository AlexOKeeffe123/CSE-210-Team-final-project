import arcade
from arcade.key import N
from game.constants import TETROMINO_SOUND_PATH


class SoundManager():
    def __init__(self):
        self.background_music = arcade.load_sound(TETROMINO_SOUND_PATH[0])
        self.gameover_sound = arcade.load_sound(TETROMINO_SOUND_PATH[1])
        self.gamestart_sound = arcade.load_sound(TETROMINO_SOUND_PATH[2])
        self.tetris_drop_sound = arcade.load_sound(TETROMINO_SOUND_PATH[3])

        self._music_player = None

    def play_startup_music(self):
        arcade.play_sound(self.gamestart_sound, .5, -1)
        self._music_player = arcade.play_sound(self.background_music, .25, 0, True)
    
    def play_gameover_sound(self):
        arcade.play_sound(self.gameover_sound,5,-1)
    
    def play_tetris_drop_sound(self):
        arcade.play_sound(self.tetris_drop_sound,.2,-1)

    def stopMusic(self):
        if self._music_player != None:
            arcade.stop_sound(self._music_player)