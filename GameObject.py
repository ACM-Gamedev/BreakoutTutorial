__author__ = 'unit978'

from MathUtil import Vector2
from pygame import Rect, draw


class GameObject:

    def __init__(self):
        self.position = Vector2(0, 0)
        self.velocity = Vector2(0, 0)

        # RGB
        self.color = (255, 255, 255)
        self.boundingBox = Rect(0, 0, 1, 1)

        self.tag = "gameobject"

    # Update the game object at every delta_time interval.
    def update(self, delta_time):

        # Kinematics: v = dr / dt
        # dr = v * dt
        # -------------------------------------------
        # delta pos = vel * dt
        # new position = current position + delta pos
        # current position = new position
        self.position += self.velocity * delta_time

        # Update the position of the bounding box so it goes with the game object.
        self.boundingBox.topleft = self.position.to_tuple()

    # Render to screen.
    def render(self, screen):
        draw.rect(screen, self.color, self.boundingBox)