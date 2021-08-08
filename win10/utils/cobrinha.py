import pygame
from .settings import *
from math import floor
from random import choice

class Cobrinha:
    def __init__(self, x, y, c1=BLACK, c2=PINK):
        self.x = x
        self.y = y
        self.width = PIXEL_LEN
        self.height = PIXEL_LEN

        self.down = False
        self.right = True
        self.left = False
        self.up = False
        self.walk_count = 0
        self.mexeu = True
        
        self.start = True
        self.end = False
        self.pause = False

        self.len = 1

        self.color1 = c1
        self.color2 = c2

        self.som_perdeu = pygame.mixer.Sound('assets/death.wav')
        self.som_perdeu.set_volume(0.3)

        self.euconut_cabeca = pygame.transform.scale(pygame.image.load('assets/icon.png'), (PIXEL_LEN, PIXEL_LEN))

        self.cauda = []

    def get_color(self):
        color = []
        if len(self.cauda) > 0:
            for i in range(3):
                color.append([])
                step = floor((self.color2[i] - self.color1[i]) / len(self.cauda))
                for j in range(len(self.cauda)):
                    to_append = self.color2[i] - j * step
                    to_append = 255 if to_append > 255 else to_append
                    to_append = 0 if to_append < 0 else to_append
                    color[i].append(to_append)

        return list(zip(*color))

    def draw(self, win):
        colors = self.get_color()
        if self.color1 != WHITE:
            pygame.draw.rect(win, self.color1, (self.x * PIXEL_LEN, self.y * PIXEL_LEN + TOPBAR, PIXEL_LEN, PIXEL_LEN))
        else:
            if self.left:
                img = pygame.transform.rotate(self.euconut_cabeca, 90)
            elif self.right:
                img = pygame.transform.rotate(self.euconut_cabeca, -90)
            elif self.down:
                img = pygame.transform.rotate(self.euconut_cabeca, 180)
            else:
                img = self.euconut_cabeca
            win.blit(img, (self.x * PIXEL_LEN, self.y * PIXEL_LEN + TOPBAR))
        
        for i in range(len(self.cauda)):
            piece = self.cauda[i]
            pygame.draw.rect(win, colors[i], (piece.x * PIXEL_LEN, piece.y * PIXEL_LEN + TOPBAR, PIXEL_LEN, PIXEL_LEN))


    def update(self):
        if self.len > len(self.cauda):
            self.cauda.append(pygame.Rect((self.x, self.y, PIXEL_LEN, PIXEL_LEN)))
        else:
            for i in range(len(self.cauda) - 1):
                self.cauda[i] = self.cauda[i+1]
            self.cauda[-1] = (pygame.Rect((self.x, self.y, PIXEL_LEN, PIXEL_LEN)))

        if self.right:
            self.x += 1
        elif self.left:
            self.x -= 1
        elif self.up:
            self.y -= 1
        elif self.down:
            self.y += 1

        self.mexeu = False

        if self.x < 0 or self.x >= COLS or self.y < 0 or self.y >= ROWS:
            self.morre()
        for piece in self.cauda:
            if self.x == piece.x and self.y == piece.y:
                self.morre()

    def restart(self):
        self.x = 1
        self.y = 1
        self.cauda.clear()
        self.go_right()

    def morre(self):
        self.som_perdeu.play()
        self.end = True
        pygame.mixer.music.stop()
        self.restart()

        self.color1, self.color2 = choice([
            (BLUE, GREEN),
            (WHITE, BLUE),
            (BLACK, PINK),
            (BLUE, PINK),
            (BLACK, CYAN),
            (WHITE, PINK),
            (WHITE, CYAN)
        ])

        

    def go_left(self):
        self.down = False
        self.right = False
        self.left = True
        self.up = False
        self.mexeu = True

    def go_right(self):
        self.down = False
        self.right = True
        self.left = False
        self.up = False
        self.mexeu = True

    def go_up(self):
        self.down = False
        self.right = False
        self.left = False
        self.up = True
        self.mexeu = True
    
    def go_down(self):
        self.down = True
        self.right = False
        self.left = False
        self.up = False
        self.mexeu = True

