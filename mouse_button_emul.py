### README ###
# This scripts emulates RIGHT MOUSE BUTTON using MIDDLE MOUSE BUTTON.

import win32api
import win32con
import time


def main():

    # Button down = 0 or 1. Button up = -127 or -128
    state_left = win32api.GetKeyState(0x01)
    state_right = win32api.GetKeyState(0x02)
    state_middle = win32api.GetKeyState(0x04)

    while True:

        left = win32api.GetKeyState(0x01)
        right = win32api.GetKeyState(0x02)
        middle = win32api.GetKeyState(0x04)

        x, y = win32api.GetCursorPos()

        if middle != state_middle:  # Button state changed
            state_middle = middle
            print(middle)

            if middle < 0:
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y)
                print('Middle Button Pressed')
                print('Mouse Coordinates: x = %d, y = %d' % (x,y))
            else:
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y)
                print('Middle Button Released')
                print('Mouse Coordinates: x = %d, y = %d' % (x,y))

        time.sleep(0.001)

main()
