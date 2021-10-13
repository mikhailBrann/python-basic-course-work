import requests

class VkInfo:
    def __init__(self, token):
        self.token = token
    
    def get_vk_request(self, url, method, params):
        ...


    def get_vk_info(self, user_id):
        # https://api.vk.com/method/users.get?user_ids=210700286&fields=bdate&access_token=533bacf01e11f55b536a565b57531ac114461ae8736d6506a3&v=5.131
        
        responce_result = False
        upload_photo = 'https://api.vk.com/method/photos.get'


        if user_id.isdigit():
            print('integer')
        elif user_id.isdigit() is False:
            print('string')
        
        params = {'owner_id': 1, 'access_token': self.token, 'v': '5.131', 'album_id': 'profile'}
        response = requests.get(url=upload_photo, params=params)
    
        if response.status_code == 200:
            responce_result = response.json()
            
        return responce_result

