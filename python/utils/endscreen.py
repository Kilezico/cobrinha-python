from .settings import *
import pygame
from .button import *

menu = Button(160, 480, 240, 100, 'Menu', YELLOW, 20)
retry = Button(440, 480, 240, 100, 'Tentar de novo', GREEN, 20)
quit = Button(WIDTH/2, HEIGHT - 40, 100, 40, 'Sair', RED, 5)

def draw(win, len):
    if len >= ROWS * COLS:
        txt, rect = get_text(pygame.font.SysFont('freemono', 60), 'Parabéns!', BLACK)
        rect.center = WIDTH/2, 100
        win.blit(txt, rect)

        txt, rect = get_text(pygame.font.SysFont('freemono', 60), 'Você ganhou!', BLACK)
        rect.center = WIDTH/2, 170
        win.blit(txt, rect)
    else:
        txt, rect = get_text(pygame.font.SysFont('freemono', 60), 'Que Pena!', BLACK)
        rect.center = WIDTH/2, 100
        win.blit(txt, rect)

        txt, rect = get_text(pygame.font.SysFont('freemono', 60), 'Você perdeu!', BLACK)
        rect.center = WIDTH/2, 170
        win.blit(txt, rect)
        
    txt, rect = get_text(pygame.font.SysFont('freemono', 30), f'Pontuação: {len - 1}', BLACK)
    rect.center = WIDTH/2, 250
    win.blit(txt, rect)


    menu.draw(win)
    retry.draw(win)
    quit.draw(win)

def events(event, cobra):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == pygame.BUTTON_LEFT:
            pos = pygame.mouse.get_pos()
            cobra.len = 1
            if menu.is_inside(pos):
                cobra.start = True
                cobra.end = False
            if retry.is_inside(pos):
                cobra.end = False
            if quit.is_inside(pos):
                pygame.quit()
                exit()
def update():
    pass
