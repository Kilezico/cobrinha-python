from utils import *

DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
pygame.display.set_icon(pygame.image.load('assets/icon.png'))
pygame.mixer.music.load('assets/music.wav')
pygame.mixer.music.set_volume(0.2)

euconut = pygame.transform.scale(pygame.image.load('assets/icon.png'), (WIDTH, HEIGHT))

size = 10

clock = pygame.time.Clock()

cobra = Cobrinha(1, 1)

pause_button = Button(TOPBAR/2, TOPBAR/2, 40, 40, '', GRAY, 10)

comida = Comida(0, 0)
comida.change_place(cobra)

def draw():
    DISPLAY.fill(BG_COLOR)
    DISPLAY.blit(euconut, (0, 0))
    conut = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    conut.fill((*BG_COLOR, 150))
    DISPLAY.blit(conut, (0, 0))

    if cobra.start:
        start.draw(DISPLAY)
    elif not cobra.end:
        if DRAW_GRID:
            draw_grid(DISPLAY, GRAY)
        cobra.draw(DISPLAY)
        comida.draw(DISPLAY)

        # Botão de pausa :)  ||   
        pause_button.draw(DISPLAY)
        pause_button_thingy = pygame.Rect(pause_button.x + pause_button.width/5, 0, pause_button.width/5, pause_button.height-10)
        pause_button_thingy.center = pause_button_thingy.center[0], TOPBAR/2
        pygame.draw.rect(DISPLAY, BLACK, pause_button_thingy)
        pause_button_thingy = pygame.Rect(pause_button.x + pause_button.width/5*3, 0, pause_button.width/5, pause_button.height-10)
        pause_button_thingy.center = pause_button_thingy.center[0], TOPBAR/2
        pygame.draw.rect(DISPLAY, BLACK, pause_button_thingy)
        

        txt, rect = get_text(pygame.font.SysFont('freemono', 30), f'Pontuação: {cobra.len - 1}', BLACK)
        rect.x = 70
        rect.center = rect.center[0] , TOPBAR/2
        DISPLAY.blit(txt, rect)

        if cobra.pause:
            pause.draw(DISPLAY)

    else:
        endscreen.draw(DISPLAY, cobra.len)

    pygame.display.update()

def main():
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if cobra.start:
                start.event(event, cobra)
            elif cobra.pause:
                pause.event(event, cobra)
            elif not cobra.end:
                if event.type == pygame.KEYDOWN:
                    if not cobra.mexeu:
                        if event.key == pygame.K_a and not cobra.right:
                            cobra.go_left()
                        if event.key == pygame.K_w and not cobra.down:
                            cobra.go_up()
                        if event.key == pygame.K_s and not cobra.up:
                            cobra.go_down()
                        if event.key == pygame.K_d and not cobra.left:
                            cobra.go_right()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        if pause_button.is_inside(pygame.mouse.get_pos()):
                            cobra.pause = True
                            pygame.mixer.music.pause()
            else:
                endscreen.events(event, cobra)



        if cobra.start:
            start.update()
        elif cobra.pause:
            cobra.pause = pause.update()
        elif not cobra.end:
            if cobra.walk_count >= FPS//6:
                cobra.update()
                cobra.walk_count = 0
            else:
                cobra.walk_count += 1
            comida.update(cobra)
        else:
            endscreen.update()

        draw()

main()
pygame.quit()
