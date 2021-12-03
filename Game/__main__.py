
import arcade
from game.Title_screen import Title_screen
from game.constants import SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_WIDTH

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = Title_screen()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()