import requests

url = "http://127.0.0.1:5000/check"
data = {"input": "abcdef1234567890abcdef1234567890"}
res = requests.post(url, json=data)

print(res.json())
