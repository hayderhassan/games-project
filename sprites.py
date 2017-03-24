# Sprite classes for platform game (main.py)

from __future__ import division
import pygame as pg
import random
import os
from os import path
from settings import *
from vectors import *

class Spritesheet:
    def __init__(self, filename):
        #print("Spritesheet()")
        # load new spritesheet
        self.spritesheet = pg.image.load(filename).convert()

    def get_image(self, picture, scale):
        #print("Spritesheet.get_image()")
        x = picture[0]
        y = picture[1]
        width = picture[2]
        height = picture[3]
        # take image from larger spritesheet
        image = pg.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        image = pg.transform.scale(image, (width // scale, height // scale))
        return image

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        #print("Player()")
        self._layer = PLAYER_LAYER
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.walking = False
        self.jumping = False
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.image = self.standing_frame[0]
        self.rect = self.image.get_rect()
        self.rect.center = (153, 300)
        self.pos = Vector((153, 300))
        self.vel = Vector((0, 0))
        self.acc = Vector((0, 0))


    def update(self):
        #print("Player.update()")
        self.animate()
        self.acc = Vector((0, PLAYER_GRAV))


        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel.x += self.acc.x
        self.vel.y += self.acc.y
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        self.pos.x += self.vel.x + 0.5 * self.acc.x
        self.pos.y += self.vel.y + 0.5 * self.acc.y

        self.rect.midbottom = self.pos.getP()

    def load_images(self):
        #print("Player.load_images()")
        self.standing_frame = [self.game.character.get_image(STANDING1, 2), self.game.character.get_image(STANDING2, 2)]
        for frame in self.standing_frame:
            frame.set_colorkey(BLACK)

        self.walk_frames_right = [self.game.character.get_image(WALK_RIGHT1, 2), self.game.character.get_image(WALK_RIGHT2, 2)]
        for frame in self.walk_frames_right:
            frame.set_colorkey(BLACK)

        self.walk_frames_left = [self.game.character.get_image(WALK_LEFT1, 2), self.game.character.get_image(WALK_LEFT2, 2)]
        for frame in self.walk_frames_left:
            frame.set_colorkey(BLACK)

        self.jump_frame = self.game.character.get_image(JUMP, 2)
        self.jump_frame.set_colorkey(BLACK)

    def jump(self):
        #print("Player.jump()")
        # jump only if standing on a platform
        self.rect.x += 2
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 2
        if hits and not self.jumping:
            #self.game.jump_sound.play()
            self.jumping = True
            self.vel.y = -PLAYER_JUMP

    def jump_cut(self):
        #print("Player.jump_cut()")
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3

    def animate(self):
        #print("Player.animate()")
        now = pg.time.get_ticks()
        if self.vel.x != 0:
            self.walking = True
        else:
            self.walking = False

        # show walking animation
        if self.walking:
            if now - self.last_update > 200:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.walk_frames_left)
                bottom = self.rect.bottom
                if self.vel.x > 0:
                    self.image = self.walk_frames_right[self.current_frame]
                else:
                    self.image = self.walk_frames_left[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom

        # show standing animation
        if not self.jumping and not self.walking:
            if now - self.last_update > 400:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.standing_frame)
                bottom = self.rect.bottom
                self.image = self.standing_frame[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom

        self.mask = pg.mask.from_surface(self.image)

class Coin(pg.sprite.Sprite):
    def __init__(self, game, picture, x, y):
        self._layer = PLATFORM_LAYER
        self.dir = path.dirname(__file__)
        img_dir = path.join(self.dir, "img")
        self.coin = Spritesheet(path.join(img_dir, COIN))
        self.groups = game.all_sprites, game.coins
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = self.coin.get_image(COIN_ICON, 8)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Platform(pg.sprite.Sprite):
    def __init__(self, game, picture, x, y):
        #print("Platform()")
        self._layer = PLATFORM_LAYER
        self.dir = path.dirname(__file__)
        img_dir = path.join(self.dir, "img")
        self.platforms = Spritesheet(path.join(img_dir, PLATFORMS))
        self.groups = game.all_sprites, game.platforms
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = self.platforms.get_image(picture, 1)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
       # if random.randrange(100) < POWER_SPAWN:
        #    Power(self.game, self)

class Enemy(pg.sprite.Sprite):
    #enemy sprite
    pass
