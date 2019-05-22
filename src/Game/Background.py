import pygame as pg

from Game.Entity import Entity


class Background(Entity):

    def __init__(self, x, y):
        self.__res = (x, y)
        self.__background = pg.image.load('Assets/background.png')
        super().__init__(x, y)

    @staticmethod
    def hittable():
        return False

    def reset(self):
        self.set_location(self.__res[0], self.__res[1])

    def get_image(self):
        return self.__background

    def get_dim(self):
        return self.__background.get_size()
