from flask import Flask, redirect
from flask.ext.jsonpify import jsonify
from flask import render_template
import requests
import urllib
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
	return redirect('https://github.com/arushs/foodfinder')

@app.route('/<query>')
def getData(query):
	requestURL = 'http://www.epicurious.com/tools/searchresults?search=' + query
	data = requests.get(requestURL)
	file = urllib.urlopen(requestURL)
	soup = BeautifulSoup(file)
	print(soup.prettify())
	return render_template("index.html", title = "Home", user="Arush", soup=soup)

if __name__ == '__main__':
	app.run(debug=True)
