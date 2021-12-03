import arcade
from game.Title_screen import Title_screen

class Gameover_screen(arcade.View):
    
    def on_show(self):
        ""
        arcade.set_background_color(arcade.color.BLACK)
        arcade.set_viewport(0,self.window.width,0, self.window.height)

    def on_draw(self):
        "Draws the title screen"
        arcade.start_render()
        arcade.draw_text("GAME OVER!!", self.window.width/2, 2*(self.window.height/3), arcade.color.WHITE, font_size = 50, anchor_x="center")
        arcade.draw_text("Click to restart", self.window.width/2, self.window.height/2, arcade.color.WHITE, font_size = 20, anchor_x="center")
    
    def on_mouse_press(self,_x,_y,_button,_modifiers):
        game_view = Title_screen
        game_view.setup()
        self.window.show_view(game_view)