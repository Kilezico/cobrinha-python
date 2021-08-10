from .settings import *
from .button import *
import pygame

resume = Button(WIDTH/2, HEIGHT/ 2, 300, 100, 'Continuar', YELLOW, 20)
menu = Button(WIDTH/2, HEIGHT/ 2 + 120, 300, 100, 'Menu', RED, 20)

resuming = False
resume_count = 0
countdown = 0

def draw(win):
    # Cobertura esbranquiçada
    surf = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    surf.fill((255, 255, 255, 150))
    win.blit(surf, (0, 0))
    
    if not resuming:
        # Texto "Pausado"
        surf, rect = get_text(pygame.font.SysFont('freemono', 60), 'Jogo Pausado', BLACK)
        rect.center = WIDTH/2, HEIGHT/2 - 200
        win.blit(surf, rect)

        resume.draw(win)
        menu.draw(win)
    else:
        surf, rect = get_text(pygame.font.SysFont('freemono', 100), countdown, PINK)
        rect.center = WIDTH/2, HEIGHT/2
        win.blit(surf, rect)

def event(event, cobra):
    global resuming
    if not resuming:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                pos = pygame.mouse.get_pos()
                if menu.is_inside(pos):
                    cobra.pause = False
                    cobra.start = True
                    cobra.restart()
                    pygame.mixer.music.stop()
                if resume.is_inside(pos):
                    resuming = True  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                resuming = True

def update():
    global resuming, resume_count, countdown
    if resuming:
        if resume_count < FPS:
            countdown = '3'
        elif resume_count < FPS * 2:
            countdown = '2'
        elif resume_count < FPS * 3:
            countdown = '1'
        else:
            pygame.mixer.music.unpause()
            resuming = False
            resume_count = 0
            return False
        resume_count += 1
    return True
