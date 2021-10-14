import requests

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

