import requests
headers = {"Authorization":"Bearer ffffffffffffffffffffffffffffff"}

resp=requests.delete("https://api.github.com/repos/username/Python-Requests-Mode", headers=headers)

print(resp.text)
print(resp.status_code)

