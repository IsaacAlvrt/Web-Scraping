#Reading news from "la jornada" 
from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.jornada.com.mx/ultimas/economia/").text
soup = BeautifulSoup(source, "lxml")

for noticia in soup.find_all("div",class_="col-7 col-md-6 col-lg-9"):
	headline = noticia.h2.a.text
	summary = noticia.p.text
	print("Headline:\n" + headline)
	print("Summary:",summary)
	print("")
