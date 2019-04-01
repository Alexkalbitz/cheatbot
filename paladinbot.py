import time

import cv2
import mss
import numpy
import pyautogui

low_hp = 50
mid_hp = 60
high_hp = 72
mana_60 = 65

with mss.mss() as sct:
    # Part of the screen to capture
    monitor = {"top": 155, "left": 1535, "width": 83, "height": 200}

    while True:
        time.sleep(0.05)
        last_time = time.time()
        mp = True
        img = numpy.array(sct.grab(monitor))
        cv2.imshow("OpenCV/Numpy normal", img)
        #print('80 ',img[0][80], img[-1][80])
        #print('40 ', img[0][40], img[-1][40])

        #hp = img[0] #at hp[0-82][0] = 113
        #mana = img[-1] #at mana[0-82][0] = 240

        if img[0][low_hp][0] != 113:
            pyautogui.press('f9')
            time.sleep(0.01)
            pyautogui.press('f12')
            mp = False
        elif img[0][mid_hp][0] != 113:
            pyautogui.press('f11')
            time.sleep(0.01)
            #pyautogui.press('f12')
            mp = True
        # elif img[0][high_hp][0] != 113:
        #     pyautogui.press('f12')
        #     mp = True

        if mp is True and img[-1][mana_60][0] != 240:
            pyautogui.press('f10')
        # Display the picture in grayscale
        # cv2.imshow('OpenCV/Numpy grayscale',
        #            cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

        #print("fps: {}".format(1 / (time.time() - last_time)))

        # Press "q" to quit
        # if cv2.waitKey(25) & 0xFF == ord("q"):
        #     cv2.destroyAllWindows()
        #     break
