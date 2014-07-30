from flask import Flask, redirect
from flask.ext.jsonpify import jsonify
import requests
import json
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
	return redirect('https://github.com/arushs/foodfinder')

@app.route('/<query>')
def calData(username):
	requestURL = 'http://www.epicurious.com/tools/searchresults?search=' + query
	data = requests.get(requestURL)
	file = urllib.urlopen(requesturl)
	soup = BeautifulSoup(file)
	print(soup.prettify())
	print (len(data.text))
	cutoff = 10000
	response = dict()

if __name__ == '__main__':
	app.run()
