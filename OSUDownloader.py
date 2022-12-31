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

cookies = {'osu_session': osu_session_cookie}
dirname = os.path.realpath(os.path.dirname(__file__))

os.makedirs(f"{dirname}/songs", exist_ok = True)
print(f"Download directory is stored in: {dirname}/songs")

unable_to_download = {}
offset = 0

# osu api only allows 100 maps per request
# so we have to make multiple requests if the user has more than 100 maps
# the offset is the number of maps to skip
while number_of_maps > 0:
    limit = 100 if number_of_maps >= 100 else number_of_maps
    requesturl = f'https://osu.ppy.sh/users/{user_id}/beatmapsets/most_played?offset={offset}&limit={limit}'

    r = requests.get(requesturl)
    data = r.json()

    for beatmap in data:
        beatmap_id = beatmap['beatmapset']['id']
        beatmap_title = removeDisallowedFilenameChars(str(beatmap['beatmapset']['title']))
        
        beatmap_url = f"https://osu.ppy.sh/beatmapsets/{beatmap_id}"
        download_url = f"{beatmap_url}/download?noVideo=1"

        # Download only if the beatmap isn't already downloaded
        if not os.path.isfile(f'{dirname}/songs/{beatmap_title}.osz'):
            try:
                r = requests.get(beatmap_url, cookies=cookies, headers = {'User-agent': 'osudownloader'})
                # Checks to see if the beatmap is downloadable, if not then use beatconnect as a fallback
                if "\"download_disabled\":true" in r.text:
                    download_url = f"https://beatconnect.io/b/{beatmap_id}"
            except Exception as e:
                unable_to_download[beatmap_title] = beatmap_url
                time.sleep(3)
                continue

            print(f'\n-------{beatmap_id}-------')
            print(download_url)
            print('Downloading beatmap: ' + str(beatmap_title))
            try:
                r = requests.get(download_url, cookies=cookies, headers = {'User-agent': 'osudownloader'})
                with open(f'{dirname}/songs/{beatmap_title}.osz', 'wb') as f:  
                    f.write(r.content)
            except Exception as e:
                unable_to_download[beatmap_title] = beatmap_url
            # Sleep for 3 seconds to prevent getting rate limited
            time.sleep(3)
    number_of_maps -= 100
    offset += 100

# Print out the beatmaps that couldn't be downloaded
if unable_to_download:
    print("Unable to download these songs:")
    for beatmap_title, beatmap_url in unable_to_download.items():
        print(beatmap_title + ":" + beatmap_url)