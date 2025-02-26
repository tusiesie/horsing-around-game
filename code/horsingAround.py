import pygame
import sys
from mainMenu import show_menu
from settingsMenu import show_settings
from pauseMenu import show_pause
from gameFunctions import show_game, show_saved, show_credits
from audioManager import AudioManager
from daoSave.characterStats import CharacterStats

from context import Context



class Game:
    def __init__(self):
        # Initialize Pygame
        pygame.init()
        ctx = Context() # initialize global context
        ctx.pygame_init(pygame)

        # Initialize audio manager
        self.sound = AudioManager()

        # Initialize save file
        self.stats = CharacterStats()

        # Set up the screen
        self.screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
        pygame.display.set_caption("Horsing Around")

        # Initialize current screen
        self.current_screen = "menu"
        # self.prev_screen = None


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
                self.stats.load_game()
                self.current_screen = show_saved(self.screen, self.stats)
            elif self.current_screen == "game":
                self.stats.reset_game()
                self.current_screen = show_game(self.screen, self.stats)
            elif self.current_screen == "settings":
                self.current_screen = show_settings(self.screen, "menu", self.sound)
            elif self.current_screen == "credits":
                self.current_screen = show_credits(self.screen)
            elif self.current_screen == "pause":
                self.current_screen = show_pause(self.screen)

            # Update the display
            pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()
