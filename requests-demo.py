import requests
#replace with your actual PAT from github account
headers = {"Authorization":"Bearer ffffffffffffffffffffff"}
data = '{"name":"Python Requests Module4"}'
#replace username with your github account username
resp=requests.patch("https://api.github.com/repos/username/Python-Requests-Module3", headers=headers, data =data)

print(resp.text)
print(resp.status_code)
print(resp.headers)
print(resp.content)
