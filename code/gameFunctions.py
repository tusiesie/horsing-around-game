import pygame
import time

from sceneManager import Background
# starts a new game
def show_game(screen):
    return "game"

'''
class Fader:

    def __init__(self, scenes):
        self.scenes = cycle(scenes)
        self.scene = next(self.scenes)
        self.fading = None
        self.alpha = 0
        sr = pygame.display.get_surface().get_rect()
        self.veil = pygame.Surface(sr.size)
        self.veil.fill((0, 0, 0))

    def next(self):
        if not self.fading:
            self.fading = 'OUT'
            self.alpha = 0

    def draw(self, screen):
        self.scene.draw(screen)
        if self.fading:
            self.veil.set_alpha(self.alpha)
            screen.blit(self.veil, (0, 0))

    def update(self, dt, events):
        self.scene.update(dt, events)

        if self.fading == 'OUT':
            self.alpha += 8
            if self.alpha >= 255:
                self.fading = 'IN'
                self.scene = next(self.scenes)
        else:
            self.alpha -= 8
            if self.alpha <= 0:
                self.fading = None
'''
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


T = Transitions()
def change_screen(name, screen, prev_bg):
    if name == "game":
        bg = pygame.image.load(Background.HIGHSCHOOL_STAIRS.value)
        T.fade_out(screen, prev_bg)
        screen.blit(bg, (2,3))
        T.fade_in(screen, bg)
    return screen

