from lib_class import VkInfo,YaUploader


def upload_foto_from_vk(disc_tokken, user_id, photo_quantity):
    vk_init = VkInfo('958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008')
    yd_file_upload = YaUploader(disc_tokken)

    responce_vk = vk_init.get_vk_info(user_id)

    # значение по умолчанию, если пользователь не указал кол-во фото
    if photo_quantity == '':
        photo_quantity = 5

    qantity_photo = int(photo_quantity)
    photo_list = []

    if responce_vk:
        photo_vk = responce_vk['response']['items']

        # задаем нужное количество сохраяемых фото
        if len(photo_vk) >= qantity_photo:
            photo_vk = photo_vk[:qantity_photo]

        # создаем директорию на удаленном диске под файл
        photo_dir = yd_file_upload._put_upload_dir('VK')

        print('Файлы загружаются:\n')
        for photo in photo_vk:
            if photo_dir:
                # определяем лучшее по размеру фото
                photo['sizes'] = sorted(photo['sizes'], key=lambda size_photo_: (size_photo_['width'] * size_photo_['height']), reverse=True)
                photo['sizes'] = photo['sizes'][:1]
                file_name = ''

                # проверяет количество одинаковых значений в списке словарей
                check_like = len(list(filter(lambda item: item['likes']['count'] == photo['likes']['count'], photo_vk)))
                
                if check_like > 1:
                    file_name = f"{photo['likes']['count']}_{photo['date']}.jpg"
                else:
                    file_name = f"{photo['likes']['count']}.jpg"

                response_result = yd_file_upload._upload_files(photo_dir, file_name, photo['sizes'][0]['url'])

                if response_result:
                    print(f'Файл {file_name} загружен в директорию {photo_dir}\n')
                    photo_list.append({"file_name": file_name, "size": photo['sizes'][0]['type']})

        return photo_list


if __name__ == '__main__':
    
    say_hello = '''
    Программа создана для бекапа фотографий со страницы ВК.
    Введите последовательно следующие данные:
    1) Токен от Яндекс.диск (доступен по адресу: https://yandex.ru/dev/disk/poligon/)
    2) Id пользователя в ВК
    3) количество фотографий для сохранения (если оставите поле пустым, сохранятся 5 фото)\n 
    '''
    print(say_hello)

    user_disk_token = input('пожалуйста, введите токен от Яндекс.диск ==> ')
    vk_id = input('пожалуйста, введите id пользователя в ВК ==> ')
    photo_qantity = input('пожалуйста, введите количество фотографий ==> ')

    while True:
        if photo_qantity == '':
            break
        elif str(photo_qantity).isdigit() is False or int(photo_qantity) <= 0:
            print('Введите число больше 0')
            photo_qantity = input('пожалуйста, введите количество фотографий ==> ')
        else:
            break


    upload_result = upload_foto_from_vk(user_disk_token, vk_id, photo_qantity)
    print(upload_result)

    
            
          