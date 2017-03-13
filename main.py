# Main file to run game

from __future__ import division
import pygame as pg
import random
import os
from settings import *
from sprites import *
from levels import *
from os import path
from vectors import *

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
        self.score = 0
        #self.lives = 3

    def load_data(self):
        #define file directory as directory of main.py
        self.dir = path.dirname(__file__)
        print("load_data()")
        # Load images from img folder
        img_dir = path.join(self.dir, "img")
        self.character = Spritesheet(path.join(img_dir, CHARACTER))

        # Load buttons
        self.buttons = Spritesheet(path.join(img_dir, BUTTON_IMAGES))
        #self.yellowButton1 = self.buttons.get_image(0, 188, 190, 49, 1)
        #self.yellowButton1.set_colorkey(BLACK)

        # Load fonts
        font_dir = path.join(self.dir, "fonts")
        self.title_font = path.join(font_dir, "font1.ttf")

        # Load sounds from sound folder
        self.sound_dir = path.join(self.dir, "sound")
        #self.an_example_sound = pg.mixer.Sound(path.join(self.sound_dir, "sound_example.wav"))

    def new(self):
        # start a new game
        print("new()")
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)

        self.current_level = Level_01(g, self.player, self.all_sprites)


        self.run()

    def run(self):
        #print("run()")
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        #print("update()")
        # Game Loop - Update
        #self.all_sprites.update()
        self.current_level.update()
        #

        # Check if player hits a platform, only if falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
                self.player.jumping = False
                # See if we are on the ground.
                if 5 == 6:
                    if self.player.rect.midbottom >= HEIGHT - 64 and self.player.vel.y >= 0:
                        self.player.vel.y = 0
                        self.player.pos.y = HEIGHT - 64
                    lowest = hits[0]
                    for hit in hits:
                        if hit.rect.bottom > lowest.rect.bottom:
                            lowest = hit
                    if self.player.pos.x < lowest.rect.right + 10 and \
                        self.player.pos.x > lowest.rect.left + 10:
                        if self.player.pos.y < lowest.rect.centery:
                            self.player.pos.y = lowest.rect.top
                            self.player.vel.y = 0
                            self.player.jumping = False

        # Check if player hits the side of a platform
        # See if we hit anything

        hits = pg.sprite.spritecollide(self.player, self.platforms, False)

        for hit in hits:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if hit.rect.bottom == HEIGHT - 64:
                if self.player.vel.x >= 0:
                    self.player.rect.right = hit.rect.left
                elif self.player.vel.x <= 0:
                    # Otherwise if we are moving left, do the opposite.
                    self.player.rect.left = hit.rect.right

        # If player falls and dies
        if self.player.rect.bottom > HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y, 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()
        if len(self.platforms) == 0:
            #self.lives -= 1
            self.playing = False

        # If the player gets near the right side, shift the world left (-x)
        if self.player.rect.right >= 500:
            diff = self.player.rect.right - 500
            print("player.rect.right: " + str(self.player.rect.right))
            print("diff: " + str(diff))
            print("player.vel.x: " + str(self.player.vel.x))
            self.player.rect.right = 500
            self.current_level.shift_world(-diff)


        # If the player gets near the left side, shift the world right (+x)
        if self.player.rect.left <= 120:
            diff = 120 - self.player.rect.left
            self.player.rect.left = 120
            self.current_level.shift_world(diff)


    def events(self):
       # print("events()")
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                #if self.playing:
                 #   self.playing = False
                self.running = False

            # Check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

            # Check if user presses space to jump
            if event.type == pg.KEYUP:
                if event.key == pg.K_UP:
                    self.player.jump_cut()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.player.jump()
                if event.key == pg.K_ESCAPE:
                    print("Esc")
                    self.running = False
                    self.playing = False

    def draw(self):
       # print("draw()")
        # Game Loop - draw

        self.current_level.draw(self.screen)

        #self.screen.fill(BG_COLOUR)
        #self.current_level.all_sprites.draw(self.screen)
        #draw sprites onto screen:
        #self.all_sprites.draw(self.screen)

        # *after* drawing everything, flip the display - nothing else should go below this line
        pg.display.flip()

    def show_start_screen(self):
        # game start screen
        print("show start screen()")
        self.screen.fill(BG_COLOUR)
        self.draw_text(TITLE, 30, BLACK, 400, 100)
        self.draw_text("Use the arrow keys to move", 20, BLACK, 400, 200)
        self.draw_button("Start", 300, 340)
        self.draw_button("Exit", 300, 400)

        # *after* drawing everything, flip the display - nothing else should go below this line
        pg.display.flip()

    def show_go_screen(self):
        # game over/continue
        print("show game over screen()")
        g.events()
        self.screen.fill(BG_COLOUR)

        self.draw_text("Game Over", 30, BLACK, 400, 100)
        self.draw_text("Score: " + str(self.score), 20, BLACK, 400, 200)
        self.draw_button("Play Again", 300, 280)
        self.draw_button("Menu", 300, 340)
        self.draw_button("Exit", 300, 400)

        pg.display.flip()

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
#while g.running:
    #g.show_start_screen()
    #g.show_go_screen()
#    g.draw()

while g.running:
    g.new()
#    g.show_go_screen()

pg.quit()
