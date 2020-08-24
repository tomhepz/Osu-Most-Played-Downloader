# Download Osu players most played songs

## What you'll need
### This git repository
* Download in the top right as a zip file, or type the git clone url in the same place into your powershell/cmd .
### Osu session token
* Go to chrome, log into OSU
* Hit F12, open application tab on top. (Might be under the >> drop down)
* In storage on left under cookies, click 'https://osu.ppy.sh'
* There should be a row called 'osu_session' , copy all the text on the right of it
* This is your osu_session token, don't share it with anyone
### Osu players ID
* Go to their (or your own) profile and in the URL, take the number
### Number of songs you want to download from their top songs
* Self explanatory
### Python 3
* https://www.python.org/downloads/
### requests library
* Once python is installed, open powershell and type: `pip install requests`

## I'm ready
* Run python script in powershell/cmd by changing to that directory and typing `python .\OsuDownloader.py`
* Enter everything you got ready earlier, it should download the songs into the directory `.\songs\`
* Duplicate entries found due to difficulty or mods will not be downloaded again

## What does it look like?
The output should look something like this as it downloads the songs:
```
-------362718-------
https://osu.ppy.sh/beatmapsets/362718/download?noVideo=1
Downloading beatmap: IM A BELIEVER

-------264819-------
https://osu.ppy.sh/beatmapsets/264819/download?noVideo=1
Downloading beatmap: Chameleon Love  feat.Kano

-------147177-------
https://osu.ppy.sh/beatmapsets/147177/download?noVideo=1
Downloading beatmap: Idola no Circus

-------104801-------
https://osu.ppy.sh/beatmapsets/104801/download?noVideo=1
Downloading beatmap: Zetsubousei Hero Chiryouyaku (TV Size)

-------264819-------
https://osu.ppy.sh/beatmapsets/264819/download?noVideo=1
Downloading beatmap: Chameleon Love  feat.Kano

-------147962-------
https://osu.ppy.sh/beatmapsets/147962/download?noVideo=1
Downloading beatmap: Omega Rhythm
```