# Main file to run game

from __future__ import division
import pygame as pg
import random
import os
from settings import *
from sprites import *
from os import path

os.environ['SDL_VIDEO_CENTERED'] = '1'

class Game:
    def __init__(self):
        # initialize game window, etc
        print("initialise game")
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)
        self.load_data()
        #self.back_to_home = False
        #self.home_screen = False
        #self.game_over_screen = False
        #self.score = 0
        #self.lives = 3

    def load_data(self):
        #define file directory as directory of main.py
        self.dir = path.dirname(__file__)

        # Load images from img folder
        img_dir = path.join(self.dir, "img")
        #self.spritesheet = Spritesheet(path.join(img_dir, SPRITESHEET))

        # Load buttons
        self.buttons = Spritesheet(path.join(img_dir, BUTTON_IMAGES))
        self.yellowButton1 = self.buttons.get_image(0, 188, 190, 49, 1)
        self.yellowButton1.set_colorkey(BLACK)

        # Load fonts
        font_dir = path.join(self.dir, "fonts")
        self.title_font = path.join(font_dir, "font1.ttf")

        # Load sounds from sound folder
        self.sound_dir = path.join(self.dir, "sound")
        #self.an_example_sound = pg.mixer.Sound(path.join(self.sound_dir, "sound_example.wav"))

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                #if self.playing:
                 #   self.playing = False
                self.running = False

    def draw(self):
        # Game Loop - draw
        self.screen.fill(BLACK)
        #draw sprites onto screen:
        #self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display - nothing else should go below this line
        pg.display.flip()

    def show_start_screen(self):
        # game start screen
        print("show start screen")
        g.events()
        self.screen.fill(BG_COLOUR)

        # These are just examples of how to draw text and add buttons:
        self.draw_text(TITLE, 30, RED, 300, 200)
        self.draw_button("Play", 300, 400)

        # *after* drawing everything, flip the display - nothing else should go below this line
        pg.display.flip()

    def show_go_screen(self):
        # game over/continue
        pass

    def draw_text(self, text, size, colour, x, y):
        font = pg.font.Font(self.title_font, size)
        text_surface = font.render(text, True, colour)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def draw_button(self, text, x, y):
        self.screen.blit(self.yellowButton1, (x, y))
        self.draw_text(text, 22, BLACK, x + 90, y + 10)

print("start")
g = Game()
print("finish initialising game and show start screen")
while g.running:
    g.show_start_screen()

#while g.running:
#    g.new()
#    g.show_go_screen()

pg.quit()