from enum import Enum
import pygame as pg
from Game.Entity import Entity


class Cloud(Entity):

    def __init__(self, x, y):
        super().__init__(x, y, CloudState.get_cloud(), (-1, 0))

    @staticmethod
    def hittable():
        return False


class CloudState(Enum):
    CLOUD = pg.image.load('Assets/cloud.png'), (50, 100)

    @staticmethod
    def get_cloud():
        return CloudState.CLOUD
