import requests

r = requests.get('https://search-dcos-tutorial-2kfa5db5yllkqpnfaysztenoku.us-east-2.es.amazonaws.com/movies/_search?q=mars')
with f as open("temp_file","w+"):
	f.write(r.text)