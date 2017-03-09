# Sprite classes for platform game (main.py)
# example
from __future__ import division
import pygame as pg
import random
from settings import *

class Spritesheet:
    def __init__(self, filename):
        # load new spritesheet
        self.spritesheet = pg.image.load(filename).convert()

    def get_image(self, x, y, width, height, scale):
        # take image from larger spritesheet
        image = pg.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        image = pg.transform.scale(image, (width // scale, height // scale))
        return image

class Player(pg.sprite.Sprite):
    #player sprite
    pass

class Platform(pg.sprite.Sprite):
    #platform sprite
    pass

class Enemy(pg.sprite.Sprite):
    #enemy sprite
    pass
