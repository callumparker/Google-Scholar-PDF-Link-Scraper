from lxml import html
from random import randint
from time import sleep
import requests
import urllib
import wget

paperFile = urllib.URLopener()

numPages = input("How many pages do you want to scrape? ")
searchQuery = raw_input("Search query (separated by +)? ")
file = open("pdflinks.txt", "w")
paperCount = 0

for x in range(0, int(numPages)):
	sleep(randint(1,5))
	print("PAGE NUM: " + str(x))
	page = requests.get('https://scholar.google.com.au/scholar?start=' + str(x * 10) + '&q=' + searchQuery)
	tree = html.fromstring(page.content)
	hrefs = tree.xpath('//div[@class="gs_or_ggsm"]/a')

	for href in hrefs:
		print(href.attrib['href'])
		file.write(href.attrib['href'] + "\n")
		paperFile = wget.download(href.attrib['href'], "paper" + str(paperCount) + ".pdf")
		paperCount = paperCount + 1

file.close()
print("Successfully gathered the links!")