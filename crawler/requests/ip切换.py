import requests
import random
ip_list=[
    "124.152.185.185:43291",
    "60.255.230.185:808",
    "61.152.230.26:8080",
]
proxies ={'http': random.choice(ip_list)}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}

url="http://httpbin.org/ip"
response = requests.get(url=url, headers=headers, proxies=proxies).text
print(response)