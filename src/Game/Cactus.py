import random
from enum import Enum
import pygame as pg
from Game.Entity import Entity


class Cactus(Entity):

    def __init__(self, x, y):
        super().__init__(x, y, CactusState.get_random_cactus(), (-1, 0))

    @staticmethod
    def hittable():
        return True


class CactusState(Enum):
    CACTUS1 = pg.image.load('Assets/cactus_1.png'), (46, 96)
    CACTUS2 = pg.image.load('Assets/cactus_2.png'), (98, 96)

    @staticmethod
    def get_random_cactus():
        chance = random.randint(0, 2)
        if chance == 0:
            return CactusState.CACTUS1
        else:
            return CactusState.CACTUS2
