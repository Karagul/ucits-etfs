from bs4 import BeautifulSoup
import requests

page_link = 'https://www.justetf.com/uk/etf-profile.html?query=IE0005042456&groupField=index&from=search&isin=IE0005042456'

page_response = requests.get(page_link, timeout=5)

page_content = BeautifulSoup(page_response.content, "html.parser")
soup = page_content#.prettify()

textContent = []
for i in range(0, 3):
        paragraphs = page_content.find_all("p")[i].text
        textContent.append(paragraphs)

#print(soup)
print (soup.find_all('span', class_="val", limit=10))
#print (soup.identifier)
#mydivs = soup.findAll("span", {"class": "identifier"})
#print(mydivs)
