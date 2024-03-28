import requests
headers = {"Authorization":"Bearer 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"}

resp=requests.delete("https://api.github.com/repos/opilonelson/Python-Requests-Mode", headers=headers)

print(resp.text)
print(resp.status_code)

