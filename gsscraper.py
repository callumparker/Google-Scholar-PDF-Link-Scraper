from lxml import html
from random import randint
from time import sleep
import requests
import urllib

testfile = urllib.URLopener()

numPages = input("How many pages do you want to scrape? ")
file = open("pdflinks.txt", "w")
paperCount = 0

for x in range(0, int(numPages)):
	sleep(randint(1,2))
	print("PAGE NUM: " + str(x))
	page = requests.get('https://scholar.google.com.au/scholar?start=' + str(x * 10) + '&q=source:Pervasive+source:Displays&hl=en&as_sdt=0,5&as_ylo=2016')
	tree = html.fromstring(page.content)
	hrefs = tree.xpath('//div[@class="gs_or_ggsm"]/a')

	for href in hrefs:
		print(href.attrib['href'])
		file.write(href.attrib['href'] + "\n")
		testfile.retrieve(href.attrib['href'], "paper" + str(paperCount) + ".pdf")
		paperCount = paperCount + 1

file.close()
print("Successfully gathered the links!")	

# https://scholar.google.com.au/scholar?start=' + str(x * 10) + 'as_vis=1&q=%22public+display%22+%22digital+signage%22+personalisation&hl=en&as_sdt=1,5
# https://scholar.google.com.au/scholar?start=' + str(x * 10) + '&q=%22public+display%22+%22digital+signage%22+observation+-education+-cost&hl=en&as_sdt=1,5&as_vis=1