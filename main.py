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
        self.back_to_home = False
        self.home_screen = False
        self.game_over_screen = False
        self.score = 0
        self.lives = 3

    #    self.current_level_no = 0

    def load_data(self):
        #define file directory as directory of main.py
        self.dir = path.dirname(__file__)
        print("load_data()")
        # Load images from img folder
        img_dir = path.join(self.dir, "img")
        self.character = Spritesheet(path.join(img_dir, CHARACTER))

        # Load buttons
        self.buttons = Spritesheet(path.join(img_dir, BUTTON_IMAGES))
        self.yellowButton1 = self.buttons.get_image(YELLOW_BUTTON1, 1)
        self.yellowButton1.set_colorkey(BLACK)

        # Load fonts
        font_dir = path.join(self.dir, "fonts")
        self.title_font = path.join(font_dir, "font1.ttf")

        # Load sounds from sound folder
        self.sound_dir = path.join(self.dir, "sound")
        #self.an_example_sound = pg.mixer.Sound(path.join(self.sound_dir, "sound_example.wav"))

        # Pause screen
        self.dim_screen = pg.Surface(self.screen.get_size()).convert_alpha()
        self.dim_screen.fill((0, 0, 0, 180))

    def new(self):
        # start a new game
        print("new()")
        self.paused = False
        self.back_to_home = False
        self.game_over_screen = False
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)

        # Create all the levels
#        self.level_list = []
#        self.level_list.append((Level_1(g, self.player, self.all_sprites)))
#        self.level_list.append((Level_2(g, self.player, self.all_sprites)))

        # Set the current level
#        self.current_level_no = 1
#        self.current_level = self.level_list[self.current_level_no]
#        print("current_level_no = " + str(self.current_level_no))
#        print("level_list = " + str(self.level_list))



        self.current_level = Level_1(g, self.player, self.all_sprites)

     #   self.current_level_no += 1
    #    self.level = "Level_" + str(self.current_level_no)
     #   print(self.level)
     #   self.current_level = self.level(g, self.player, self.all_sprites)
     #   print(self.current_level)
        self.run()

    def run(self):
        print("run()")
        # Game Loop
        self.playing = True

        while self.playing:
            self.clock.tick(FPS)
            self.events()
            if not self.paused:
                self.update()
                #print("run() total lives: " + str(self.lives))
                print("current world shift: " + str(self.current_level.world_shift))
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
            self.lives -= 1
            self.playing = False

        # If the player gets near the right side, shift the world left (-x)
        if self.player.pos.x > 500 and abs(self.player.vel.x) > 0:
            shift = self.player.pos.x - 500
            self.player.pos.x = 500
            self.current_level.shift_world(-shift)


        # If the player gets near the left side, shift the world right (+x)
        if self.player.pos.x <= 300 and self.player.vel.x < 0:
            shift = 300 - self.player.pos.x
            self.player.pos.x = 300
            self.current_level.shift_world(shift)

        if 5 == 5:
            # If the player gets to the end of the level, go to the next level
            current_position = self.player.rect.x + self.current_level.world_shift
            print("Current position: " + str(current_position))
            if current_position < self.current_level.level_limit:
                self.player.rect.x = 120
                self.current_level = Level_2(g, self.player, self.all_sprites)
#                if self.current_level_no < len(self.level_list) - 1:
#                    self.current_level_no += 1
#                    self.current_level = self.level_list[self.current_level_no]
#                    #self.player.level = self.current_level

    def events(self):
       # print("events()")
        # Game Loop - events
        for event in pg.event.get():

            pos = pg.mouse.get_pos()
            x = pos[0]
            y = pos[1]

            continue_button = (x >= 300 and x <= 490) and (y >= 220 and y <= 270)
            restart_button = (x >= 300 and x <= 490) and (y >= 280 and y <= 330)
            home_button = (x >= 300 and x <= 490) and (y >= 340 and y <= 390)
            exit_button = (x >= 300 and x <= 490) and (y >= 400 and y <= 450)

            # check for closing window
            if event.type == pg.QUIT:
                #if self.playing:
                 #   self.playing = False
                self.running = False

            # Check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.lives = 0
                    self.playing = False
                self.running = False

            # Check if user presses space to jump
            if event.type == pg.KEYUP:
                if event.key == pg.K_UP:
                    self.player.jump_cut()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.player.jump()

                # check if game is paused
                if event.key == pg.K_p:
                    self.paused = not self.paused

                # check if "ESC" has been pressed to quit
                if event.key == pg.K_ESCAPE:
                    print("Esc")
                    if self.playing:
                        self.lives = 0
                        self.playing = False
                    self.running = False

            if event.type == pg.MOUSEBUTTONDOWN and self.paused:
                print(str(x) + ", " + str(y))
                if continue_button:
                    self.paused = False
                if restart_button:
                    self.lives = 3
                    self.score = 0
                    self.playing = False
                if home_button:
                    self.lives = 0
                    self.score = 0
                    self.playing = False
                    self.back_to_home = True
                if exit_button:
                    self.lives = 0
                    self.playing = False
                    self.running = False

    def draw(self):
       # print("draw()")
        # Game Loop - draw

        self.current_level.draw(self.screen)
