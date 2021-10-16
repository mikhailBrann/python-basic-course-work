
# Возможна такая ситуация, что мы хотим показать друзьям фотографии из социальных сетей, но соц. сети могут быть недоступны по каким-либо причинам. Давайте защитимся от такого.
# Нужно написать программу для резервного копирования фотографий с профиля(аватарок) пользователя vk в облачное хранилище Яндекс.Диск.
# Для названий фотографий использовать количество лайков, если количество лайков одинаково, то добавить дату загрузки.
# Информацию по сохраненным фотографиям сохранить в json-файл.


# Нужно написать программу, которая будет:
# 1) Получать фотографии с профиля. Для этого нужно использовать метод photos.get.
# 2) Сохранять фотографии максимального размера(ширина/высота в пикселях) на Я.Диске.
# 3) Для имени фотографий использовать количество лайков.
# 4) Сохранять информацию по фотографиям в json-файл с результатами.

# Входные данные:

# Пользователь вводит:
# 1) id пользователя vk;
# 2) токен с Полигона Яндекс.Диска. Важно: Токен публиковать в github не нужно!

# Выходные данные:
# 1) json-файл с информацией по файлу:
#     [{
#     "file_name": "34.jpg",
#     "size": "z"
#     }]
# 2) Измененный Я.диск, куда добавились фотографии.​​


# Обязательные требования к программе:
# 1) Использовать REST API Я.Диска и ключ, полученный с полигона.
# 2) Для загруженных фотографий нужно создать свою папку.
# 3) Сохранять указанное количество фотографий(по умолчанию 5) наибольшего размера (ширина/высота в пикселях) на Я.Диске
# 4) Сделать прогресс-бар или логирование для отслеживания процесса программы.
# 5) Код программы должен удовлетворять PEP8.​


# Необязательные требования к программе:
# 1) Сохранять фотографии и из других альбомов.
# 2) Сохранять фотографии из других социальных сетей. Одноклассники и Инстаграмм
# 3) Сохранять фотографии на Google.Drive.


# Советы:
# Для тестирования можно использовать аккаунт https://vk.com/begemot_korovin


from pprint import pprint
from lib_class import VkInfo,YaUploader



if __name__ == '__main__':
    vk_init = VkInfo('958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008')
    yd_file_upload = YaUploader('...')

    responce_vk = vk_init.get_vk_info('begemot_korovin')
    qantity_photo = 5
    photo_list = []

    if responce_vk:
        #  top5 = list_cat[:5]
        photo_vk = responce_vk['response']['items']

        # задаем нужное количество сохраяемых фото
        if len(photo_vk) >= qantity_photo:
            photo_vk = photo_vk[:qantity_photo]

        # получаем фото лучшего качества через подсчет площади фотографии
        for photo in photo_vk:
            photo['sizes'] = sorted(photo['sizes'], key=lambda size_photo_: (size_photo_['width'] * size_photo_['height']), reverse=True)
            photo['sizes'] = photo['sizes'][:1]

            # "file_name": "34.jpg",
            # "size": "z"

            # photo_list.apend({})
        
        dir_is = yd_file_upload._get_upload_link('test')

        pprint(dir_is)