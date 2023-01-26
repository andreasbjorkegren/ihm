import requests
import json



base_url = 'http://127.0.0.1:5000/'
user = {"name":"Andreas", "password":"secret password", "age": 28}  

r = requests.post(base_url + "users/2", json.dumps(user))
print(r.json())

r = requests.get(base_url + "users/1")
print(r.json())
