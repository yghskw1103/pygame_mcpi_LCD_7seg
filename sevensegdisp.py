# 7-seg display simulator for pygame
# 各セグメントをブロック２個で構成。
# 4x7ドットマトリクスになっている。

from math import log

from sevensegfont import SEGMENTS


# 色の準備。R, G, Bを0から255で指定。
DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)


class SevenSegDisplay():
    """
    7-segment LED simulation, with two square blocks in each segment

    7セグLEDのシミュレーション、各セグメントを2つの正方形ブロックで
    """
    def __init__(self, screen):
        self.screen = screen

    def init_col(self, block_size=3, block_intv=4, color_on=WHITE, color_off=GRAY):
        """ Initialize the character of collumn in dislapy line

        表示行の一文字について初期設定

        Args:
            block_size (int, optional): Defaults to 3.
                Size of each block in pixels.
                ブロックサイズをピクセル数で指定。
            block_intv (int, optional): Defaults to 4.
                Interval between each block in pixels.
                ブロック同士の間隔をピクセル数で指定。
            color_on ([type], optional): Defaults to WHITE.
                color of block with lights on
                点灯中ブロックの色。
            color_off ([type], optional):Defaults to GRAY.
                color of block with lights off
                消灯中ブロックの色。
        """
        # ひと桁、コラムの設定
        # 7セグをセグメントあたり2個のブロックで構成
        # ブロックのサイズと配置間隔をピクセル指定（インターバル）
        self.BLOCK_SIZE = block_size
        self.BLOCK_INTV = block_intv
        # on/offのカラー
        self.COLOR_ON = color_on
        self.COLOR_OFF = color_off

    def init_row(self, x_org=2, y_org=8, col_intv=6):
        """ Initialize the display row line

        表示行を初期設定

        Args:
            x_org (int, optional): Defaults to 2.
                Origin x of the line in the number of blocks.
                原点のxをブロック数で指定。
            y_org (int, optional): Defaults to 8.
                Origin y of the line in the number of block.
                原点のyをブロック数で指定。
            col_intv (int, optional): Defaults to 6.
                Interval between each character in the number of block.
                それぞれの文字の間隔をブロック数で指定。
        """
        self.X_ORG = x_org * self.BLOCK_INTV
        self.Y_ORG = y_org * self.BLOCK_INTV
        self.COL_INTV = col_intv * self.BLOCK_INTV

    def update_col(self, col=0, num=3, base=16, blank=False):  # ある桁にある数字を表示する関数
        """[summary]

        Args:
            col (int, optional): [description]. Defaults to 0.
            num (int, optional): [description]. Defaults to 3.
            base (int, optional): [description]. Defaults to 16.
            blank (bool, optional): [description]. Defaults to False.
        """
        # numをcol桁目に表示、桁は最上位桁の左から右へ進む。
        num = num % base  # デフォルトは16進数表示
        for segment in SEGMENTS:  # 7つのセグメントのうちの、あるセグメントについて、
            if segment[num] == 1:
                color = self.COLOR_ON
            else:
                color = self.COLOR_OFF
            if blank is True:    # ブランク表示の場合は、すべてOFFで上書き
                color = self.COLOR_OFF
            # 桁の原点
            x0 = self.X_ORG + self.COL_INTV * col
            y0 = self.Y_ORG
            # ブロック1、ブロック2の座標オフセット
            x1, y1 = segment[16][0]
            x2, y2 = segment[16][1]
            # ブロック1、ブロック2の原点座標
            org1 = (x0 + x1 * self.BLOCK_INTV, y0 - y1 * self.BLOCK_INTV)
            org2 = (x0 + x2 * self.BLOCK_INTV, y0 - y2 * self.BLOCK_INTV)
            self.draw_dot(org1, color)
            self.draw_dot(org2, color)

    def draw_dot(self, org, color):
        """ draw a dot.  you need actual method in the child class.
        ドットを描く。実際のメソッドは、子クラスに実装すること。"""
        pass

    def disp_num(self, num=1234, base=16):
        """[summary]

        Args:
            num (int, optional): [description]. Defaults to 1234.
            base (int, optional): [description]. Defaults to 16.
        """
        # numを複数桁で表示する。左詰め。
        if num <= 0:
            num = 1
        num_cols = int(log(num, base)) + 1
        for col in range(num_cols):
            self.update_col(col=col, num=num // (base ** (num_cols - col - 1)), base=base)

    def disp_num2(self, rjust=4, zfil=False, num=1234, base=16):
        """[summary]

        Args:
            rjust (int, optional): [description]. Defaults to 4.
            zfil (bool, optional): [description]. Defaults to False.
            num (int, optional): [description]. Defaults to 1234.
            base (int, optional): [description]. Defaults to 16.
        """
        # numをrjust桁で右詰め表示する。桁あふれが起きると、右にずれていく。
        # zfil==Trueの時、上位桁をゼロで埋める。Falseの場合は、ブランク表示。
        if num <= 0:
            num = 1
        num_cols = int(log(num, base)) + 1
        if num_cols > rjust:
            rjust = num_cols
        for disp_col in range(rjust):
            col = disp_col + num_cols - rjust
            if col >= 0:
                self.update_col(col=disp_col, num=num // (base ** (num_cols - col - 1)), base=base)
            else:
                if zfil is True:
                    self.update_col(col=disp_col, num=0)
                else:
                    self.update_col(col=disp_col, blank=True)
