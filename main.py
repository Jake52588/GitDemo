import cv2
import pytesseract
import numpy as np
import pyautogui as pg
import time as tm
import open_cv as my_cv

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
custom_config = '--psm 8 -c tessedit_char_whitelist=0123456789'

img_hash = {'0100000011110000111100001111110011111100111100001111000000000000': 'Шрэк',
            '0000000000001110000011110011111100111111000111110001111100011111': 'Клиника',
            '0000000000000000000000000011111000111111001111110011111101111111': 'Зависнуть в Палм-Спвингс',
            '0000000000000000110000001111110011111100111100001111100011111000': 'Одержимость',
            '0100000011110000111111001111110011111100111110001111000000000000': 'Крепкий орешек',
            '0100000011110000111100001111110011111100111110001111000000000000': 'Темный рыцарь: Возрождение\nлегенды',
            '0000000000001110000011110011111100111111000111110001111100001111': 'Король говорит!'}

# *************
# Нащалама
i = 1000

while True:
    tm.sleep(0.8)  # Задержка
    image = pg.screenshot(region=(1575, 287, 736, 660))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    ret, image_th = cv2.threshold(image, 150, 255, cv2.THRESH_TOZERO)

    hash_my = my_cv.CalcImageHash(image)
    if hash_my in img_hash:
        print(img_hash[hash_my])
    else:
        print('---NOUP---')
        pic = f'pic/{str(i)}_num.png'
        cv2.imwrite(pic, image)
        i += 1
# Point(x=1575, y=287)
# Point(x=2311, y=947)

# region=(3378, 328, 1388, 897))
