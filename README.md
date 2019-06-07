# Download Osu players top songs

## What you'll need
### This git repository
* Download in the top right as a zip file, or type the git clone url in the same place into your powershell/cmd 
### Osu session token
* Go to chrome, log into OSU
* Hit F12, open application tab on top
* In storage on left under cookies, click 'https://osu.ppy.sh'
* There should be a row called 'osu_session' , copy all the text on the right of it
* This is your osu_session token, don't share it with anyone
### Osu players ID
* Go to their (or your own) profile and in the URL, take the number
### Number of songs you want to download from their top songs
* Self explanitory
### Python 3
* https://www.python.org/downloads/
### requests library
* Once python is installed, open powershell and type: `pip install requests`

## I'm ready
* Run python script in powershell/cmd by changing to that directory and typing `python .\OsuDownloader.py`
* Enter everything you got ready earlier, it should download the songs into the directory `.\songs\`
