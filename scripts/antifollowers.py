import asyncio
from aiovk import API, ImplicitSession
from time import sleep

async def antifollowers():
    print ("Enter login:")
    login = input()
    print ("Enter password:")
    password = input()
    print ("Enter app id:")
    app_id = input()
    
    session = ImplicitSession(login, password, app_id, ['friends'])
    await session.authorize()

    api = API(session)

    not_banned = []

    while True:    
        followers = await api.users.getFollowers(count=1000)
        if followers['count'] == 0 or followers['items'] == not_banned:
            break
        for i in followers['items']:
            try:       
                await api.account.ban(owner_id=i)
            except:
                print('{} not banned'.format(i))
                not_banned.append(i)
            sleep(2)
    
    print('Wait 10 minutes...')
    sleep(600)

    while True:
        banned = await api.account.getBanned(count=200)
        if banned['count'] == 0:
            break
        for i in banned['items']:
            try:       
                await api.account.unban(owner_id=i['id'])
            except:
                print('{} not unbanned'.format(i))
            sleep(2)
    session.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(antifollowers())    