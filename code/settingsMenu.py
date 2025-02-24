import pygame
import sys
import os
from audioManager import AudioManager

# Initialize Pygame mixer
pygame.mixer.init()

# Establish constants
SLIDER_WIDTH, SLIDER_HEIGHT = 750, 100
HANDLE_WIDTH, HANDLE_HEIGHT = 100, 100

# load assets
assets_folder = os.path.join(os.path.dirname(__file__), '../assets/visuals/settingsMenu')
background_image = pygame.image.load(os.path.join(assets_folder, 'settingsBG.png'))
background_image = pygame.transform.scale(background_image, (1530, 860))

image_back = pygame.image.load(os.path.join(assets_folder, 'backButt.png'))
image_back_hovered = pygame.image.load(os.path.join(assets_folder, 'backButtHover.png'))
image_slider_bg = pygame.image.load(os.path.join(assets_folder, 'sliderBG.png'))
image_slider_fill = pygame.image.load(os.path.join(assets_folder, 'sliderFiller.png'))
image_handle = pygame.image.load(os.path.join(assets_folder, 'slideHandle.png'))
image_handle_hovered = pygame.image.load(os.path.join(assets_folder, 'slideHandleHover.png'))

master_dragging = False
music_dragging = False
voice_dragging = False

def change_screen(screen_name):
    return screen_name

def show_settings(screen, prev_screen, sound_manager):
    global master_dragging, music_dragging, voice_dragging

    # Create back button
    button_back = Button(25, 25, image_back, image_back_hovered, action=lambda: change_screen(prev_screen))

    # Create sliders
    slider_master = Slider(365, 265, sound_manager.get_volume("master_volume"), sound_manager, "master_volume")
    slider_music = Slider(365, 415, sound_manager.get_volume("music_volume"), sound_manager, "music_volume")
    slider_voice = Slider(365, 565, sound_manager.get_volume("voice_volume"), sound_manager, "voice_volume")


    # fill background
    screen.blit(background_image, (2, 3))

    # Draw components
    button_back.draw(screen)
    slider_master.draw(screen)
    slider_music.draw(screen)
    slider_voice.draw(screen)

    # Update slider
    mouse_pos = pygame.mouse.get_pos()
    mouse = pygame.mouse.get_pressed()

    if mouse[0]:
        if slider_master.handle_rect.collidepoint(mouse_pos) or master_dragging:
            master_dragging = True
            slider_master.move_slider()
        elif slider_music.handle_rect.collidepoint(mouse_pos) or music_dragging:
            music_dragging = True
            slider_music.move_slider()
        elif slider_voice.handle_rect.collidepoint(mouse_pos) or voice_dragging:
            voice_dragging = True
            slider_voice.move_slider()
    else:
        master_dragging = False
        music_dragging = False
        voice_dragging = False

    if button_back.is_clicked():
        return prev_screen

    return "settings"

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
    def __init__(self, x, y, initial_value, sound_manager, category):
        self.rect = pygame.Rect(x, y, SLIDER_WIDTH, SLIDER_HEIGHT)
        self.handle_rect = pygame.Rect(x + (initial_value * SLIDER_WIDTH) - (HANDLE_WIDTH / 2), y + 15, HANDLE_WIDTH, HANDLE_HEIGHT)
        self.value = initial_value
        self.sound_manager = sound_manager
        self.category = category

    def draw(self, surface):
        surface.blit(image_slider_bg, self.rect.topleft)

        fill_width = max(0, min(self.handle_rect.centerx - self.rect.left, self.rect.width))
        fill_surface = pygame.transform.scale(image_slider_fill, (fill_width, SLIDER_HEIGHT))
        surface.blit(fill_surface, self.rect.topleft)
        surface.blit(image_handle, self.handle_rect.topleft)

    def move_slider(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()

        if mouse[0]:
            self.dragging = True
            self.handle_rect.centerx = max(self.rect.left + HANDLE_WIDTH / 2, min(mouse_pos[0], self.rect.right + HANDLE_WIDTH))
            self.value = (self.handle_rect.centerx - self.rect.left) / self.rect.width
            self.sound_manager.set_volume(self.category, self.value)