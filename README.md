# osu! User Beatmaps Downloader

A little python script that can download any users' most played beatmaps using v2 of osu! api. 

### Requirements
___
* Python 3+

### Instructions
___
1. Go to your osu! settings and at the very bottom in the OAuth section, and click on New OAuth Application
1. Give any application name, and enter https://example.com in the URL. Then register application.
1. Copy 'Client ID' into config.py instead of 0 and the 'Client Secret' between the quotes. Change browser to 'firefox' if logged into osu! through that.
1. Open the directory of the downloaded source code, type 'cmd' in the address bar of Windows Explorer on top and press Enter. Then enter the following one by one.
```
python -m venv env
env\Scripts\activate.bat
pip install -r requirements.txt
