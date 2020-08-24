import json
import requests
import os
import string
import unicodedata
import time

validFilenameChars = "-_.() %s%s" % (string.ascii_letters, string.digits)
def removeDisallowedFilenameChars(filename):
    cleanedFilename = unicodedata.normalize('NFKD', filename).encode('ASCII', 'ignore')
    return ''.join(chr(c) for c in cleanedFilename if chr(c) in validFilenameChars)

user_id = int(input('Enter User ID from profile URL: '))
number_of_maps = int(input('Enter top number of maps to download: '))
osu_session_cookie = str(input('Enter osu session token, instructions in github readme: '))

print('\nThere will be a 7 second delay between each download to prevent error for too many requests')

beatmap_count = 0

offset = 0

while(number_of_maps > 0):

    r = requests.get(f'https://osu.ppy.sh/users/{user_id}/beatmapsets/most_played?offset={offset}&limit={number_of_maps}')
    data = r.json()

    try:
        os.makedirs("./songs")
    except FileExistsError:
        pass

    for beatmap in data:

        beatmap_count += 1

        beatmap_id = beatmap['beatmapset']['id']
        beatmap_title = removeDisallowedFilenameChars(str(beatmap['beatmapset']['title']))

        if beatmap_count != 1 : time.sleep(7) # delay put to prevent error 429, delay skipped for the first download

        download_url = f"https://osu.ppy.sh/beatmapsets/{beatmap_id}/download?noVideo=1"
        
        print(f'\n-------{beatmap_id}-------')
        print(download_url)
        print(f'Downloading beatmap: {beatmap_count}. ' + str(beatmap_title))
        
        cookies = {'osu_session': osu_session_cookie}
        r = requests.get(download_url, cookies=cookies)

        with open(f'./songs/{beatmap_title}.osz', 'wb') as f:  
            f.write(r.content)
        
    number_of_maps -= 51 # number of maps left
    offset += 51 # site only allows 51 downloads each request

    

        