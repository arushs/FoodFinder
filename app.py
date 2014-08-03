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
	requestURL = 'http://allrecipes.com/search/default.aspx?wt=' + query
	file = urllib.urlopen(requestURL)
	soup = BeautifulSoup(file)
	divs = soup.html.findAll("div", {"id":"divGridItemWrapper"})
	myList = []
	for div in divs:
		img = div.find("img")
		myList.append([img.get("src"), img.get("title")])
	return render_template("index.html", title = "Home", user="Arush", imgs=myList)

if __name__ == '__main__':
	app.run(debug=True)
