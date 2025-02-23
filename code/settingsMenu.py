import pygame
import sys
import os

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
image_silderbg_master = pygame.image.load(os.path.join(assets_folder, 'sliderBG.png'))
image_sliderbg_music = pygame.image.load(os.path.join(assets_folder, 'sliderBG.png'))
image_silderbg_voice = pygame.image.load(os.path.join(assets_folder, 'sliderBG.png'))
image_silderfill_master = pygame.image.load(os.path.join(assets_folder, 'sliderFiller.png'))
image_sliderfill_music = pygame.image.load(os.path.join(assets_folder, 'sliderFiller.png'))
image_silderfill_voice = pygame.image.load(os.path.join(assets_folder, 'sliderFiller.png'))
image_handle_master = pygame.image.load(os.path.join(assets_folder, 'slideHandle.png'))
image_handle_music = pygame.image.load(os.path.join(assets_folder, 'slideHandle.png'))
image_handle_voice = pygame.image.load(os.path.join(assets_folder, 'slideHandle.png'))
image_handle_master_hovered = pygame.image.load(os.path.join(assets_folder, 'slideHandleHover.png'))
image_handle_music_hovered = pygame.image.load(os.path.join(assets_folder, 'slideHandleHover.png'))
image_handle_voice_hovered = pygame.image.load(os.path.join(assets_folder, 'slideHandleHover.png'))


def show_settings(screen, prev_screen):
    button_back = Button(100, 400, image_back, image_back_hovered, action=lambda: change_screen(prev_screen))


    # fill background
    screen.blit(background_image, (2, 3))

    button_back.draw(screen)


    if button_back.is_clicked():
        return "saved_game"

    

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