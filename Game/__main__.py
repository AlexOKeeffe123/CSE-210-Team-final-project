
import arcade
from game.game_views import TitleView
from game.constants import SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_WIDTH

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.total_score = 0
    window.high_score = 0
    window.level = 1

    title_view = TitleView()
    window.show_view(title_view)
    arcade.run()

if __name__ == "__main__":
    main()