__author__ = 'unit978'

from pygame import Rect
from pygame import draw
from Vector2 import Vector2


class GameObject:

    def __init__(self):

        self.position = Vector2()
        self.velocity = Vector2()

        self.boundingBox = Rect(0, 0, 1, 1)

        self.color = (255, 255, 255)

        self.tag = "object"

    def update(self, delta_time):

        # kinematics v = dr / dt

        # dr = v * dt

        # change in position = velocity * delta_time

        # new position = current position + change in position

        # current position = new pos.

        self.position += self.velocity * delta_time

        self.boundingBox.topleft = self.position.to_tuple()

    def render(self, screen):
        draw.rect(screen, self.color, self.boundingBox)