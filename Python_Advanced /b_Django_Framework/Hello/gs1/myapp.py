# thsi python application communicates with the api 
# it can be of python, java, c++ or any language

import requests
URL = "http://127.0.0.1:8000/stuinfo/3" # url which it hits

r = requests.get(url=URL)

data = r.json()

print(data)