import urllib
import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_data(query):
	USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"

	MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"

	query = query.replace(' ', '+')
	URL = f"https://google.com/search?q={query}&num=100"

	headers = {"user-agent": USER_AGENT}
	resp = requests.get(URL, headers=headers)

	if resp.status_code == 200:
		soup = BeautifulSoup(resp.content, "html.parser")
		results = []
		for g in soup.find_all('div', class_='r'):
			anchors = g.find_all('a')
			nextp = g.find_next('div', class_='s')
			#children = nextp.findChildren("div" , recursive=False)
			description = nextp.find("span", class_='st')
			if description:
				hi = description.text
			else:
				hi = ""

			if anchors:
				link = anchors[0]['href']
				title = g.find('h3').text
				item = {
					"title": title,
					"link": link,
					"description": hi
				}
				results.append(item)

		df = pd.DataFrame(results)  
		df.to_excel("flasksite/scrapdata.xlsx", index = False)
		return results[:10]
		


