import requests

class VkInfo:
    def __init__(self, token):
        self.token = token

    def get_vk_info(self, user_id):
        # https://api.vk.com/method/users.get?user_ids=210700286&fields=bdate&access_token=533bacf01e11f55b536a565b57531ac114461ae8736d6506a3&v=5.131
        
        responce_result = False
        upload_url = 'https://api.vk.com/method/users.get'
        
        params = {'user_ids': user_id, 'access_token': self.token, 'v': '5.131', 'fields': 'photo_max'}
        response = requests.get(url=upload_url, params=params)
    
        if response.status_code == 200:
            responce_result = response.json()
            
        return responce_result

