import pygame
import sys
import os
from audioManager import AudioManager

# Initialize Pygame mixer
pygame.mixer.init()

# Establish constants
SLIDER_WIDTH, SLIDER_HEIGHT = 300, 10
HANDLE_WIDTH, HANDLE_HEIGHT = 20, 20

# load assets
assets_folder = os.path.join(os.path.dirname(__file__), '../assets/visuals/settingsMenu')
background_image = pygame.image.load(os.path.join(assets_folder, 'settingsBG.png'))
background_image = pygame.transform.scale(background_image, (1530, 860))

image_back = pygame.image.load(os.path.join(assets_folder, 'backButt.png'))
image_back_hovered = pygame.image.load(os.path.join(assets_folder, 'backButtHover.png'))
image_silder_bg = pygame.image.load(os.path.join(assets_folder, 'sliderBG.png'))
image_silder_fill = pygame.image.load(os.path.join(assets_folder, 'sliderFiller.png'))
image_handle = pygame.image.load(os.path.join(assets_folder, 'slideHandle.png'))
image_handle_hovered = pygame.image.load(os.path.join(assets_folder, 'slideHandleHover.png'))


def show_settings(screen, prev_screen, sound_manager):

    # Create back button
    button_back = Button(100, 400, image_back, image_back_hovered, action=lambda: change_screen(prev_screen))

    # Create sliders
    slider_master = Slider(100, 100, sound_manager.get_volume("master_volume"), sound_manager)
    slider_music = Slider(100, 150, sound_manager.get_volume("music_volume"), sound_manager)
    slider_voice = Slider(100, 200, sound_manager.get_volume("voice_volume"), sound_manager)


    # fill background
    screen.blit(background_image, (2, 3))

    # Draw components
    button_back.draw(screen)
    slider_master.draw(screen)
    slider_music.draw(screen)
    slider_voice.draw(screen)

    # Update all sliders
    slider_master.update()
    slider_music.update()
    slider_voice.update()

    if button_back.is_clicked():
        return prev_screen


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
    


class Slider:
    def __init__(self, x, y, initial_value, sound_manager):
        self.rect = pygame.Rect(x, y, SLIDER_WIDTH, SLIDER_HEIGHT)
        self.handle_rect = pygame.Rect(x + (initial_value * SLIDER_WIDTH) - (HANDLE_WIDTH / 2), y - (HANDLE_HEIGHT / 2), HANDLE_WIDTH, HANDLE_HEIGHT)
        self.value = initial_value
        self.sound_manager = sound_manager

    def draw(self):
        surface.blit(image_silder_bg)