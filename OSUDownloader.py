import json
import requests

user_id = int(input('Enter User ID from profile URL: '))
number_of_maps = int(input('Enter top number of maps to download: '))
osu_session_cookie = str(input('Enter osu session token, instructions in github readme: '))

r = requests.get(f'https://osu.ppy.sh/users/{user_id}/beatmapsets/most_played?offset=0&limit={number_of_maps}')
data = r.json()

for beatmap in data:
    beatmap_id = beatmap['beatmapset']['id']
    beatmap_title = str(beatmap['beatmapset']['title'])
    download_url = f"https://osu.ppy.sh/beatmapsets/{beatmap_id}/download?noVideo=1"
    
    print(f'\n-------{beatmap_id}-------')
    print(download_url)
    print('Downloading beatmap: ' + str(beatmap_title))
    
    cookies = {'osu_session': osu_session_cookie}
    r = requests.get(download_url, cookies=cookies)
    
    with open(f'./songs/{beatmap_title}.osz', 'wb') as f:  
        f.write(r.content)