from .settings import *
import pygame

class Button(pygame.Rect):
    def __init__(self, x, y, w, h, txt, c, r):
        self.width = w
        self.height = h
        self.center = x, y
        self.color = c
        self.r = r
        self.txt = txt
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, self, 0, self.r)
        surf = pygame.font.SysFont('comicsans', 45).render(self.txt, False, BLACK)
        rect = surf.get_rect()
        rect.center = self.center
        win.blit(surf, rect)

    def is_inside(self, pos):
        return pos[0] < self.x + self.width and pos[0] > self.x and pos[1] > self.y and pos[1] < self.y + self.height

