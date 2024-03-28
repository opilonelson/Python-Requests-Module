import requests
headers = {"Authorization":"Bearer ffffffffffffffffffffffffffffff"}
#replace username with your github account username
resp=requests.delete("https://api.github.com/repos/username/Python-Requests-Mode", headers=headers)

print(resp.text)
print(resp.status_code)

