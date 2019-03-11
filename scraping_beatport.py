from bs4 import BeautifulSoup
import requests

#r = requests.get('https://www.beatport.com/label/spinnin-records/1609/tracks')
#f = open("testFile.txt", "w")
#f.write(r.text.encode("utf-8"))
f = open("testFile.txt", "r")
y = 1
for x in f:
	soup = BeautifulSoup(x, "html.parser") 
	get_name = soup.find('span', {'class': 'buk-track-primary-title'})
	if get_name is not None:
		name = get_name.text.strip() # strip() is used to remove starting and trailing
		print name
		print y
		y = y + 1
		#r = requests.post('http://localhost:1337/songnames', data = {'Name': name})

