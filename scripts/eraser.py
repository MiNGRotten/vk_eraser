import asyncio
from vk_api import VkApi, VkUserPermissions
from time import sleep

def eraser():
    print ("Enter login:")
    _login = input()
    print ("Enter password:")
    _password = input()
    print ("Enter app id:")
    _app_id = input()
    
    _session = VkApi(
        login=_login,
        password=_password,
        app_id=_app_id,
        auth_handler=auth_handler,
        scope=(VkUserPermissions.PHOTOS & VkUserPermissions.WALL))

    _session.auth()

    _api = _session.get_api()

    while True:
        _wall = _api.wall.get(count = 100)
        if _wall['count'] == 0:
            break
        for i in _wall['items']:
            _api.wall.delete(post_id=i['id'])
            sleep(2)

    while True:
        _photos = _api.photos.get(album_id='wall', count=1000)
        if _photos['count'] == 0:
            break
        for i in _photos['items']:
            _api.photos.delete(photo_id=i['id'])
            sleep(2)

def auth_handler():
    print ("Enter two auth code:")
    return input(), False

eraser()