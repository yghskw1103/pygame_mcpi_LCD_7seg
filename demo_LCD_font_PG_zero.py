# practise file for handmade LCD font
# 手作りLCDフォントの制作演習用
# There are only 0, 1, 2 for font design, create from 3 to 9 by yourself.
# 0, 1, 2しかフォントデザインが無いので、3から9を制作してください。


import colorsys  # colorsys.hsv_to_rgb()を使用
import os  # os.path.dirname(), os.path.join()を使用

import pygame
import pygame.freetype

from lcdfont_zero import LcdFontPG


APP_DIR = os.path.dirname(__file__)
FONTS_DIR = os.path.join(APP_DIR, 'fonts')


def hsv_to_rgb_255(h, s, v):
    """convert the color from HSV(0.0-1.0) to a tuple of R, G, and B(0-255)

    HSV(0.0-1.0)の色をR, G, B(0-255)のタプルに変換する

    Args:
        h (float): hue (0.0-1.0)
        s (float): saturation (0.0-1.0)
        v (float): value (0.0-1.0)

    Returns:
         (tuple, int): RGB values(0-255)
    """
    return tuple(round(rgb_val * 255) for rgb_val in (colorsys.hsv_to_rgb(h, s, v)))


# 0.0から1.0、H：Hue 色相（R-->G-->B）、 S：Saturation 彩度（白-->色）、V：Value 明度（黒-->色）
COLOR_01 = hsv_to_rgb_255(0.0, 0.5, 1.0)  # PINK
COLOR_02 = hsv_to_rgb_255(0.33, 0.5, 1.0)  # PALE_GREEN
COLOR_03 = hsv_to_rgb_255(0.66, 0.5, 1.0)  # PALE_BLUE


DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
CYAN = (120, 120, 250)

YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)
LCD_BLUE = (149, 227, 203)

WINDOW_WIDTH = 320
WINDOW_HEIGHT = 240

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('LCD font')

clock = pygame.time.Clock()

font1 = pygame.freetype.Font(os.path.join(FONTS_DIR, 'natumemozi.ttf'), 48)

lcd1 = LcdFontPG(screen)
lcd1.set_col(block_size=7, block_intv=8, color_on=COLOR_01, color_off=GRAY)
lcd1.set_row(x_org=5, y_org=5, col_intv=6)

lcd2 = LcdFontPG(screen)
lcd2.set_col(block_size=4, block_intv=5, color_on=COLOR_02, color_off=GRAY)
lcd2.set_row(x_org=3, y_org=39, col_intv=6)


def disp_one_character(pos_x, pos_y):
    """ display one character of LCD font

    1文字のLCDフォント表示

    Args:
        pos_x (int): horizaontal position, 水平位置
        pos_y (int): virtical position, 垂直位置
    """

    chr_code = int(pos_x / 8) % 3
    if chr_code < 10:
        chr_code += ord("0")
    else:
        chr_code += ord("a") - 10
    text1, rect1 = font1.render(chr(chr_code), WHITE)
    rect1.center = (pos_x, pos_y)
    screen.blit(text1, rect1)
    lcd1.update_col(col=0, character=chr(chr_code))


def infinite_loop():
    """ infinite loop to render/update the Pygame window """

    pos_x = (WINDOW_WIDTH * 0.5)
    pos_y = (WINDOW_HEIGHT * 0.5)

    x_change = 0
    y_change = 0

    key_code = 0x20
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                key_code = event.key
                if pygame.key.get_mods() and pygame.KMOD_SHIFT:
                    if key_code >= pygame.K_a and key_code <= pygame.K_z:
                        key_code += ord("A") - ord("a")
                if event.key == pygame.K_LEFT:
                    x_change = -1
                if event.key == pygame.K_RIGHT:
                    x_change = 1
                if event.key == pygame.K_UP:
                    y_change = -1
                if event.key == pygame.K_DOWN:
                    y_change = 1
                if event.key == pygame.K_q:
                    running = False

            if event.type == pygame.KEYUP:
                key_code = pygame.K_SPACE  # space
                if (
                        event.key == pygame.K_LEFT
                        or event.key == pygame.K_RIGHT
                        or event.key == pygame.K_UP
                        or event.key == pygame.K_DOWN):
                    x_change = 0
                    y_change = 0

        pos_x += x_change
        pos_y += y_change

        if pos_x > WINDOW_WIDTH:
            pos_x = WINDOW_WIDTH
        if pos_y > WINDOW_HEIGHT:
            pos_y = WINDOW_HEIGHT
        if pos_x < 0:
            pos_x = 0
        if pos_y < 0:
            pos_y = 0

        screen.fill(GRAY)

        disp_one_character(pos_x, pos_y)
        lcd2.update_message("0123456789")

        pygame.display.update()
        clock.tick(60)


infinite_loop()
pygame.quit()
