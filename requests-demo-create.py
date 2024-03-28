import requests
headers = {"Authorization":"Bearer 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"}
data = '{"name":"Python Requests Module", "description":"Repository for Python Requests module"}'
resp=requests.post("https://api.github.com/user/repos", headers=headers, data=data)

print(resp.json())
print(resp.status_code)

