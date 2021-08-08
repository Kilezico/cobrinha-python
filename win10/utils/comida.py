import pygame
from .settings import *
from random import choice

class Comida():
    def __init__(self, x, y, c=RED):
        self.x = x 
        self.y = y
        self.width = PIXEL_LEN
        self.height = PIXEL_LEN
        self.color = c

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x * PIXEL_LEN, self.y * PIXEL_LEN + TOPBAR, self.width, self.height))
    
    def update(self, player):
        if self.x == player.x and self.y == player.y:
            player.len += 1
            self.change_place(player)
    
    def change_place(self, player):
        possible_places = [(i, j) for i in range(ROWS) for j in range(COLS)]
        possible_places.pop(possible_places.index((player.x, player.y)))
        for piece in player.cauda:
            possible_places.pop(possible_places.index((piece.x, piece.y)))
        if len(possible_places) > 0:
            self.x, self.y = choice(possible_places)
