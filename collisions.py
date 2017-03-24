import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random
import math
from settings import *

class Interaction:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.border = 3

    def dot(u, v):
        return u[0] * v[0] + u[1] * v[1]

    def normal(self, center):
        left_dist = center[0]
        right_dist = self.width - center[0]
        top_dist = center[1]
        bottom_dist = self.height - center[1]
        if left_dist < min(right_dist, top_dist, bottom_dist):
            return (1, 0)
        elif right_dist < min(left_dist, top_dist, bottom_dist):
            return (-1, 0)
        elif top_dist < min(bottom_dist, left_dist, right_dist):
            return (0, 1)
        else:
            return (0, -1)

    def update(self):
        if not self.domain.inside(self.pos, self.radius):
            self.reflect()

    def reflect_Y(self):
        norm = self.domain.normal(self.pos)
        norm_length = dot(self.vel, norm)
        self.vel[1] = self.vel[1] - 2 * norm_length * norm[1]