# demo for handmade LCD font for Pygame
# 手作りLCDフォントのデモ Pygame用

# Using HSV model instead of RGB for 'stylish' coloring.
# Refer to demo_RGB_HSV.py for the details.
# 「おしゃれな」色使いのために RGBの代わりにHSVモデルを使用した。
# 詳細はdemo_RGB_HSV.pyを参照のこと。

# pygameでは、実行時のファイル階層（ワーキングディレクトリー）が、
# 実行ファイル自体が存在する階層（アプリディレクトリー）と一致しない場合、
# フォントや画像など、他のファイルを相対pathで参照することはできない。
#
# ワーキングディレクトリーからの相対pathになってしまい、not foundエラーとなる。
# 実行時にアプリフォルダの絶対pathを取得し、目的ファイルを絶対pathで参照すべし。


import colorsys  # colorsys.hsv_to_rgb()
import os        # os.path.dirname(), os.path.join()
from datetime import datetime

import pygame
import pygame.freetype
from pygame.locals import Rect

from lcdfontdisp import LcdFontDisplay

# ルートからアプリのディレクトリ（このファイル自身が居る）までのpathを取得
APP_DIR = os.path.dirname(__file__)
# pathの区切り文字が'/'でないOSを想定して文字列連結
FONTS_DIR = os.path.join(APP_DIR, "fonts")
# IMAGES_DIR = os.path.join(APP_DIR, "images")
# print(APP_DIR, IMAGES_DIR, FONTS_DIR, sep="\n")  # テスト用


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
COLOR_04 = hsv_to_rgb_255(0.9, 0.5, 1.0)
COLOR_05 = hsv_to_rgb_255(0.19, 0.5, 1.0)  #

COLOR_BG = (50, 50, 50)  # Background color, RGBでgray
COLOR_BG2 = (90, 90, 90)  # Background color, RGBでlight gray

DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
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


class LcdFontDisplayPG(LcdFontDisplay):
    """ draw a dot on the Pygame screen """
    def draw_dot(self, org1, color):
        """ overide the method of LcdFontDisplay for Pygame

        LcdFOntDisplayのメソッドをPygame用にオーバーライド
        """
        pygame.draw.rect(self.screen, color,
                         Rect(org1[0], org1[1], self.BLOCK_SIZE, self.BLOCK_SIZE))


# big display
lcd1 = LcdFontDisplayPG(screen)
lcd1.set_col(block_size=7, block_intv=8, color_on=COLOR_01, color_off=COLOR_BG2)
lcd1.set_row(x_org=8, y_org=8, col_intv=6)
# sample display
lcd2 = LcdFontDisplayPG(screen)
lcd2.set_col(block_size=2, block_intv=3, color_on=COLOR_05, color_off=COLOR_BG)
lcd2.set_row(x_org=4, y_org=70, col_intv=6)
# letter pressed
lcd3 = LcdFontDisplayPG(screen)
lcd3.set_col(block_size=11, block_intv=12, color_on=LCD_BLUE, color_off=COLOR_BG2)
lcd3.set_row(x_org=21, y_org=1, col_intv=6)
# ASCII
lcd4 = LcdFontDisplayPG(screen)
lcd4.set_col(block_size=3, block_intv=4, color_on=COLOR_04, color_off=COLOR_BG)
lcd4.set_row(x_org=3, y_org=44, col_intv=6)
# clock
lcd_time = LcdFontDisplayPG(screen)
lcd_time.set_col(block_size=4, block_intv=5, color_on=COLOR_02, color_off=COLOR_BG)
lcd_time.set_row(x_org=2, y_org=2, col_intv=6)

font1 = pygame.freetype.Font(os.path.join(FONTS_DIR, 'natumemozi.ttf'), 48)


def disp_one_character(pos_x, pos_y):
    """ display one character of LCD font

    1文字のLCDフォント表示

    Args:
        pos_x (int): horizaontal position, 水平位置
        pos_y (int): virtical position, 垂直位置
    """

    chr_code = int(pos_x / 8) % 16
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

    pos_x = WINDOW_WIDTH * 0.5
    pos_y = WINDOW_HEIGHT * 0.6

    x_change = 0
    y_change = 0

    key_code = pygame.K_SPACE  # 0x20
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

        dt_now = datetime.now()

        disp_one_character(pos_x, pos_y)
        # sample display
        lcd2.update_message("0123456789abcdef 12:34")
        # show the key pressed
        lcd3.update_col(character=chr(key_code if key_code < 0x7f else 0x7f))
        # show ASCII code of the key pressed
        lcd4.update_message(hex(key_code))
        # clock style display
        lcd_time.update_message(
            str(dt_now.hour)
            + ':' + str(dt_now.minute)
            + ':' + str(dt_now.second)
            )

        pygame.display.update()
        clock.tick(60)


infinite_loop()
pygame.quit()
