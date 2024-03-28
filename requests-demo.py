import requests
headers = {"Authorization":"Bearer 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"}
data = '{"name":"Python Requests Module"}'
resp=requests.patch("https://api.github.com/repos/opilonelson/Python-Requests-Mode", headers=headers, data =data)
#headers = {"Authorization":"Bearer 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"}
#data = '{"name":"Python Requests Mode", "description":"A repository for Python requests module"}'
#resp=requests.post("https://api.github.com/user/repos", headers=headers, data=data)

print(resp.text)
print(resp.status_code)
#print(resp.headers)
#print(resp.content)

#"Authorization: Bearer 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"
