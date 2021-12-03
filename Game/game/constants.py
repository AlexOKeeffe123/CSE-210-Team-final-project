# Screen title and size
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 960
BRICK_LENGTH = 20
if not(BRICK_LENGTH > 1):
    BRICK_LENGTH = 2
HALF_BRICK_LENGTH = int(BRICK_LENGTH / 2)
SCALING = 1
SCREEN_TITLE = "TETRIS"
TETROMINO_FILEPATHS = ["Game/game/Assets/image/tetrisI.png", "Game/game/Assets/image/tetrisJ.png", "Game/game/Assets/image/tetrisL.png", "Game/game/Assets/image/tetrisO.png", "Game/game/Assets/image/tetrisS.png", "Game/game/Assets/image/tetrisT.png", "Game/game/Assets/image/tetrisZ.png"]
TETROMINO_BRICK_FILEPATH = "Game/game/Assets/image/Border Square.png"
TEXT_COLOR = arcade.color.BLACK_LEATHER_JACKET
BOARD_COLORS = [arcade.color.DIM_GRAY, arcade.color.EGGPLANT, arcade.color.GOLDEN_BROWN, arcade.color.PURPUREUS, arcade.color.PUCE_RED, arcade.color.PEACH_ORANGE, arcade.color.YELLOW_ROSE, arcade.color.TEA_GREEN, arcade.color.BLUEBERRY, arcade.color.INDIGO]