import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (150, 150, 150)
YELLOW = (255, 255, 0)
PINK = (255, 0, 255)

FPS = 60

WIDTH, HEIGHT = 600, 600
ROWS = COLS = 12
PIXEL_LEN = WIDTH / ROWS
BG_COLOR = WHITE
DRAW_GRID = True
TITLE = 'Cobrinha'

Start = True
End = False

def draw_grid(win, color):
    for r in range(ROWS + 1):
        pygame.draw.line(win, color, (0, r * PIXEL_LEN), (WIDTH, r * PIXEL_LEN))
        pygame.draw.line(win, color, (0, r * PIXEL_LEN + 1), (WIDTH, r * PIXEL_LEN + 1))
        # Thick grid... Don't like using the thickness parameter
    for c in range(COLS + 1):
        pygame.draw.line(win, color, (c * PIXEL_LEN, 0), (c * PIXEL_LEN, HEIGHT))
        pygame.draw.line(win, color, (c * PIXEL_LEN - 1, 0), (c * PIXEL_LEN - 1, HEIGHT))

def get_text(font, text, color, back=None):
    txt_sfr = font.render(text, False, color, back)
    txt_rect = txt_sfr.get_rect()
    return txt_sfr, txt_rect