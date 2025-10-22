"""
myfirstmacroboard
elton
thanks to palmacas (https://github.com/palmacas/MacroBoard/blob/master/firmware/code.py)
and hackpad (https://hackpad.hackclub.com/guide)
"""

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.extensions.rgb import RGB, AnimationModes

keyboard = KMKKeyboard()

PINS = [board.D3, board.D4, board.D2, board.D1]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# RGB LEDs settings
rgb_ext = RGB(
    pixel_pin=board.D0,
    num_pixels=2,
    hue_default=180,
    sat_default=255,
    val_default=15,
    val_limit=25,
    animation_speed=1,
    animation_mode=AnimationModes.RAINBOW,
    refresh_rate=30,
)
keyboard.extensions.append(rgb_ext)

# Keymap
keyboard.keymap = [
    [KC.A, KC.B, KC.C, KC.D]
]

if __name__ == '__main__':
    keyboard.go()