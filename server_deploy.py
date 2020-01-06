from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json
from multiprocessing import Process

deployment_service = Flask(__name__)
api = Api(deployment_service)

class welcome(Resource):
	def get(self):
		return "Welcome to Wesley's deployment server!"

class deploy(Resource):
	def post(self):
		data = request.get_json()
		data_dict = json.loads(data)
		try:
			success = True
		except:
			success = False

		if success:
			response = {
				'status': 200,
				'message': 'Deployment Successful',
			}
		else:
			response = {
				'status': 700,
				'message': 'Deployment Failed'
			}
		return jsonify(response)

api.add_resource(welcome, '/')
api.add_resource(deploy, '/deploy')

def main():
	deployment_service.run(debug=True)

if __name__ == '__main__':
	main()