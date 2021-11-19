
import arcade
from game.director import Director
from game.constants import SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_WIDTH

def main():
    window = Director(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()