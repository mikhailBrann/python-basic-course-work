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
        
        # params = {'owner_id': 1, 'access_token': self.token, 'v': '5.131', 'album_id': 'profile'}
        request_info = False
        
        # если id передали как число
        if type(user_id) == int or user_id.isdigit():
            method = 'photos.get'
            params = {'owner_id': user_id, 'v': '5.131', 'album_id': 'profile'}
            responce = self.get_vk_request(method, params)
            
            if responce:
                request_info = responce
        
        # если id передали как псевдоним    
        elif user_id.isdigit() is False:
            # получаем id пользователя
            get_user_id = self.get_vk_request('users.get', {'user_ids': user_id, 'v': '5.131'})
            user_id = get_user_id['response'][0]['id']
            
            method = 'photos.get'
            params = {'owner_id': user_id, 'v': '5.131', 'album_id': 'profile'}
            responce = self.get_vk_request(method, params)
            
            if responce:
                request_info = responce
            
    
        
            
        return request_info

