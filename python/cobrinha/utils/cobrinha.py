import pygame
from .settings import *

class Cobrinha:
    def __init__(self, x, y, c1=RED, c2=RED):
        self.x = x
        self.y = y
        self.width = PIXEL_LEN
        self.height = PIXEL_LEN

        self.down = False
        self.right = True
        self.left = False
        self.up = False
        self.walk_count = 0
        self.mexeu = False

        self.len = 1
        self.color1 = c1
        self.color2 = c2

        self.cauda = []

    def get_color(self):
        color = [
            [self.color1[0]],
            [self.color1[1]],
            [self.color1[2]]
        ]
        for i in range(3):
            delta = self.color1[i] - self.color2[i]
            step = delta // self.len
            for i in range(self.len):
                color[i].append(self.color1[i] + step)

        return list(zip(*color))

    def draw(self, win):
        colors = self.get_color()
        pygame.draw.rect(win, colors[0], (self.x * PIXEL_LEN, self.y * PIXEL_LEN, PIXEL_LEN, PIXEL_LEN))

        for i in range(len(self.cauda)):
            piece = self.cauda[i]
            j = len(colors) - i
            pygame.draw.rect(win, colors[j], (piece.x * PIXEL_LEN, piece.y * PIXEL_LEN, PIXEL_LEN, PIXEL_LEN))
        
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

