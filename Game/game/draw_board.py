import arcade
from arcade.color import BLACK

class draw_board:

    def draw_background(self):
        background_width = 1000
        background_height = 1200
        background_title = "Team 6 Final Project"
        arcade.open_window(background_width,background_height, background_title)
        arcade.set_background_color(arcade.color.WHITE)
        arcade.start_render()
        arcade.draw_rectangle_filled(background_width/2, background_height/2, 600, background_height- 50, arcade.color.BLACK)
        arcade.finish_render
        arcade.run()