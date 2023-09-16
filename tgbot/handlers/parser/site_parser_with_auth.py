import bs4
import requests


session = requests.Session()



link = 'https://atlasauth.b2clogin.com/f50ebcfb-eadd-41d8-9099-a7049d073f5c/B2C_1A_atoproduction_Atlas_SUSI/SelfAsserted?tx=StateProperties=eyJUSUQiOiJiNzc4NmYyZi00MDZjLTQyODQtYjAyMC0wZWM4NTI5M2Y5MmMifQ&p=B2C_1A_atoproduction_Atlas_SUSI'

header = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}


data = {
    "signInName": 'MADHUMATITAILOR',
    "password": 'Tailor@999',
    "extension_atlasCaptchaResponse": 'e8Q28',
    "extension_atlasCaptchaToken": '3eb2edfb-1abb-474d-a328-774d5e6e2eb5',
    "request_type": 'RESPONSE'
}

responce = requests.post(url=link,  data=data, headers=header).text
print(responce)