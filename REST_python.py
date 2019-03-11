import requests

r = requests.delete('http://localhost:1337/posts/5c250da4bb07d17a8bfaca03')
r = requests.put('http://localhost:1337/posts/5c26798c6252350fc343b0be', data = {'BIN':'100000', 'Project':'Amanda'})
#r = requests.post('http://localhost:1337/posts', data = {'BIN':'3255039', 'Project':'Skrrrrr'})
r = requests.get('http://localhost:1337/posts')
f = open("testFile.txt", "w")
f.write(r.text)