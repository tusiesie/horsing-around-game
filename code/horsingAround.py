import pygame
import sys
import os
from mainMenu import show_menu

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.display.set_caption("My Game")

# Initialize current screen
current_screen = "menu"

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Check which screen to show
    if current_screen == "menu":
        current_screen = show_menu(screen)
    elif   current_screen == "saved_game":
        current_screen = show_saved(screen)
    elif current_screen == "game":
        current_screen = show_game(screen)
    elif current_screen == "settings":
        current_screen = show_settings(screen)
    elif current_screen == "credits":
        current_screen = show_credits(screen)

    # Update the display
    pygame.display.flip()
