import pyautogui
import cv2
from PIL import ImageGrab
from time import sleep
import numpy as np


def initializePyAutoGUI():
    pyautogui.FAILSAFE = True


def take_capture(magnification):
    mx, my = pyautogui.position()
    x = mx - 15
    y = my - 15
    capture = ImageGrab.grab(
        bbox=(x, y, x + 30, y + 30)
    )
    arr = np.array(capture)
    res = cv2.cvtColor(
        cv2.resize(
            arr,
            None,
            fx=magnification,
            fy=magnification,
            interpolation=cv2.INTER_CUBIC
        ), cv2.COLOR_BGR2GRAY
    )
    return res


def autofish(tick_interval, threshold, magnification):
    pyautogui.rightClick()
    sleep(2)
    img = take_capture(magnification)

    while np.sum(img == 0) > threshold:
        img = take_capture(magnification)
        sleep(tick_interval)
        cv2.imshow('window', img)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
    pyautogui.rightClick()
    sleep(1)


def main():
    initializePyAutoGUI()
    sleep(5)
    i = 0
    while i < 100:
        autofish(0.01, 0, 5)
        i += 1


if __name__ == "__main__":
    main()