import arcade
from arcade.color import SMOKY_BLACK
from game.sound_manager import SoundManager
import game.director

class TitleView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE_SMOKE)

    def on_draw(self):
        "Draws the title screen"
        arcade.start_render()
        xCenter = self.window.width / 2

        yPosLogo = self.yPosByFifths(1.5)
        img = arcade.load_texture('Game/game/Assets/image/Tetris Logo.png')
        arcade.draw_ellipse_filled(xCenter, yPosLogo, 625, 200, SMOKY_BLACK)
        arcade.draw_texture_rectangle(xCenter, yPosLogo, 500, 100, img)

        arcade.draw_text("Every three levels it shrinks", xCenter, self.yPosByFifths(2.5), SMOKY_BLACK, font_size = 25, anchor_x="center")

        arcade.draw_text("Enter or click to start!", xCenter, self.yPosByFifths(3.5), SMOKY_BLACK, font_size = 25, anchor_x="center")

        arcade.draw_text("Space Bar: Store Tetromino", xCenter - 250, self.yPosByFifths(4), SMOKY_BLACK, 16, align="center", width=500)
        arcade.draw_text("Rotate: W   Left: A   Down: S   Right: D", xCenter - 250, self.yPosByFifths(4.2), SMOKY_BLACK, 16, align="center", width=500)    
        arcade.draw_text("Shift: Fast Fall", xCenter - 250, self.yPosByFifths(4.4), SMOKY_BLACK, 16, align="center", width=500)  
        
        arcade.finish_render()
    
    def on_mouse_press(self,_x,_y,_button,_modifiers):
        self.startGame()

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        if key == 65293: #enter
            self.startGame()

    def yPosByFifths(self, numerator):
        return (self.window.height / 5) * (5 - numerator)

    def startGame(self):
        print("Game Started")
        self.window.level = 1
        self.window.total_score = 0
        game_view = game.director.Director()
        self.window.show_view(game_view)

class GameOverView(arcade.View):
    def on_show(self):
        if self.window.total_score == self.window.high_score:
            arcade.set_background_color(arcade.color.WHITE_SMOKE)
        else:
            arcade.set_background_color(arcade.color.BLACK)
        SoundManager().play_gameover_sound()

    def on_draw(self):
        "Draws the title screen"
        arcade.start_render()
        xCenter = self.window.width / 2

        #dynamic end screen
        fontColor = SMOKY_BLACK if self.window.total_score == self.window.high_score else arcade.color.WHITE_SMOKE
        headline = "NEW HIGHSCORE" if self.window.total_score == self.window.high_score else "GAMEOVER"

        arcade.draw_text(headline, xCenter, self.yPosByFifths(1.5), fontColor, font_size = 50, anchor_x="center")
        arcade.draw_text(f"High Score: {self.window.high_score}", xCenter, self.yPosByFifths(2.2), fontColor, font_size = 30, anchor_x="center")
        arcade.draw_text(f"Level Reached: {self.window.level}", xCenter, self.yPosByFifths(2.5), fontColor, font_size = 30, anchor_x="center")
        if self.window.total_score != self.window.high_score:
            arcade.draw_text(f"Final Score: {self.window.total_score}", xCenter, self.yPosByFifths(2.8), fontColor, font_size = 30, anchor_x="center")

        arcade.draw_text("Enter or click to play again!", xCenter, self.yPosByFifths(3.5), fontColor, font_size = 20, anchor_x="center")

        arcade.finish_render()
        
    def on_mouse_press(self,_x,_y,_button,_modifiers):
        self.restartGame()

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        if key == 65293: #enter
            self.restartGame()

    def yPosByFifths(self, numerator):
        return (self.window.height / 5) * (5 - numerator)

    def restartGame(self):
        title_view = TitleView()
        self.window.show_view(title_view)