from .button import *
import pygame

button = Button(WIDTH/2, HEIGHT/2 + 100, 300, 100, 'JOGAR', RED, 20)

def draw(win):
    surf, rect = get_text(pygame.font.SysFont('freemono', 60), 'Jogo da Cobrinha', BLACK)
    rect.center = WIDTH/2, 100
    win.blit(surf, rect)

    surf, rect = get_text(pygame.font.SysFont('freemono', 30), 'É bem legal!', BLACK)
    rect.center = WIDTH/2, 160
    win.blit(surf, rect)

    button.draw(win)



def event(event, cobra):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == pygame.BUTTON_LEFT:
            if button.is_inside(pygame.mouse.get_pos()):
                cobra.start = False
                pygame.mixer.music.play(-1)


def update():
    pass
