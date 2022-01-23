import requests


file1 = open('file.txt', 'w', encoding='utf-8')
r = requests.get('https://steamcommunity.com/market/')
file1.write(r.text)
file1.close()
