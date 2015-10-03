__author__ = 'unit978'

import pygame
import sys
from pygame import Rect
from GameObject import GameObject
from MathUtil import Vector2
from random import randrange

# Initialize any modules that pygame uses.
pygame.init()

screen_size = (900, 500)

# Bits per pixel, 8 bits for each RGBA value.
bpp = 32
screen = pygame.display.set_mode(screen_size, pygame.HWSURFACE, bpp)

all_game_objects = list()

# MAKE THE PLAYER
player = GameObject()
player.position.x = screen_size[0]/2.0
player.position.y = screen_size[1] - 100
player.color = (255, 0, 0)
player.boundingBox = Rect(player.position.to_tuple(), (100, 20))
all_game_objects.append(player)

# MAKE THE BALL
ball = GameObject()
ball.tag = "ball"
ball.position.x = player.position.x
ball.position.y = player.position.y - 50
ball.velocity = Vector2(randrange(-100, 100), -150)
ball.color = (0, 255, 255)
ball.boundingBox = Rect(ball.position.to_tuple(), (10, 10))
all_game_objects.append(ball)

# MAKE THE BRICKS
brick_width = 60
brick_height = 30
total_bricks = 60

brick_x = 0.0
brick_y = 0.0

for i in range(1, total_bricks+1):
    brick = GameObject()
    brick.tag = "brick"
    brick.position = Vector2(brick_x, brick_y)
    brick.boundingBox = Rect(brick.position.to_tuple(), (brick_width, brick_height))
    all_game_objects.append(brick)

    # Calculate how many bricks fit along the width of the screen
    bricks_per_row = screen_size[0] / brick_width

    # Random Color
    r = randrange
    brick.color = (r(20, 255), r(20, 255), r(20, 255))

    brick_x += brick_width

    # Start a new row of bricks if they no longer fit within the screen width.
    if i % bricks_per_row == 0:  # alternate: if brick_x + brick_width > screen width
        brick_y += brick_height
        brick_x = 0

quit_game = False

delta_time = 0.0
last_frame_time = 0.0
timer = pygame.time.Clock()

while not quit_game:

    # Get the time in milliseconds.
    start_frame_time = pygame.time.get_ticks()

    # Get all events that were triggered and process them.
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quit_game = True

    # Make the player follow the mouse on the x-axis only.
    player.position.x = pygame.mouse.get_pos()[0]

    # Color the screen black.
    screen.fill((0, 0, 0))

    # Iterate backwards - much safer solution for iteration and removal at the same time.
    for i in xrange(len(all_game_objects) - 1, -1, -1):
        game_object = all_game_objects[i]
        game_object.update(delta_time)
        game_object.render(screen)

        # Check if ball collided with anything besides itself - avoid self collision
        if game_object.tag != ball.tag:

            # Check if bounding boxes intersect.
            if game_object.boundingBox.colliderect(ball.boundingBox):

                # make the ball respond to the collision
                ball.velocity.y *= -1

                # Remove bricks that collided with the ball.
                if game_object.tag == "brick":
                    del all_game_objects[i]

    # Reset ball over player if it goes past the bottom of the screen
    if ball.position.y > screen_size[1]:
        ball.position.x = player.position.x
        ball.position.y = player.position.y - 40

        # Make the ball go up
        ball.velocity.y *= -1.0

    # Make the ball bounce against the left and right sides of the screen.
    if ball.position.x <= 0 or ball.position.x + ball.boundingBox.width >= screen_size[0]:
        # Negate the x component of velocity
        ball.velocity.x *= -1.0

        # Apply collision resolution. Shift the ball outside the edges of the screen
        ##
        ##

    # Make the ball bounce against the top of the screen
    if ball.position.y <= 0:

        # Negate the y component of velocity.
        ball.velocity.y *= -1

    pygame.display.update()

    # Store how long the frame lasted in seconds.
    delta_time = (start_frame_time - last_frame_time) / 1000.0

    # Mark the time the frame ended, so we can later calculate delta time.
    last_frame_time = start_frame_time


# Un-initialize pygame modules.
pygame.quit()

# Kill the window.
sys.exit()