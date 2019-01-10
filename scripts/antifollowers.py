import asyncio
from vk_api import VkApi, VkUserPermissions
from time import sleep

def antifollowers():
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

    _not_banned = []

    while True:    
        _followers = _api.users.getFollowers(count=1000)
        if _followers['count'] == 0 or _followers['items'] == _not_banned:
            break
        for i in _followers['items']:
            try:       
                _api.account.ban(owner_id=i)
            except:
                print('{} not banned'.format(i))
                _not_banned.append(i)
            sleep(2)
    
    print('Wait 10 minutes...')
    sleep(600)

    while True:
        _banned = _api.account.getBanned(count=200)
        if _banned['count'] == 0:
            break
        for i in _banned['items']:
            try:       
                _api.account.unban(owner_id=i['id'])
            except:
                print('{} not unbanned'.format(i))
            sleep(2)

def auth_handler():
    print ("Enter two auth code:")
    return input(), False

antifollowers()  