import requests

req = requests.get("http://www.lemonde.fr")
print(req.text)














req = requests.get("http://www.floatrates.com/daily/usd.json")
data = req.json()
print(data["eur"])