#        print("Level " + str(self.current_level_no))
        #self.screen.fill(BG_COLOUR)
        #self.current_level.all_sprites.draw(self.screen)
        #draw sprites onto screen:
 #       self.all_sprites.draw(self.screen)

        self.draw_text("Score: " + str(self.score), 22, BLACK, (WIDTH / 4), 15)
        self.draw_text("Lives: " + str(self.lives), 22, BLACK, (WIDTH * (3 / 4)), 15)

        if self.paused:
            self.screen.blit(self.dim_screen, (0, 0))
            self.draw_text("Paused", 40, WHITE, WIDTH / 2, HEIGHT / 4)
            self.draw_button("Continue", 300, (HEIGHT * (4 / 5)) - 180)
            self.draw_button("Restart", 300, (HEIGHT * (4 / 5)) - 120)
            self.draw_button("Home", 300, (HEIGHT * (4 / 5)) - 60)
            self.draw_button("Exit", 300, ((HEIGHT * (4 / 5))))

        # *after* drawing everything, flip the display - nothing else should go below this line
        pg.display.flip()

    def wait_for_user(self):
        # wait for user to make choice

        waiting = True
        while waiting:
            self.clock.tick(FPS)

            pos = pg.mouse.get_pos()
            x = pos[0]
            y = pos[1]

            play_again_button = (x >= 300 and x <= 488) and (y >= 280 and y <= 330)
            play_button = (x >= 300 and x <= 488) and (y >= 340 and y <= 390)
            home_button = (x >= 300 and x <= 488) and (y >= 340 and y <= 390)
            exit_button = (x >= 300 and x <= 488) and (y >= 400 and y <= 450)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.lives = 0
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    if event.key == pg.K_ESCAPE:
                        self.lives = 0
                        waiting = False
                        self.running = False

                # Game over screen
                if event.type == pg.MOUSEBUTTONDOWN and self.game_over_screen:
                    print(str(x) + ", " + str(y))
                    if play_again_button:
                        self.lives = 3
                        self.score = 0
                        self.game_over_screen = False
                        waiting = False
                        self.playing = True

                    if home_button:
                        self.game_over_screen = False
                        waiting = False
                        self.back_to_home = True

                    if exit_button:
                        self.lives = 0
                        self.game_over_screen = False
                        waiting = False
                        self.running = False

                # Home screen
                if event.type == pg.MOUSEBUTTONDOWN and self.home_screen:
                    print(str(x) + ", " + str(y))
                    if play_button:
                        waiting = False
                    if exit_button:
                        self.lives = 0
                        waiting = False
                        self.running = False

    def show_start_screen(self):
        # game start screen
        print("show start screen()")

        self.home_screen = True
        self.score = 0
        self.lives = 3

        self.screen.fill(BG_COLOUR)
        self.draw_text(TITLE, 30, BLACK, 400, 100)
        self.draw_text("Use the arrow keys to move", 20, BLACK, 400, 200)
        self.draw_button("Play", 300, 340)
        self.draw_button("Exit", 300, 400)

        # *after* drawing everything, flip the display - no other drawings/text should go below this line
        pg.display.flip()

        self.wait_for_user()
        self.home_screen = False

    def show_go_screen(self):
        # game over/continue
        print("show game over screen()")

        if not self.running:
            return

        self.game_over_screen = True

        self.screen.fill(BG_COLOUR)
        self.draw_text("GAME OVER", 50, WHITE, WIDTH / 2, (HEIGHT / 4) - 40)
        self.draw_text("Score: " + str(self.score), 22, WHITE, WIDTH / 2, (HEIGHT / 3) + 50)

        self.draw_button("Play Again", 300, 280)
        self.draw_button("Home", 300, 340)
        self.draw_button("Exit", 300, 400)

        pg.display.flip()

        self.wait_for_user()

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
g.show_start_screen()

while g.running:
    while g.lives > 0:
        g.new()
    if not g.back_to_home:
        g.show_go_screen()
    else:
        g.show_start_screen()

pg.quit()
