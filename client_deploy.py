import requests
import json


def post_request(server_name, action, body, node_certificate, node_key):
	request_url= 'http://www.wkbonline.net/'.format(server_name,action)
	request_headers = {
		'Content-Type': "application/json"
		}
	response = requests.post(
		url= request_url,
		data=json.dumps(body),
		headers = request_headers,
		#cert = (node_certificate, node_key),
	)

	return response

def update_content():
	repos = raw_input("New repos: ")
	scripts = raw_input("New scripts: ")
	files = raw_input

def get_content():
	content_dict = {}
	return content_dict


def main():
	server_name = 'deployment-server'
	#update_content()
	content = get_content()
	post_response = post_request(server_name,'deploy',content,'../keys/???.crt','../keys/???.key')
	for x in post_response:
		print(x,post_response[x])

if __name__ == '__main__':
	main()