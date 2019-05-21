import pygame as pg


class Entity:

    def __init__(self, x, y, state=0, speed=(0, 0)):
        self.__state = state
        self.__hitbox = pg.Rect((x, y), self.get_dim())
        self.__speed = speed

    def move(self, x_var, y_var):
        self.__hitbox.move_ip(x_var, y_var)

    def auto_move(self):
        self.__hitbox.move_ip(self.__speed[0], self.__speed[1])

    def intersects(self, entity):
        return self.__hitbox.colliderect(entity.get_hitbox())

    def set_location(self, x, y):
        self.__hitbox.move_ip(x - self.__hitbox.x, y - self.__hitbox.y)

    def set_state(self, state):
        self.__state = state

    def get_state(self):
        return self.__state

    def get_speed(self):
        return self.__speed

    def set_speed(self, x, y):
        self.__speed = (x, y)

    def get_hitbox(self):
        return self.__hitbox

    def get_dim(self):
        return self.__state.value[1]

    def get_location(self):
        return self.__hitbox.topleft

    def get_image(self):
        return self.__state.value[0]
