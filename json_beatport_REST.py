import json
import requests

with open('beatport.json') as f:
    label_chart = json.load(f)

#print(json.dumps(label_chart, indent=4))

#print(json.dumps(label_chart[0]["price"]["value"], indent=4))
artists = ""
genre = ""
slash = "/"
for number in range(len(label_chart)):
	for x in range(len(label_chart[number]["artists"])):
		artists += label_chart[number]["artists"][x]["name"]
		artists += slash
	artists = artists[:-1]
	artists = artists.encode("utf-8")
	track = label_chart[number]["name"].encode("utf-8")
	hammad = {
		"Track Name": track,
		"BPM": int(label_chart[number]["bpm"]),
		"Artist": artists,
		"Date Released": label_chart[number]["date"]["published"],
		"Genre": label_chart[number]["genres"][0]["name"]
	}
	artists = ""
	#print(json.dumps(hammad, indent=4))
	#r = requests.post('http://localhost:1337/labels', data = hammad)

r = requests.get('http://localhost:1337/labels')
jr = json.loads(r.text)
#print(json.dumps(jr, indent=4))
_id = ""
for y in range(len(jr)):
	_id = jr[y]["_id"]
	url = "http://localhost:1337/labels/"
	url += _id
	print url
	r = requests.delete(url)