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

        dir_path = disk_file_path + data.strftime("%d.%m.%Y_%H.%M.%S_") + str(data.microsecond)
        params = {'path': dir_path}
        response = requests.put(url=upload_url, headers=headers, params=params)

        # тут проверяем, есть ли директория в облачном хранилище
        if response.status_code == 201:
            return dir_path
        else:
            return False

    def _file_exists(self, file_path, serch_file_name):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()

        full_path_to_file = f'{file_path}/{serch_file_name}'
        params = {'path':  str(full_path_to_file)}
        response = requests.get(url=url, headers=headers, params=params)

        return response.status_code
        
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

