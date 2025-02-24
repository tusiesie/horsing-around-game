import pygame
import pygame.freetype
from os import WSTOPSIG

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


T = Transitions()
ctx = Context()

# starts a new game
def show_game(screen):
    ctx.load_arc(Arcs.BEGINNING)
    character, line = next(ctx.get_dialogue())
    text_surface, rect = ctx.font.render( f'{character}: {line}', (0,0,0) )
    screen.blit(text_surface, (40, 250))
    return "game"

def show_saved(screen):
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

