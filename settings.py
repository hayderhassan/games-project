# game options/settings
TITLE = "Platform Game"
WIDTH = 800
HEIGHT = 500
FPS = 60
FONT_NAME = "arial"

# Sprites
BUTTON_IMAGES = "yellow_buttons.png"
KEYS = "arrows.png"
PLATFORMS = "sprites_Tiles.png"
CHARACTER = "character_sprites.png"

YELLOW_BUTTON1 = ([0, 188, 190, 49])

BACKGROUND1_IMG = "background_01.png"
BACKGROUND1 = ([0, 0, 2100, 600])

GRASS_LEFT = ([66, 598, 64, 64])
GRASS_RIGHT = ([66, 532, 64, 64])
GRASS_CENTRE = ([66, 664, 64, 64])

GRASS_HALF_CENTRE = ([132, 462, 64, 32])
GRASS_HALF_ROUND = ([132, 496, 64, 32])
GRASS_HALF_RIGHT = ([132, 530, 64, 32])
GRASS_HALF_LEFT = ([132, 564, 64, 32])

STANDING1 = ([404, 1157, 132, 161])
STANDING2 = ([404, 992, 132, 163])
WALK_RIGHT1 = ([673, 334, 120, 161])
WALK_RIGHT2 = ([917, 166, 120, 161])
WALK_LEFT1 = ([1039, 166, 120, 162])
WALK_LEFT2 = ([1039, 330, 120, 162])
JUMP = ([135, 1007, 133, 163])

# Levels

# Platforms for level 1
# Array with type of platform, and x, y location of the platform.
LEVEL_ONE = ([(GRASS_HALF_LEFT, ((WIDTH / 2) - 100), (HEIGHT / 2)),
              (GRASS_LEFT, ((WIDTH / 2) - 36), (HEIGHT - 128)),
              (GRASS_HALF_CENTRE, ((WIDTH / 2) - 36), (HEIGHT / 2)),
              (GRASS_HALF_RIGHT, ((WIDTH / 2) + 28), (HEIGHT / 2)),
              (GRASS_HALF_LEFT, ((WIDTH / 2) + 192), (HEIGHT / 2) - 40),
              (GRASS_HALF_RIGHT, ((WIDTH / 2) + 256), (HEIGHT / 2) - 40),
              (GRASS_HALF_LEFT, ((WIDTH / 2) + 392), (HEIGHT / 2)),
              (GRASS_HALF_RIGHT, ((WIDTH / 2) + 456), (HEIGHT / 2)),
              (GRASS_HALF_LEFT, ((WIDTH / 2) + 532), (HEIGHT / 2) + 20),
              (GRASS_HALF_RIGHT, ((WIDTH / 2) + 596), (HEIGHT / 2) + 20),
              (GRASS_HALF_LEFT, ((WIDTH / 2) + 800), (HEIGHT / 2) - 40),
              (GRASS_HALF_RIGHT, ((WIDTH / 2) + 864), (HEIGHT / 2) - 40)
              ])

# Ground for level 1
for i in range(0, WIDTH * 2, 64):
    LEVEL_ONE.append((GRASS_CENTRE, i, HEIGHT - 64))

for i in range((WIDTH*2) + 70, WIDTH*4, 140):
    LEVEL_ONE.append((GRASS_CENTRE, i, HEIGHT - 64))

for i in range((WIDTH*4) + 70, WIDTH*6, 64):
    LEVEL_ONE.append((GRASS_CENTRE, i, HEIGHT - 64))


# Platforms for level 2

LEVEL_TWO = ([(GRASS_HALF_LEFT, ((WIDTH / 2) - 100), (HEIGHT / 2)),
              (GRASS_HALF_CENTRE, ((WIDTH / 2) - 36), (HEIGHT / 2)),
              (GRASS_HALF_RIGHT, ((WIDTH / 2) + 28), (HEIGHT / 2))
              ])

# Ground for level 2
for i in range(0, WIDTH, 64):
    LEVEL_TWO.append((GRASS_CENTRE, i, HEIGHT - 64))

# Player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 22

# Game settings
PLAYER_LAYER = 2
PLATFORM_LAYER = 1


# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (102, 102, 0)
DARK_GREEN = (34, 139, 34)
RED = (255, 0, 0)
BROWN = (102, 51, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHT_BLUE = (0, 155, 155)
BG_COLOUR = LIGHT_BLUE

