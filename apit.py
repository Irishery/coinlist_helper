import requests

req_prms = {
    'id': 2
}

r = requests.put('http://127.0.0.1:5000/api/user/', params=req_prms)

print(r.json())