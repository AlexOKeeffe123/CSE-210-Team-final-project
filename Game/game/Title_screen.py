import arcade
from game.director import Director

class Title_screen(arcade.View):
           
    def on_draw(self):
        "Draws the title screen"
        arcade.start_render()
        arcade.set_background_color(arcade.color.AMAZON)
        arcade.draw_text("TETRIS", self.window.width/2, 2*(self.window.height/3), arcade.color.WHITE, font_size = 50, anchor_x="center")
        arcade.draw_text("Click to start", self.window.width/2, self.window.height/2, arcade.color.WHITE, font_size = 20, anchor_x="center")
    
    def on_mouse_press(self,_x,_y,_button,_modifiers):
        game_view = Director()
        game_view.setup()
        self.window.show_view(game_view)