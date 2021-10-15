from requests_html import HTML, HTMLSession

session = HTMLSession()
r = session.get('https://www.sin0nime.com/dex/?cheie=piatra')

#cuvant = r.html.find('a', first=True)
cuvant = r.html.find('Sinonime', first=True)
print(cuvant.html)
print(r.html)
