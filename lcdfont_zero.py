# handmade LCD font for pygame
# 5x7ドットマトリクス   制作用。 0, 1, 2のみ作ってあります。

import pygame
from pygame.locals import Rect

# 0 code=0
LCD_0 = (0, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         1, 0, 0, 1, 1,
         1, 0, 1, 0, 1,
         1, 1, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 1, 1, 1, 0)
# 1 code=1
LCD_1 = (0, 0, 1, 0, 0,
         0, 1, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 1, 1, 1, 0)
# 2 code=2
LCD_2 = (0, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         0, 0, 0, 0, 1,
         0, 0, 0, 1, 0,
         0, 0, 1, 0, 0,
         0, 1, 0, 0, 0,
         1, 1, 1, 1, 1)

# [ ] 0x7f  DELETE
LCD_NONE = (1, 1, 1, 1, 1,
            1, 0, 0, 0, 1,
            1, 0, 0, 0, 1,
            1, 0, 0, 0, 1,
            1, 0, 0, 0, 1,
            1, 0, 0, 0, 1,
            1, 1, 1, 1, 1)


# LCD_FONT_STYLES = (LCD_0, LCD_1, LCD_2)

LCD_FONT_STYLES_ASCII = {
    0x30: LCD_0, 0x31: LCD_1, 0x32: LCD_2,
    0x7f: LCD_NONE
}

GRAY = (80, 80, 80)
GREEN = (10, 250, 10)
WHITE = (250, 250, 250)


class LcdFont():
    """[LCDフォントで文字列を描くディスプレイラインのクラス]
    """
    def __init__(self, screen):
        self.screen = screen
        self.set_col()
        self.set_row()

    def set_col(self, block_size=4, block_intv=4, color_on=WHITE, color_off=GRAY):
        """ Setting the character of collumn in dislapy line

        表示行の一文字について設定

        Args:
            block_size (int, optional): Defaults to 3.
                Size of each block in pixels.
                ブロックサイズをピクセル数で指定。
            block_intv (int, optional): Defaults to 4.
                Interval of each block in pixels.
                ブロック同士の配置間隔をピクセル数で指定。
            color_on ([type], optional): Defaults to WHITE.
                color of block with lights on
                点灯中ブロックの色。
            color_off ([type], optional):Defaults to GRAY.
                color of block with lights off
                消灯中ブロックの色。
        """
        self.BLOCK_SIZE = block_size
        self.BLOCK_INTV = block_intv
        self.COLOR_ON = color_on
        self.COLOR_OFF = color_off

    def set_row(self, x_org=2, y_org=8, col_intv=6):
        """ Setting display row line

        表示行の設定

        Args:
            x_org (int): Defaults to 2.
                原点（最上位桁の左下）のx座標をブロック数で指定。
            y_org (int): Defaults to 8.
                原点（最上位桁の左下）のy座標をブロック数で指定。
            col_intv (int): Defaults to 6.
                桁の間隔をブロック数で指定。
        """
        # BLOCK_INTVは、
        # 原点（最上位桁の左下）の座標
        self.X_ORG = x_org * self.BLOCK_INTV
        self.Y_ORG = y_org * self.BLOCK_INTV
        # 桁同士の間隔、ピクセル指定
        self.COL_INTV = col_intv * self.BLOCK_INTV

    def update_col(self, col=0, character="2"):
        """ Display one character at the column
        指定桁に、指定文字を表示する関数

        Args（引数）:
            col (int): Defaults to 0.
                the column to display
                表示する桁
            chr (str): Defaults to "2".
                the character to display
                表示する文字

        """
        # codeの文字をcol桁目に表示、桁は最上位桁の左から右へ進む。
        # そのコードのフォントデザインがなければコード0x7fにすり替える。
        if ord(character) in LCD_FONT_STYLES_ASCII.keys():
            chr_code = ord(character)
        else:
            chr_code = 0x7f
        i = 0
        for i in range(35):
            x = i % 5
            y = i // 5
            if LCD_FONT_STYLES_ASCII[chr_code][i] == 1:
                color = self.COLOR_ON
            else:
                color = self.COLOR_OFF
            # 桁の原点
            x0 = self.X_ORG + self.COL_INTV * col
            y0 = self.Y_ORG
            # ドットの原点座標
            org1 = (x0 + x * self.BLOCK_INTV, y0 + y * self.BLOCK_INTV)
            # ドットを描く
            pygame.draw.rect(self.screen, color,
                             Rect(org1[0], org1[1], self.BLOCK_SIZE, self.BLOCK_SIZE))

    def update_message(self, message="012"):
        """ display the message line

        文字列を表示
        """
        i = 0
        for c in message:
            self.update_col(col=i, character=c)
            i += 1


class LcdFontPG(LcdFont):
    """  """
    pass


class LcdFontMC(LcdFont):
    """  """
    pass
