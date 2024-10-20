import requests
from PIL import Image
# Загрузка изображения из интернета с помощью библиотеки requests
url = "https://avatars.mds.yandex.net/i?id=4361d8fa88a5e188370c010dd18a4025_l-5194260-images-thumbs&n=13"
file_path = 'image1.jpg'
response = requests.get(url)
if response.status_code == 200:
    with open(file_path, 'wb') as file:
        file.write(response.content)
else:
    print(f"Изображение не загружено, код ответа сервера {response.status_code}")

"""Модуль Requests предоставляет возможность управления HTTP-запросами при помощи языка Python. Инструментарий 
библиотеки широкий и рассчитан на все случаи взаимодействия с web-приложениями:
– поддержка постоянного HTTP-соединения и его повторное использование;
– применение международных и национальных доменов;
– использование Cookie: передача и получение значений в формате ключ: значение;
– автоматическое декодирование контента;
– SSL верификация;
– аутентификация пользователей на большинстве ресурсов с сохранением;
– поддержка proxy при необходимости;
– загрузка и выгрузка файлов;
– стриминговые загрузки и фрагментированные запросы;
– задержки соединений;
– передача требуемых заголовков на web-ресурсы и др."""

# Форматирвание изображения с помощью библиотеки pillow
image = Image.open('image1.jpg')
print(image.format, image.size, image.mode)
image = image.resize((800, 600))
image = image.crop((0, 80, 500, 380))
image.show()
image.save('new_image.jpg')

"""Pillow — самая популярная библиотека для работы с изображениями в Python. С помощью неё картинки можно открывать,
 изменять, вращать, накладывать фильтры и даже работать с отдельными пикселями."""

# Работа с массивами используя библиотеку NumPy
import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
b = a.reshape(4, 2)
c = b.copy() + 2
d = b + c
d_transposet = d.transpose()
x = np.vstack([a, d_transposet])
print(x)

"""NumPy — это открытая бесплатная библиотека для Python.Она ускоряет работу с многомерными массивами и матрицами,
а также позволяет вычислять много высокоуровневых математических функций при работе с массивами данных.
Это упрoщает работу аналитика данных, позволяя ему быстро проводить сложные вычисления."""
