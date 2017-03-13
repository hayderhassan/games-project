## Class for levels

from __future__ import division
import pygame as pg
import os
from settings import *
from sprites import *
from os import path

class Level():
    def __init__(self, game, player, sprites):
        # Lists of sprites used in all levels
        self.all_sprites = sprites
        self.game = game

        # Background image
        self.background = None

        # How far this world has been scrolled left/right
        self.world_shift = 0
        self.level_limit = -1000

        self.player = player
       # print("levels.init()")


    def update(self):
        # Update everything on this level
        self.all_sprites.update()
        #print("levels.update()")



    def draw(self, screen):
        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(RED)

        screen.blit(self.background, (self.world_shift // 3, 0))

        # Draw all the sprite lists that we have
        self.all_sprites.draw(screen)

    def shift_world(self, shift_x):
        # Scroll screen when player moves left/right

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.all_sprites:
            platform.rect.x += shift_x




# Create platforms for the level
class Level_01(Level):

    def __init__(self, game, player, sprites):
        # Create Level 1

        # Call the parent constructor
        Level.__init__(self, game, player, sprites)
        print("level01.init()")

        self.dir = path.dirname(__file__)
        img_dir = path.join(self.dir, "img")
        self.background = pg.image.load(path.join(img_dir, "background_01.png"))
        self.background.set_colorkey(WHITE)
        self.level_limit = -2500

        for platform in LEVEL_ONE:
            Platform(self.game, platform[0], platform[1], platform[2])



