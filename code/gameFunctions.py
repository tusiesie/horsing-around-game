import os
import pygame
import pygame.freetype
# from os import WSTOPSIG

from sceneManager import Background
from context import Arcs,Context 

class Transitions:
    def __init__(self):
        self.alpha = 0

    def draw(self, screen, bg):
        screen.blit(bg, (2,3))

        overlay = pygame.Surface(screen.get_size())
        overlay.fill( (0,0,0) )
        overlay.set_alpha(self.alpha)
        screen.blit(overlay, (0,0) ) #apply overlay to screen
        pygame.display.flip() #update screen

    def fade_in(self, screen, bg):
        alpha = 255
        for _ in range(0, 256):
            #time.sleep(0.0005)
            alpha -= 12
            self.alpha = alpha
            self.draw(screen, bg)
            if alpha < 0:
                return
            #self.update(new_bg, screen)
    def fade_out(self, screen, bg):

        alpha = 0
        for _ in range(0, 256): 
            
            #time.sleep(.0005) # 0.5s (duration) / 255 = 0.002
            alpha += 12
            self.alpha = alpha
            self.draw(screen, bg)
            if alpha > 255:
                return
    def typewriter(self, text):
        pass

class DialogueBox:
    def set_dialogue_text_box(self, dialogue_type, character):
        text_boxes = os.path.join(os.path.dirname(__file__), '../assets/visuals/textBoxes/')
        path = ''
        if dialogue_type == 'default':
            if character == 'MC':
                path = text_boxes + 'textBoxLeftStars.png'
            else: path = text_boxes + 'textBoxRightStars.png'

        elif dialogue_type == 'hearts':
            if character == 'MC':
                path = text_boxes + 'textBoxLeftHearts.png'
            else: path = text_boxes + 'textBoxRightHearts.png'

        else: raise Exception('Unknown type for TextBox')
        self.dialogue_box = pygame.image.load(path)

    def __init__(self, dialogue_box_type = 'default', character = 'MC', action=None):

        self.dialogue_box = None
        self.set_dialogue_text_box(dialogue_box_type, character) # initialize dialogue box

        self.screen_size = pygame.display.set_mode().get_size()
        self.action = action


    def draw(self, surface):
        #if self.rect.collidepoint(pygame.mouse.get_pos()):
        #    surface.blit(self.image_hovered, self.rect.topleft)
        #else:
        #    surface.blit(self.image_normal, self.rect.topleft)

        size = pygame.transform.scale(self.dialogue_box, (900, 500))
        rect = size.get_rect(topleft=(500, 500)) 
        #self.rect = self.dialogue_box.get_rect(center=(x//2, y - 100))

        surface.blit(size, (500, 600))
    def is_clicked(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            if self.action:
                self.action()
            return True
        return False
T = Transitions()
D = DialogueBox()
ctx = Context()

def show_dialogue_box():
    pass

# starts a new game
def show_game(screen, stats):

    ctx.load_arc(Arcs.BEGINNING)

    character, line = next(ctx.get_dialogue())

    
    D.draw(screen) # draw dialogue box
    text_surface, rect = ctx.font.render( f'{character}: {line}', (0,0,0) )
    screen.blit(text_surface, (40, 250))

    return "game"

def show_saved(screen, stats):
    return "saved_game"

def show_credits(screen):
    return "credits"
def change_screen(name, screen, prev_bg):
    if name == "game":
        bg = pygame.image.load(Background.HIGHSCHOOL_STAIRS.value)
        T.fade_out(screen, prev_bg)
        screen.blit(bg, (2,3))
        T.fade_in(screen, bg)
    return screen

