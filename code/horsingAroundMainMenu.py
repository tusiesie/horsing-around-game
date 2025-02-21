import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.display.set_caption("My Game")

# load assets
assets_folder = os.path.join(os.path.dirname(__file__), '../assets/visuals/mainMenu')
background_image = pygame.image.load(os.path.join(assets_folder, 'bg.png'))

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # fill background
    background_image = pygame.transform.scale(background_image, (1530, 860))
    screen.blit(background_image, (2, 3))

    # Update the display
    pygame.display.flip()