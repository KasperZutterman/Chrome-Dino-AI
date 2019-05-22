import random
from enum import Enum
import pygame as pg
from Game.Entity import Entity


class Bird(Entity):

    def __init__(self, x, y):
        super().__init__(x, y, BirdState.get_random_Bird(), (-1, 0))

    @staticmethod
    def hittable():
        return True

    def fly(self):
        if self.get_state() == BirdState.Bird1:
            self.set_state(BirdState.Bird2)
        else:
            self.set_state(BirdState.Bird1)


class BirdState(Enum):
    Bird1 = pg.image.load('Assets/bird_1.png'), (84, 60)
    Bird2 = pg.image.load('Assets/bird_2.png'), (84, 52)

    @staticmethod
    def get_random_Bird():
        chance = random.randint(0, 2)
        if chance == 0:
            return BirdState.Bird1
        else:
            return BirdState.Bird2
