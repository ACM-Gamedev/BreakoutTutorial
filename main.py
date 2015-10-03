__author__ = 'unit978'


import pygame
import sys

from GameObject import GameObject
from Vector2 import Vector2
from random import randrange

pygame.init()

screen_size = (730, 500)

screen = pygame.display.set_mode(screen_size, pygame.HWSURFACE, 32)


all_game_objects = list()

player = GameObject()
player.position.x = screen_size[0] / 2
player.position.y = screen_size[1] - 100
player.boundingBox.width = 150
player.boundingBox.height = 50
player.color = (255, 0, 0)

player.velocity = Vector2(0, 0)
all_game_objects.append(player)

ball = GameObject()
ball.tag = "ball"
ball.position.x = player.position.x
ball.position.y = player.position.y - 100
ball.boundingBox.width = 10
ball.boundingBox.height = 10
ball.velocity = Vector2(100, -100)
ball.color = (100, 100, 200)
all_game_objects.append(ball)

brick_width = 70
brick_height = 30
brick_count = 60

bricks_per_row = screen_size[0] / brick_width

brick_x = 0
brick_y = 0

r = randrange

for i in range(1, brick_count + 1):

    brick = GameObject()
    brick.tag = "brick"
    brick.position = Vector2(brick_x, brick_y)
    brick.boundingBox.width = brick_width
    brick.boundingBox.height = brick_height
    all_game_objects.append(brick)

    brick.color = (r(20, 255), r(20, 255), r(20, 255))

    brick_x += brick_width

    #if i % bricks_per_row == 0:
     #   brick_x = 0
      #  brick_y += brick_height

    if brick_x + brick_width > screen_size[0]:
        brick_x = 0
        brick_y += brick_height


delta_time = 0.0
last_frame_time = 0.0

timer = pygame.time.Clock()

while True:

    # Get the time in milliseconds
    start_frame_time = pygame.time.get_ticks()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Make the X pos of player the same as the x mouse
    # move left to right , vice versa
    player.position.x = pygame.mouse.get_pos()[0]

    screen.fill((0, 0, 0))

    for game_object in all_game_objects:
        game_object.update(delta_time)
        game_object.render(screen)

        if game_object.tag != ball.tag:

            if game_object.boundingBox.colliderect(ball.boundingBox):

                if game_object.tag == "brick":
                    all_game_objects.remove(game_object)

                ball.velocity.y *= -1

    # Make ball collide with left/right side of the screen
    if ball.position.x <= 0 or ball.position.x + ball.boundingBox.width > screen_size[0]:
        ball.velocity.x *= -1.0

    if ball.position.y <= 0:
        ball.velocity.y *= -1.0

    # Restart ball over the player
    if ball.position.y >= screen_size[1]:
        ball.position.x = player.position.x
        ball.position.y = player.position.y - 100
        ball.velocity.y *= -1.0


    pygame.display.update()

    # record delta time in seconds - how much the frame took to finish
    delta_time = (start_frame_time - last_frame_time) / 1000.0
    last_frame_time = start_frame_time
