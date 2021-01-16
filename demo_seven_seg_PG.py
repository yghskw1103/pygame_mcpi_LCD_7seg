# demo for 7-segment simulation
# using the class 'Seven_seg' in seven_seg_pg.py
# pylint: disable=invalid-name

import pygame
from sevensegdisp import SevenSegDisplay
from pygame.locals import Rect

DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
CYAN = (120, 120, 250)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([400, 320])
pygame.display.set_caption("pygame 7-segment display simulation")
screen.fill(DARK_GRAY)


class SevenSegDisplayPG(SevenSegDisplay):
    """  """
    def draw_dot(self, org, color):
        """ draw a dot """
        pygame.draw.rect(self.screen, color, Rect(org[0], org[1],
                         self.BLOCK_SIZE, self.BLOCK_SIZE))


display1 = SevenSegDisplayPG(screen)
display1.init_col(block_size=6, block_intv=8, color_on=GREEN, color_off=GRAY)
display1.init_row(x_org=8, y_org=8, col_intv=6)

display2 = SevenSegDisplayPG(screen)
display2.init_col(block_size=6, block_intv=8, color_on=CYAN, color_off=GRAY)
display2.init_row(x_org=2, y_org=16, col_intv=6)

display3 = SevenSegDisplayPG(screen)
display3.init_col()
display3.init_row(x_org=20, y_org=60, col_intv=6)

display4 = SevenSegDisplayPG(screen)
display4.init_col()
display4.init_row(x_org=2, y_org=70, col_intv=6)


running = True
# infinite loop top ----
while running:
    for count in range(16 ** 4):  # 0から65535まで
        # press ctrl-c or close the window to stop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if not running:
            break
        # 「for count」のループから抜ける。whileループも抜ける。

        display1.update_col(col=0, num=count // (16 ** 3))  # 4096の位
        display1.update_col(col=1, num=count // (16 ** 2))  # 256の位
        display1.update_col(col=2, num=count // 16)         # 16の位
        display1.update_col(col=3, num=count)               # 1の位

        display2.update_col(col=0, num=count // (10 ** 4), base=10)  # 1000の位
        display2.update_col(col=1, num=count // (10 ** 3), base=10)  # 1000の位
        display2.update_col(col=2, num=count // (10 ** 2), base=10)  # 100の位
        display2.update_col(col=3, num=count // (10 ** 1), base=10)  # 10の位
        display2.update_col(col=4, num=count // (10 ** 0), base=10)  # 1の位

        display3.disp_num2(zfil=False, rjust=3, num=count, base=10)

        display4.disp_num2(zfil=True, rjust=16, num=count, base=2)

        pygame.display.flip()  # update_col
        clock.tick(20)  # FPS, Frame Per Second
    screen.fill(DARK_GRAY)
# infinit loop bottom ----

pygame.quit()
