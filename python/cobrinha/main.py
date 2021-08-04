from utils import *

DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
pygame.display.set_icon(pygame.image.load('assets/icon.png'))

clock = pygame.time.Clock()

cobra = Cobrinha(0, 0)

def draw():
    DISPLAY.fill(BG_COLOR)
    if DRAW_GRID:
        draw_grid(DISPLAY, BLACK)

    cobra.draw(DISPLAY)

    pygame.display.update()

def main():
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
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
                if event.key == pygame.K_g:
                    cobra.len += 1
        if cobra.walk_count >= 10:
            cobra.update()
            cobra.walk_count = 0
        else:
            cobra.walk_count += 1

        draw()

main()
pygame.quit()
