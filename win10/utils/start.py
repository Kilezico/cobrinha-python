from .button import *
import pygame

button = Button(WIDTH/2, HEIGHT/2 + 100, 300, 100, 'JOGAR', GREEN, 20)
quit = Button(WIDTH/2, HEIGHT - 80, 100, 40, 'Sair', RED, 5)

def draw(win):
    surf, rect = get_text(pygame.font.SysFont('freemono', 60), 'Jogo da Cobrinha', BLACK)
    rect.center = WIDTH/2, 100
    win.blit(surf, rect)

    surf, rect = get_text(pygame.font.SysFont('freemono', 30), 'É bem legal!', BLACK)
    rect.center = WIDTH/2, 160
    win.blit(surf, rect)

    button.draw(win)
    quit.draw(win)



def event(event, cobra):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == pygame.BUTTON_LEFT:
            pos = pygame.mouse.get_pos()
            if button.is_inside(pos):
                cobra.start = False
                pygame.mixer.music.play(-1)
            if quit.is_inside(pos):
                pygame.quit()
                exit()


def update():
    pass
