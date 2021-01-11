# osu! User Beatmaps Downloader

A little python script that can download any users' most played beatmaps using v2 of osu! api. Beatmaps will be downloaded into a new folder 'beatmaps'.

### Requirements
___
* Any Python from version 3.6.x to 3.8.x. Other versions are incompatible due to syntax or library issues.

### Instructions
___
1. Go to your [osu! settings](https://osu.ppy.sh/home/account/edit) and at the very bottom in the OAuth section, and click on New OAuth Application
1. Give any application name, and enter https://example.com in the URL. Then register application.
1. Open config.py with a text editor. Copy client ID into 'Client ID' instead of 0. Show client secret and copy it in 'Client Secret' between the quotes. Change browser to 'firefox' if logged into osu! through that.
1. Open the directory of the downloaded source code, type 'cmd' in the address bar of Windows Explorer on top and press Enter. Then enter the following one by one.

    ```
    python -m venv env
    env\Scripts\activate.bat
    pip install -r requirements.txt
    python userbeatmaps.py
    ```
### Notes
___
* If on a Linux system :
    1. Use python3 and pip3 instead of just python and pip in the commands above
    1. You need to use Firefox, as browser_cookie3 is not compatible with Chrome on Linux, so change browser to 'firefox' in config.py
    1. Second command will instead be
        >source env/bin/activate
* Please make sure the browser specified in config.py is logged into osu! as the cookie from that browser is extracted in the script. If not logged in, html files will be downloaded instead.
* Script may lag behind in displaying progress if command prompt is unfocued, press Enter to refresh it.
* Same beatmaps in your most played will only be downloaded once. So for example, if you want to download the top 5, and 2 of those belong to the same beatmapset, you will be downloading 4 beatmaps.
