import asyncio
from aiovk import API, ImplicitSession
from time import sleep

async def eraser():
    print ("Enter login:")
    login = input()
    print ("Enter password:")
    password = input()
    print ("Enter app id:")
    app_id = input()
    
    session = ImplicitSession(login, password, app_id, ['photos', 'wall'])
    await session.authorize()

    api = API(session)

    while True:
        wall = await api.wall.get(count = 100)
        if wall['count'] == 0:
            break
        for i in wall['items']:
            await api.wall.delete(post_id=i['id'])
            sleep(2)

    while True:
        photos = await api.photos.get(album_id='wall', count=1000)
        if photos['count'] == 0:
            break
        for i in photos['items']:
            await api.photos.delete(photo_id=i['id'])
            sleep(2)

    session.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(eraser())