import cv2
import difflib


# Функция вычисления хэша
def CalcImageHash(image):
    crop_img = image[70:460, 20:705] # Вырезание картинки для хэширования
    resized = cv2.resize(crop_img, (8, 8), interpolation=cv2.INTER_AREA)  # Уменьшим картинку
    gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)  # Переведем в черно-белый формат
    avg = gray_image.mean()  # Среднее значение пикселя
    ret, threshold_image = cv2.threshold(gray_image, avg, 255, 0)  # Бинаризация по порогу

    # Рассчитаем хэш
    _hash = ""
    for x in range(8):
        for y in range(8):
            val = threshold_image[x, y]
            if val == 255:
                _hash = _hash + "1"
            else:
                _hash = _hash + "0"

    return _hash


def CompareHash(hash1, hash2):
    l = len(hash1)
    i = 0
    count = 0
    while i < l:
        if hash1[i] != hash2[i]:
            count = count + 1
        i = i + 1
    return count


# hash1 = CalcImageHash("pic/Guess/1011_num.png")
# hash2 = CalcImageHash("pic/Guess/1011_num++.png")
# print(hash1)
# print(hash2)
# print(CompareHash(hash1, hash2))



