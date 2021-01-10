import webbrowser as browser
import time
import os
from pathlib import Path

import requests
import browser_cookie3
from fake_useragent import UserAgent

import filename_fixer
import config
import urllib.parse as url_parse

def get_code():

    params_url = url_parse.urlencode({
        'client_id' : config.client_id,
        'redirect_uri' : 'https://example.com',
        'response_type' : 'code',
        'scope' : 'public'
    })

    url = 'https://osu.ppy.sh/oauth/authorize?'f"{params_url}"

    browser.open_new_tab(url)

    entered_url = input("After clicking authorize in your browser, paste the url here (e.g example.com/?code=alskdndoan..) : ")

    parsed = url_parse.urlparse(entered_url)
    code = url_parse.parse_qs(parsed.query)['code'][0]

    return code


def get_access_token():

    params = {
        'client_id' : config.client_id,
        'client_secret' : config.client_secret,
        'redirect_uri' : 'https://example.com',
        'grant_type' : 'authorization_code',
        'code' : get_code()
    }
    
    response = requests.post('https://osu.ppy.sh/oauth/token', #no question mark as we aren't querying for data
        headers={
            'Accept' : 'application/json',
            'Content-Type' : 'application/x-www-form-urlencoded' #type of content we are sending in post request
        },
        data=params) #data to post

    json = response.json()

    return {
        'Authorization' : f"Bearer {json['access_token']}",
        'Accept' : 'application/json',
        'Content-Type' : 'application/json'
    }

access_token = get_access_token()

print("--------------------------------osu! UserBeatmaps--------------------------------")
user_id = input("Enter your user ID here (can be found in the url of your osu! profile): ")
number_of_maps = int(input("Enter number of most played maps you want to download (duplicates included): "))
download_video = int(input("Enter 1 if you want to download maps with video, 0 if no video for smaller file sizes: "))

response = requests.get(f"https://osu.ppy.sh/api/v2/users/{user_id}/beatmapsets/most_played?&limit={number_of_maps}", headers=access_token)
json = response.json()

filtered_beatmaps = dict() #to filter out same beatmaps that only differ by difficulty level
for beatmap in json:
    beatmapset_id = beatmap['beatmapset']['id']
    beatmapset_content = beatmap['beatmapset']

    if not beatmapset_id in filtered_beatmaps:
        filtered_beatmaps[beatmapset_id] = beatmapset_content

fake_user_agent = UserAgent().chrome #to make site think we are visiting from browser, or else request gets blocked
counter = 1

for id in filtered_beatmaps:

    title = filtered_beatmaps[id]['title']
    artist = filtered_beatmaps[id]['artist']
    
    print(f"------------------------------------\nDownloading {counter}. {title}({artist}) ....")

    file_name = filename_fixer.remove_invalid_chars(f"{title}({artist}).osz")

    if not os.path.exists('beatmaps'): #if folder already exists
        os.makedirs('beatmaps')
    elif os.path.isfile(Path('beatmaps', file_name)): #if file already exists, Path module used so linux or windows won't matter
        print(f"Skipping {file_name}. File already exists.\n------------------------------------")
        counter += 1
        continue

    download_url = f"https://osu.ppy.sh/beatmapsets/{id}/download" if download_video else f"https://osu.ppy.sh/beatmapsets/{id}/download?noVideo=1"
    headers = {'User-Agent': fake_user_agent, 'referer' : f"https://osu.ppy.sh/beatmapsets/{id}"}  # referer means which page is making the request, required or else html file is downloaded
    cookies = browser_cookie3.chrome() if config.browser == 'chrome' else browser_cookie3.firefox()

    response = requests.get(download_url, cookies=cookies, headers=headers)

    with open(Path('beatmaps', file_name), 'wb') as file:
        file.write(response.content)
        print('Download done, waiting 5 secs to start next download\n------------------------------------')

    counter += 1
    time.sleep(5) #to prevent excessive requests per minute

print('\n--------------------------------All downloads SUCCESFULLY completed--------------------------------')
#script won't work on linux, browser_cookie3 not compatible with linux desktop environments
#if desperate to make it work, launch chrome browser from the terminal with the --password-store=basic flag
#will have to login again

#duplicated calculation

#download maps in certain directory

#make sure preferred browser logged in, or else html files will be downloaded

#script display may lag behind, press enter to refresh
#file already exists