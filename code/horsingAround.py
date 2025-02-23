import pygame
import sys
from mainMenu import show_menu
from settingsMenu import show_settings
from audioManager import AudioManager


class Game:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Initialize audio manager
        self.sound = AudioManager()

        # Set up the screen
        self.screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
        pygame.display.set_caption("Horsing Around")

        # Initialize current screen
        self.current_screen = "menu"

    def run(self):
        # Game Loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Check which screen to show
            if self.current_screen == "menu":
                self.current_screen = show_menu(self.screen)
            elif self.current_screen == "saved_game":
                self.current_screen = show_saved(self.screen)
            elif self.current_screen == "game":
                self.current_screen = show_game(self.screen)
            elif self.current_screen == "settings":
                self.current_screen = show_settings(self.screen, self.current_screen, self.sound)
            elif self.current_screen == "credits":
                self.current_screen = show_credits(self.screen)

            # Update the display
            pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()