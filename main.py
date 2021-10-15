from requests_html import HTML, HTMLSession
import random

def incercare():
    alegere = input("Alege un sinonim pentru cuvantul {cuvant}, din urmatoarele sinonime: {cuvantFals}, {cuvantReal}, {cuvantFals2}: ".format(cuvant=cuvantRandom, cuvantFals=random.choice(listacuvinte), cuvantReal='muie', cuvantFals2=random.choice(listacuvinte))).lower()
    if alegere in sinonime:
        print('Bravo!')
    else:
        print('Mai Incerca!')
        incercare()

listacuvinte=["grai","frumos","descoperim","sfiala","poveste","cancer","suparat","destept","banuit","voce","marunte","mireasma","spaima","stralucire","destept","suras","omat","lent","cantec","copil","sclipitor"]
#listacuvinte=["Mireasma"]
cuvantRandom = random.choice(listacuvinte)
sinonime=["miros", "aroma"]
session = HTMLSession()
url = 'https://www.sin0nime.com/dex/?cheie='+cuvantRandom
r = session.get(url)
incercare()
print(r.html)
