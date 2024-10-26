import requests

link = "https://gist.githubusercontent.com/dariusz-wozniak/656f2f9070b4205c5009716f05c94067/raw/b291d58154c85dad840859fef4e63efb163005b0/list-of-countries.txt"
req = requests.get(link)




print(req.content)