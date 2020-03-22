from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json
from multiprocessing import Process

#Might need this: https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

deployment_service = Flask(__name__)
api = Api(deployment_service)
master_file = open('ignore_files/word_files/master.json','r')
master_dict = json.loads(master_file.read())
master_file.close()

class welcome(Resource):
	def get(self):
		return "Welcome to Wesley's deployment server!"

class deploy(Resource):
	def post(self):
		data = request.get_json()
		data_dict = json.loads(data)
		my_key = data_dict['key']
		i = 1
		response = {}
		while str(i) in data_dict:
			try:
				response.update(str(i):master_dict[str(i)][my_key])
			except:
				response.update(str(i):data_dict[str(i)])
		return jsonify(response)

api.add_resource(welcome, '/')
api.add_resource(deploy, '/deploy')

def main():
	deployment_service.run(debug=True)

if __name__ == '__main__':
	main()