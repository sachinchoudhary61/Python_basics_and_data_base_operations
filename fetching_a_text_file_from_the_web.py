# fetching the text file from the web
import requests
url = 'http://uiit.ac.in/'
r = requests.get(url)


print(r.status_code) # should be 200
print(r.content) # you get a byte literal
