import pygame
import sys
import os

from gameFunctions import change_screen

# Load assets
assets_folder = os.path.join(os.path.dirname(__file__), '../assets/visuals/pauseMenu')
background_image = pygame.image.load(os.path.join(assets_folder, 'pauseBG.png'))
background_image = pygame.transform.scale(background_image, (1530, 860))

image_resume = pygame.image.load(os.path.join(assets_folder, 'resumeButt.png'))
image_settings = pygame.image.load(os.path.join(assets_folder, 'settingsButt.png'))
image_title = pygame.image.load(os.path.join(assets_folder, 'titleScreenButt.png'))


image_resume_hovered = pygame.image.load(os.path.join(assets_folder, 'resumeButtHover.png'))
image_settings_hovered = pygame.image.load(os.path.join(assets_folder, 'settingsButtHover.png'))
image_title_hovered = pygame.image.load(os.path.join(assets_folder, 'titleScreenButtHover.png'))

def show_pause(screen):

    # Declare buttons
    button_resume = Button(632, 260, image_resume, image_resume_hovered, action=lambda: change_screen('game', screen, background_image))
    button_settings = Button(617, 420, image_settings, image_settings_hovered, action=lambda: change_screen('settings', screen, background_image))
    button_title = Button(593, 580, image_title, image_title_hovered, action=lambda: change_screen('menu', screen, background_image))

    # fill background
    screen.blit(background_image, (2, 3))

    # Load buttons onto screen
    button_resume.draw(screen)
    button_settings.draw(screen)
    button_title.draw(screen)


    if button_resume.is_clicked():
        return 'game'
    elif button_settings.is_clicked():
        return 'settings'
    elif button_title.is_clicked():
        return 'menu'

    return 'pause'


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