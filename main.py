import random
import unidecode
import os
from requests_html import HTML, HTMLSession

def incercare():
    os.system("color b0")
    os.system("cls")
    alegere = input("   Alege un sinonim pentru cuvantul {cuvant}, din urmatoarele sinonime: {cuvantFals},{cuvantReal}, {cuvantFals2}: ".format(cuvant=cuvantRandom, cuvantFals=random.choice(listacuvinte), cuvantReal=cuvantReal, cuvantFals2=random.choice(listacuvinte))).lower()
    if alegere in sinonim:
        print('Bravo!')
    else:
        print('Mai Incerca!')
        incercare()

listacuvinte=["grai","frumos","sfiala","poveste","voce","spaima","suras","omat"]
cuvantRandom = random.choice(listacuvinte)
url = 'https://dexonline.ro/definitie-sinonime/'+cuvantRandom+'/json'
session = HTMLSession()
r = session.get(url)
#print(r.html)
#sinonim = str(r.html.search('${}.$')[0]).replace(u"\u0103", "a")
sinonim = str(r.html.search('${}.$')[0].encode('utf-8').decode('unicode-escape'))
cuvantReal=sinonim.split(',')[-1]
#print(cuvantReal)
incercare()



