import pygame
import sys
import os

from gameFunctions import change_screen

# load assets
assets_folder = os.path.join(os.path.dirname(__file__), '../assets/visuals/mainMenu')
background_image = pygame.image.load(os.path.join(assets_folder, 'bg.png'))
background_image = pygame.transform.scale(background_image, (1530, 860))

image_continue = pygame.image.load(os.path.join(assets_folder, 'continueButt.png'))
image_newgame = pygame.image.load(os.path.join(assets_folder, 'newGameButt.png'))
image_settings = pygame.image.load(os.path.join(assets_folder, 'settingsButt.png'))
image_credits = pygame.image.load(os.path.join(assets_folder, 'creditsButt.png'))
image_quit = pygame.image.load(os.path.join(assets_folder, 'quitButt.png'))

image_continue_hovered = pygame.image.load(os.path.join(assets_folder, 'continueButtHover.png'))
image_newgame_hovered = pygame.image.load(os.path.join(assets_folder, 'newGameButtHover.png'))
image_settings_hovered = pygame.image.load(os.path.join(assets_folder, 'settingsButtHover.png'))
image_credits_hovered = pygame.image.load(os.path.join(assets_folder, 'creditsButtHover.png'))
image_quit_hovered = pygame.image.load(os.path.join(assets_folder, 'quitButtHover.png'))



def show_menu(screen):
    button_continue = Button(100, 400, image_continue, image_continue_hovered, action=lambda: change_screen('game', screen, background_image))
    button_newgame = Button(100, 475, image_newgame, image_newgame_hovered, action=lambda: change_screen('game', screen, background_image))
    button_settings = Button(100, 550, image_settings, image_settings_hovered, action=lambda: change_screen('settings', screen, background_image))
    button_credits = Button(100, 625, image_credits, image_credits_hovered, action=lambda: change_screen('settings', screen, background_image))
    button_quit = Button(100, 700, image_quit, image_quit_hovered, action=sys.exit)

    # fill background
    screen.blit(background_image, (2, 3))

    button_continue.draw(screen)
    button_newgame.draw(screen)
    button_settings.draw(screen)
    button_credits.draw(screen)
    button_quit.draw(screen)


    if button_continue.is_clicked():
        return "saved_game"
    elif button_newgame.is_clicked():
        return "game"
    elif button_settings.is_clicked():
        return "settings"
    elif button_credits.is_clicked():
        return "credits"
    elif button_quit.is_clicked():
        return None
    
    return "menu"

class Button:
    def __init__(self, x, y, image_normal, image_hovered, action=None):
        self.rect = image_normal.get_rect(topleft=(x, y))
        self.image_normal = image_normal
        self.image_hovered = image_hovered
        self.action = action

    def draw(self, surface):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            surface.blit(self.image_hovered, self.rect.topleft)
        else:
            surface.blit(self.image_normal, self.rect.topleft)

    def is_clicked(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            if self.action:
                self.action()
            return True
        return False
