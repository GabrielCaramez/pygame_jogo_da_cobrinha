import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Snake settings
snake_size = 20
snake_color = white
snake_pos = [screen_width // 2, screen_height // 2]
snake_body = [snake_pos[:]]

# Apple settings
apple_size = 20
apple_color = red
apple_pos = [random.randrange(1, screen_width // apple_size) * apple_size,
             random.randrange(1, screen_height // apple_size) * apple_size]

# Game settings
direction = 'RIGHT'
change_to = direction
speed = 10

# Input buffer
input_buffer = []

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
            if key in ['up', 'down', 'left', 'right']:
                input_buffer.append(key)

    # Process input buffer
    if input_buffer:
        key = input_buffer.pop(0)
        if key == 'up' and direction != 'DOWN':
            change_to = 'UP'
        elif key == 'down' and direction != 'UP':
            change_to = 'DOWN'
        elif key == 'left' and direction != 'RIGHT':
            change_to = 'LEFT'
        elif key == 'right' and direction != 'LEFT':
            change_to = 'RIGHT'

    # Update direction
    direction = change_to

    # Update snake position
    if direction == 'UP':
        snake_pos[1] -= snake_size
    if direction == 'DOWN':
        snake_pos[1] += snake_size
    if direction == 'LEFT':
        snake_pos[0] -= snake_size
    if direction == 'RIGHT':
        snake_pos[0] += snake_size

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos == apple_pos:
        apple_pos = [random.randrange(1, screen_width // apple_size) * apple_size,
                     random.randrange(1, screen_height // apple_size) * apple_size]
    else:
        snake_body.pop()

    # Game Over conditions
    if (snake_pos[0] < 0 or snake_pos[0] >= screen_width or
            snake_pos[1] < 0 or snake_pos[1] >= screen_height):
        running = False
    for block in snake_body[1:]:
        if snake_pos == block:
            running = False

    # Refresh game screen
    screen.fill(black)
    for pos in snake_body:
        pygame.draw.rect(screen, snake_color, pygame.Rect(pos[0], pos[1], snake_size, snake_size))
    pygame.draw.rect(screen, apple_color, pygame.Rect(apple_pos[0], apple_pos[1], apple_size, apple_size))

    # Refresh rate
    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
sys.exit()