# pygame_mcpi_LCD_7seg
Introduction to Python with Pygame.
Pygameを使ってPython入門

7セグシミュレーション、LCDフォントをハンドメイドで表示するコードを通じてPyhonの書き方に慣れましょう。
Pygameウィンドウ、ラズパイのマイクラ世界に表示します。

注：ラズパイとの互換性を考慮して、Python 3.7を想定しています。
Pygameは Macで1.9.6が動かなくなったので、2.0.1です。ラズパイ4／Busterでも、Pygame2.0.1が使えます。Pygame ZeroがPygame1.9.6を要求しますが、2.0.1でも問題ない模様。Pygame2.0.1をインストール、続いてPygame Zeroをインストールすればオッケー。

### LCDフォント、7セグシミュレーション
 - demo_LCD_font_PG_zero.py: 5x7のLCDフォント制作練習用。
 - demo_LCD_font_PG.py: LCDフォント表示 Pygame用。
 - demo_seven_seg_PG.py: 7セグのシミュレーション、各セグメントを2ブロックで構成。Pygame用。

 - demo_LCD_font_PG.py: LCDフォント表示 マイクラ用。
 - demo_seven_seg_PG.py: 7セグのシミュレーション、マイクラ用

### モジュール
 - lcdfont.py: LcdFont  デザイン
 - lcdfontdisp.py: LcdFontDisplay, LcdFontDisplayPG, LcdFontDisplayMC  表示クラス
 - 
 - sevensegfont.py: SevenSegFont  デザイン
 - sevensegdisp.py: SevenSegDisplay, SevenSegDisplayPG, SevenSegDisplayMC  表示クラス