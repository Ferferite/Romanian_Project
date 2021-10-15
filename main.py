from requests_html import HTML, HTMLSession
import random

#listacuvinte=["grai","frumos","descoperim","sfiala","poveste","cancer","suparat","destept","banuit","voce","marunte","mireasma","spaima","stralucire","destept","suras","omat","lent","cantec","copil","sclipitor"]
listacuvinte=["Mireasma"]
cuvantRandom = random.choice(listacuvinte)
sinonime=["miros", "aroma"]
session = HTMLSession()
url = 'https://www.sin0nime.com/dex/?cheie='+cuvantRandom
r = session.get(url)
alegere = input('Sinonim pentru cuvantul "'+cuvantRandom+'": ').lower()
if alegere in sinonime:
    print('Bravo!')
else:
    print('Mai Incerca!')
print(r.html)
