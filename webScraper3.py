from bs4 import BeautifulSoup
import requests

source = requests.get("http://famous-mathematicians.org/")
soup = BeautifulSoup(source.text, "lxml")

table = soup.find("table", class_="toplist")
for mathematician in table.find_all("td"):
    name = mathematician.a.text
    famous = mathematician.em.text
    print("Name:", name)
    print("Famous for:", famous, "\n")
