import requests
from datetime import datetime

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    # метод создает директорию на яндекс диске с уникальным именем
    def _put_upload_dir(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        data = datetime.now()

        disk_file_path = disk_file_path + data.strftime("__(%d.%m.%Y)_%H-%M-%S") + str(data.microsecond)
        params = {'path': disk_file_path}
        response = requests.put(url=upload_url, headers=headers, params=params)

        # тут проверяем, есть ли директория в облачном хранилище
        if response.status_code == 201:
            return disk_file_path
        else:
            return False


    def _upload_files(self, disk_file_path, file_name, url_to_file):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload/'
        headers = self.get_headers()
        path_to_file = disk_file_path + '/' + file_name

        params = {'path': path_to_file, 'url': url_to_file}
        response = requests.post(url=upload_url, headers=headers, params=params)

        # тут проверяем, есть ли директория в облачном хранилище
        if response.status_code == 201:
            return response.json()
        else:
            return False


    # def upload(self, file_path: str='', hard_disk_dir='files'):
    #     """Метод загружает файлы из директории {hard_disk_dir} на яндекс диск"""
    #     response = self._get_upload_link(file_path)
    
    #     if response:
    #         url = response['href']
    #         response = requests.put(url=url, data=open(path_to_file + file_.name, 'rb'))
    #         response.raise_for_status()
    #         if response.status_code == 201:
    #             if file_path:
    #                 print(f'Файл {file_.name} успешно загружен в {file_path}')
    #             else:
    #                 print(f'Файл {file_.name} успешно загружен в корневую папку диска')
    #     else:
    #         print(f'Ошибка: директории {file_path} нет в облачном хранилище.\nУкажите существующую директорию или оставьте поле пустым для загрузки в корень хранилища')
    #         break

class VkInfo:
    def __init__(self, token):
        self.token = token
    
    def get_vk_request(self, method, params = {}):
        responce_result = False
        params.setdefault('access_token', self.token)
        url = 'https://api.vk.com/method/' + method
        
        response = requests.get(url=url, params=params)
        
        if response.status_code == 200:
            responce_result = response.json()
            
        return responce_result


    def get_vk_info(self, user_id):
        # https://api.vk.com/method/users.get?user_ids=210700286&fields=bdate&access_token=533bacf01e11f55b536a565b57531ac114461ae8736d6506a3&v=5.131
        request_info = False

        # если id передали как псевдоним 
        if str(user_id).isdigit() is False:
            # получаем id пользователя
            get_user_id = self.get_vk_request('users.get', {'user_ids': user_id, 'v': '5.131'})
            user_id = get_user_id['response'][0]['id']
        
        get_photo_params = {'owner_id': user_id, 'v': '5.131', 'album_id': 'profile', 'extended': 'likes', 'photo_sizes': '1'}
        get_photo_method = 'photos.get'
        
        responce = self.get_vk_request(get_photo_method, get_photo_params)
        if responce:
            request_info = responce
        
        return request_info

