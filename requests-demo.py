import requests
headers = {"Authorization":"Bearer ffffffffffffffffffffff"}
data = '{"name":"Python Requests Module4"}'
resp=requests.patch("https://api.github.com/repos/username/Python-Requests-Module3", headers=headers, data =data)

print(resp.text)
print(resp.status_code)
print(resp.headers)
print(resp.content)