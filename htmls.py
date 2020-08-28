import requests, bs4

res = requests.get("http://m.meteo.pl/lublin/60")
res.raise_for_status()
mmeteo = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(mmeteo))

elems=mmeteo.select("body > article > div.col4_60.miasto > a")
print(elems)
print(elems[0].getText())
print(elems[0].attrs)
