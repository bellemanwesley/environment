from django.shortcuts import render
import requests
import random

def button(request):
	return(render(request,'home.html'))

def output(request):
	#data = requests.get('http://x.com')
	#print(data.text)
	#data=data.text
	print(request.GET['q'])
	data = str(random.randrange(20)) + ' ' + request.GET['q']
	return(render(request,'home.html',{'data':data}))