import requests
#relace with your actual PAT from github account
headers = {"Authorization":"Bearer fffffffffffffffffffffff"}
data = '{"name":"Python Requests Module", "description":"Repository for Python Requests module"}'
resp=requests.post("https://api.github.com/user/repos", headers=headers, data=data)

print(resp.json())
print(resp.status_code)

